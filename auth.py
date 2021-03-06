import numpy as np
import base64
import requests
from datetime import datetime
from datetime import timedelta
import secret

class Auth:

    client_id = '4ff0ff28da4242aea660db21e3821e3e'
    client_secret = secret.client_secret
    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {'grant_type': 'client_credentials'}
    expires = datetime.now()

    def __init__(self):

        client_creds = f'{self.client_id}:{self.client_secret}'
        client_creds_byte = client_creds.encode()
        client_creds_b64 = base64.b64encode(client_creds_byte)
        self.token_headers = {
            'Authorization': f'Basic {client_creds_b64.decode()}'
        }

    def request_access_token(self):
        r = requests.post(self.token_url, data = self.token_data, headers=self.token_headers)
        valid_request = r.status_code in range(200, 300)
        if not valid_request:
            raise Exception('token invalid')
        now = datetime.now()
        token_response_data = r.json()
        self.access_token = token_response_data['access_token']
        expires_in = token_response_data['expires_in'] #seconds
        self.expires = now + timedelta(seconds=expires_in)
        return True
    
    def get_access_token(self):
        now = datetime.now()
        if self.expires < now:
            self.request_access_token()
        return self.access_token