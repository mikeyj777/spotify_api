from auth import Auth
from spotify_request import Spotify_Request

# access token in Auth.access_token
# token expiration in Auth.expires

auth = Auth()
auth.request_access_token()

request_type = 'search'
search_params = {
    'search_string': 'Time',
    'search_type': 'track'
}
spot_req = Spotify_Request(auth_token=auth.get_access_token(), request_type = request_type, request_params=search_params)
spot_req.request()
data = spot_req.data
print(data)

