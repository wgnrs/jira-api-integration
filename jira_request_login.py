from requests.auth import HTTPBasicAuth

def get_authentication(email, api_token):
    auth = HTTPBasicAuth(email, api_token)
    headers = {
        "Accept": "application/json"
    }
    return auth, headers
