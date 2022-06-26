import requests
from urllib.parse import urlencode

class Spotify_Request:
    def __init__(self, auth_token, request_type, request_params):
        self.headers = {
            'Authorization':  f'Bearer {auth_token}'
        }
        if request_type == 'search':
            endpoint = 'https://api.spotify.com/v1/search'
            search_string = request_params['search_string']
            search_type = request_params['search_type']
            search_params = urlencode({'q': search_string, 'type': search_type.lower()})
            self.uri = f'{endpoint}?{search_params}'
        
        if request_type == 'playlists':
            pass


    def request(self):
        r = requests.get(self.uri, headers = self.headers)
        valid_request = r.status_code in range(200, 300)
        if not valid_request:
            raise Exception(f'search invalid.  uri {self.uri}.  response code {r.status_code}.  response string {r.json()}')
        self.data = r.json()

