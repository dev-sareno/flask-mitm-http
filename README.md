# Flask MITM HTTP
A web app that act as man-in-the-middle (MITM) to make HTTP GET request in behalf of the user and returns the response.

## Parameters
* `APP_REQUEST_URL` (Required) - The target URL for GET request (with prefix http:// or https://)
* `APP_REQUEST_BEARER_TOKEN` (Optional) - Token for `headers['Authorization'] = 'Bearer <token>'`
* `APP_REQUEST_BEARER_TOKEN_PATH` (Optional) - File path of the token for `headers['Authorization'] = 'Bearer <token>'`

## Requirements
* Python 3.8.10

## Dev
Prepare Python environment
```sh
python -m venv .venv
source .venv/bin/activate
```

Install requirements
```sh
pip install pip --upgrade
pip install -r requirements.txt
```

Run
```sh
FLASK_APP=app.py flask run --host=0.0.0.0 --port=8000
```

Open app at [http://localhost:8000](http://localhost:8000)

## Docker
Docker hub link: [https://hub.docker.com/r/devsareno/flask-mitm-http](https://hub.docker.com/r/devsareno/flask-mitm-http)

Run
```sh
docker run --rm -p 8000:8000 -e APP_REQUEST_URL=https://github.com/dev-sareno/flask-mitm-http devsareno/flask-mitm-http
```
