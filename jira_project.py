import requests
from jira_request_login import get_authentication

def get_project_info(project_id, email, api_token):
    auth, headers = get_authentication(email, api_token)
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/project/{project_id}"
    
    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code == 200:
        project = response.json()
        print(f"ID do projeto: {project['id']}, Nome do projeto: {project['name']}")
    else:
        print(f"Erro {response.status_code}: {response.text}")
