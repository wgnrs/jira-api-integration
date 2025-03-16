import requests
from requests.auth import HTTPBasicAuth

def make_request(issue_key, email, api_token):
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/issue/{issue_key}"
    auth = HTTPBasicAuth(email, api_token)
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, auth=auth)
    return response
