from jira_request_login import get_authentication
import requests


def get_task_info(issue_key, email, api_token):
    auth, headers = get_authentication(email, api_token)
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/issue/{issue_key}"
    
    response = requests.get(url, headers=headers, auth=auth)
    
    if response.status_code == 200:
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
    

def get_task_names(issue_key, email, api_token):
    auth, headers = get_authentication(email, api_token)
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/search?jql=project=GTMS"
    
    response = requests.get(url, headers=headers, auth=auth)
    
    if response.status_code == 200:
        task_data = response.json()
        
        task_names = []
        for issue in task_data.get("issues", []):
            task_names.append(issue["fields"]["summary"])
        
        formatted_output = "\n\n".join(task_names)
        return formatted_output
    else:
        return f"Erro {response.status_code}: {response.text}"

def get_task_total(issue_key, email, api_token):
    auth,  headers = get_authentication(email, api_token)
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/search?jql=project=GTMS"

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        task_data = response.json()
        return task_data["total"]
    else:
        return f"Erro {response.status_code}: {response.text}"