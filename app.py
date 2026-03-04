import tls_client
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def health_check():
    return "Sunucu Aktif!", 200

@app.route('/api/get_stats', methods=['POST'])
def get_stats():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"success": False, "message": "Eksik bilgi!"}), 400

    session = tls_client.Session(client_identifier="chrome_120")
    
    try:
        # Riot Auth
        auth_url = "https://auth.riotgames.com/api/v1/authorization"
        session.post(auth_url, json={
            "client_id": "play-valorant-web-client",
            "nonce": "1",
            "redirect_uri": "https://playvalorant.com/opt_in",
            "response_type": "token id_token",
            "scope": "account openid"
        })

        login_res = session.put(auth_url, json={"type": "auth", "username": username, "password": password}).json()

        if "error" in login_res:
            return jsonify({"success": False, "message": "Giriş başarısız!"})

        auth_uri = login_res['response']['parameters']['uri']
        access_token = re.search('access_token=([^&]+)', auth_uri).group(1)
        
        ent_headers = {"Authorization": f"Bearer {access_token}"}
        ent_token = session.post("https://entitlements.riotgames.com/api/token/v1", headers=ent_headers, json={}).json()['entitlements_token']
        user_id = session.get("https://auth.riotgames.com/userinfo", headers=ent_headers).json()['sub']

        # Cüzdan Sorgusu
        wallet = session.get(f"https://pd.eu.a.pvp.net/store/v1/wallet/{user_id}", headers={
            "Authorization": f"Bearer {access_token}",
            "X-Riot-Entitlements-JWT": ent_token
        }).json()

        vp = wallet['Balances'].get('86ca2b34-591d-45a0-9bc6-e26522c00249', 0)
        rad = wallet['Balances'].get('e5912443-410a-4a90-835c-204b77d6ba58', 0)

        return jsonify({"success": True, "vp": vp, "rad": rad})

    except Exception as e:
        return jsonify({"success": False, "message": "Bağlantı hatası!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
