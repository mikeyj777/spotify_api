from auth import Auth
from search import Search

# access token in Auth.access_token
# token expiration in Auth.expires

auth = Auth()
if not auth.send_request():
    raise Exception('token invalid')

search_string = 'Time'
search_type = 'artist'
search = Search(auth.access_token, search_string, search_type)
if not search.request():
    raise Exception('search invalid')
print('hi')
