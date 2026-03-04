==> Using Python version 3.14.3 (default)
==> Docs on specifying a Python version: https://render.com/docs/python-version
==> Using Poetry version 2.1.3 (default)
==> Docs on specifying a Poetry version: https://render.com/docs/poetry-version
==> Running build command 'pip install -r requirements.txt'...
Collecting flask (from -r requirements.txt (line 1))
  Downloading flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting flask-cors (from -r requirements.txt (line 2))
  Downloading flask_cors-6.0.2-py3-none-any.whl.metadata (5.3 kB)
Collecting tls-client (from -r requirements.txt (line 3))
  Downloading tls_client-1.0.1-py3-none-any.whl.metadata (5.0 kB)
Collecting blinker>=1.9.0 (from flask->-r requirements.txt (line 1))
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask->-r requirements.txt (line 1))
  Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2.0 (from flask->-r requirements.txt (line 1))
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask->-r requirements.txt (line 1))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask->-r requirements.txt (line 1))
  Downloading markupsafe-3.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting werkzeug>=3.1.0 (from flask->-r requirements.txt (line 1))
  Downloading werkzeug-3.1.6-py3-none-any.whl.metadata (4.0 kB)
Downloading flask-3.1.3-py3-none-any.whl (103 kB)
Downloading flask_cors-6.0.2-py3-none-any.whl (13 kB)
Downloading tls_client-1.0.1-py3-none-any.whl (41.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.3/41.3 MB 36.8 MB/s  0:00:01
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.3.1-py3-none-any.whl (108 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading markupsafe-3.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (23 kB)
Downloading werkzeug-3.1.6-py3-none-any.whl (225 kB)
Installing collected packages: tls-client, markupsafe, itsdangerous, click, blinker, werkzeug, jinja2, flask, flask-cors
Menu
Successfully installed blinker-1.9.0 click-8.3.1 flask-3.1.3 flask-cors-6.0.2 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.3 tls-client-1.0.1 werkzeug-3.1.6
[notice] A new release of pip is available: 25.3 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
==> Uploading build...
==> Uploaded in 10.9s. Compression took 4.7s
==> Build successful 🎉
==> Deploying...
==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance
==> Running 'python app.py'
python: can't open file '/opt/render/project/src/app.py': [Errno 2] No such file or directory
==> Exited with status 2
==> Common ways to troubleshoot your deploy: https://render.com/docs/troubleshooting-deploys
==> Running 'python app.py'
python: can't open file '/opt/render/project/src/app.py': [Errno 2] No such file or directory
