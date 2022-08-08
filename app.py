import os
from flask import Flask, Response
import requests


url = os.getenv('APP_REQUEST_URL')
print(url)
if url is None or len(url.strip()) == 0:
    raise Exception('APP_REQUEST_URL env is required')
elif not url.lower().startswith('http://') and not url.lower().startswith('https://'):
    raise Exception(f'APP_REQUEST_URL should start with http:// or https://')

header_bearer_token = os.getenv('APP_REQUEST_BEARER_TOKEN', None)
header_bearer_token_path = os.getenv('APP_REQUEST_BEARER_TOKEN_PATH', None)

app = Flask(__name__)

@app.route("/")
def root():
    headers = {}
    if header_bearer_token_path is not None:
        if os.path.isfile(header_bearer_token_path):
            with open(header_bearer_token_path) as f:
                token = f.read()
                headers['Authorization'] = f'Bearer {token}'
    elif header_bearer_token is not None:
        headers['Authorization'] = f'Bearer {header_bearer_token}'

    r = requests.get(url, headers=headers)
    if r.ok:
        response = Response(r.text)
        response.headers['content-type'] = r.headers['content-type']  # same as the original reques
        response.headers['x-meta'] = 'status=ok'  # extra information
        return response
    else:
        return Response(r.text, status=r.status_code)
