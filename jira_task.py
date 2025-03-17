from jira_request_login import get_authentication
import requests

def get_all_tasks(project_key, email, api_token):
    """
    Retorna uma lista de issues (tasks) do projeto indicado pela chave.
    """
    auth, headers = get_authentication(email, api_token)
    # Utilize a query JQL para filtrar as tasks do projeto (por exemplo, GTMS)
    url = f"https://atlasinovacoes-ws-testes-consumacao.atlassian.net/rest/api/3/search?jql=project={project_key}&maxResults=100"
    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code == 200:
        data = response.json()
        return data["issues"]
    else:
        raise Exception(f"Erro {response.status_code}: {response.text}")

from datetime import datetime


from datetime import datetime

def aggregate_tasks_by_assignee(project_key, email, api_token):
    """
    Agrega os dados das tasks do projeto, agrupando por colaborador.
    Para cada colaborador, calcula:
      - Total de tasks atribuídas
      - Total de tasks concluídas
      - Tempo médio de resolução (em horas)
    """
    tasks = get_all_tasks(project_key, email, api_token)  # Função que retorna todas as tasks do projeto
    
    aggregation = {}
    
    for issue in tasks:
        fields = issue.get("fields", {})
        assignee_info = fields.get("assignee")
        assignee = assignee_info["displayName"] if assignee_info else "Unassigned"
        
        if assignee not in aggregation:
            aggregation[assignee] = {
                "total_tasks": 0,
                "completed_tasks": 0,
                "total_resolution_time": 0,  # total em segundos
                "num_resolved": 0
            }
        
        aggregation[assignee]["total_tasks"] += 1
        
        # Verifica se a task foi concluída (se resolutiondate estiver preenchido)
        if fields.get("resolutiondate"):
            aggregation[assignee]["completed_tasks"] += 1
            
            try:
                created_str = fields.get("created")
                resolution_str = fields.get("resolutiondate")
                # Exemplo de formato: "2025-03-14T12:22:39.518-0300"
                created = datetime.strptime(created_str, "%Y-%m-%dT%H:%M:%S.%f%z")
                resolution = datetime.strptime(resolution_str, "%Y-%m-%dT%H:%M:%S.%f%z")
                delta = resolution - created
                aggregation[assignee]["total_resolution_time"] += delta.total_seconds()
                aggregation[assignee]["num_resolved"] += 1
            except Exception as e:
                print(f"Erro ao calcular tempo para {issue['key']}: {e}")
    
    # Calcula a média de tempo de resolução para cada colaborador, convertendo para horas
    result = []
    for assignee, stats in aggregation.items():
        avg_hours = None
        if stats["num_resolved"] > 0:
            # Divide o total de segundos pela quantidade de tarefas resolvidas e converte para horas
            avg_hours = stats["total_resolution_time"] / stats["num_resolved"] / 3600
            avg_hours = round(avg_hours, 2)  # arredonda para 2 casas decimais
        result.append({
            "assignee": assignee,
            "total_tasks": stats["total_tasks"],
            "completed_tasks": stats["completed_tasks"],
            "avg_resolution_time_hours": avg_hours
        })
    
    return result


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