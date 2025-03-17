import json
from jira_request_login import get_authentication
import requests

def get_task_info(issue_key, email, api_token):
    auth, headers = get_authentication(email, api_token)
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/issue/{issue_key}"
    
    response = requests.get(url, headers=headers, auth=auth)
    
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        return response.json()
    else:
        return f"Erro {response.status_code}: {response.text}"

def get_task_details(issue_key, email, api_token):
    auth, headers = get_authentication(email, api_token)
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/issue/{issue_key}"

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        task_data = response.json()
        details = {
            "summary": task_data["fields"]["summary"],
            "status": task_data["fields"]["status"]["name"],
            "assignee": task_data["fields"]["assignee"]["displayName"] if task_data["fields"]["assignee"] else "Unassigned"
        }
        return details
    else:
        return f"Erro {response.status_code}: {response.text}"
