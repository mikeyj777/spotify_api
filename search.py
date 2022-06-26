import requests
from urllib.parse import urlencode

class Search:
    endpoint = 'https://api.spotify.com/search'

    def __init__(self, auth_token, q_type, q_string):
        self.headers = {
            'Authorization':  f'Bearer {auth_token}'
        }

        search_params = urlencode({'q': q_string, 'type': q_type})
        self.uri = f'{self.endpoint}?{search_params}'

    def request(self):
        r = requests.get(self.uri, headers = self.headers)
        apple = 1

        valid_request = r.status_code in range(200, 300)
        if valid_request:
            pass
        return valid_request

        return 
