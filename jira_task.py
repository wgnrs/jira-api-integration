import requests
from requests.auth import HTTPBasicAuth

def get_task_info(issue_key, email, api_token):
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/issue/{issue_key}"
    auth = HTTPBasicAuth(email, api_token)
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erro {response.status_code}: {response.text}"
