import tls_client
from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
# CORS ayarı: Senin .gt.tc sitenden gelen isteklere izin verir
CORS(app)

@app.route('/')
def home():
    return "Valorant API Sunucusu Calisiyor!"

@app.route('/api/get_stats', methods=['POST'])
def get_stats():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"success": False, "message": "Kullanıcı adı veya şifre eksik!"}), 400

    # Modern tarayıcı taklidi yapan güvenli oturum
    session = tls_client.Session(client_identifier="chrome_120")
    
    try:
        # 1. Adım: Riot Auth Başlatma
        auth_url = "https://auth.riotgames.com/api/v1/authorization"
        init_body = {
            "client_id": "play-valorant-web-client",
            "nonce": "1",
            "redirect_uri": "https://playvalorant.com/opt_in",
            "response_type": "token id_token",
            "scope": "account openid"
        }
        session.post(auth_url, json=init_body)

        # 2. Adım: Giriş Yapma
        login_body = {"type": "auth", "username": username, "password": password}
        response = session.put(auth_url, json=login_body).json()

        if "error" in response:
            return jsonify({"success": False, "message": "Riot bilgileri hatali!"})

        # 3. Adım: Token Ayıklama
        auth_uri = response['response']['parameters']['uri']
        access_token = re.search('access_token=([^&]+)', auth_uri).group(1)
        
        # 4. Adım: Entitlements Token ve UserID Alma
        ent_headers = {"Authorization": f"Bearer {access_token}"}
        ent_res = session.post("https://entitlements.riotgames.com/api/token/v1", headers=ent_headers, json={})
        ent_token = ent_res.json()['entitlements_token']
        
        user_info = session.get("https://auth.riotgames.com/userinfo", headers=ent_headers).json()
        user_id = user_info['sub']

        # 5. Adım: Cüzdan Verilerini Çekme (EU/TR bölgesi için)
        wallet_headers = {
            "Authorization": f"Bearer {access_token}",
            "X-Riot-Entitlements-JWT": ent_token
        }
        wallet = session.get(f"https://pd.eu.a.pvp.net/store/v1/wallet/{user_id}", headers=wallet_headers).json()

        # VP ve Radianite ID'leri
        vp = wallet['Balances'].get('86ca2b34-591d-45a0-9bc6-e26522c00249', 0)
        rad = wallet['Balances'].get('e5912443-410a-4a90-835c-204b77d6ba58', 0)

        return jsonify({
            "success": True,
            "vp": vp,
            "rad": rad
        })

    except Exception as e:
        return jsonify({"success": False, "message": "Sunucu hatasi oluştu!"})

if __name__ == '__main__':
    # Render için 0.0.0.0 host ayarı zorunludur
    app.run(host='0.0.0.0', port=10000)
