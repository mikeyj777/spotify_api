from auth import Auth

# access token in Auth.access_token
# token expiration in Auth.expires

auth = Auth()
if not auth.send_request():
    raise Exception('token invalid')
access_token = auth.access_token
print(access_token)
