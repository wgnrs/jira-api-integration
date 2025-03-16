import requests
from requests.auth import HTTPBasicAuth

import requests
from requests.auth import HTTPBasicAuth

def get_project_info(project_id, email, api_token):
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/project/{project_id}"
    auth = HTTPBasicAuth(email, api_token)
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        project = response.json()
        print(f"ID do projeto: {project['id']}, Nome do projeto: {project['name']}")
    else:
        print(f"Erro {response.status_code}: {response.text}")
