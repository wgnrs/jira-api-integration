import requests
from jira_request_login import make_request

def get_project_info(project_id, email, api_token):
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        project = response.json()
        print(f"ID do projeto: {project['id']}, Nome do projeto: {project['name']}")
    else:
        print(f"Erro {response.status_code}: {response.text}")
