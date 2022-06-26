from auth import Auth
from search import Search

# access token in Auth.access_token
# token expiration in Auth.expires

auth = Auth()
auth.request_access_token()

search_string = 'Time'
search_type = 'artist'
search = Search(auth_token=auth.get_access_token(), q_type=search_type, q_string=search_string)
search.request()

