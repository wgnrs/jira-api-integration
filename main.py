from jira_project import get_project_info
from jira_task import get_task_info, get_task_details

email = "wagner.silva@atlasinovacoes.com.br"
api_token = "ATATT3xFfGF0t7j6k7Nf2dLGSUfUv1XUDiVW1UTl05cLKUV2eZY3Ymi3hhSDWKAHfvtpogwpsvKkwP6yQ4Y0eYqmAqqbfM16Q4Mg8Hn9nUtvR7BFbqFulq6np1k8JcQEGn4Vmp6ZxVwJVH_F_o8dzOlDbJD_CwbeLMJNvakiLTz1fsoeyBaE8nU=0673AA8B"

project_info = get_project_info(10001, email, api_token)

task_info = get_task_info("SCRUM-1", email, api_token)
#print("task info: \n", task_info)

task_details = get_task_details("SCRUM-1", email, api_token)
#print("\n\n Detalhes da Task: \n", task_details)


#fazendo um teste aqui de chave valor
if 'issues' in task_info:
    issues = task_info['issues']
    print(f"quantidade de issues {len(issues)}")
else:
    print("A chave 'issues' não foi encontrada na resposta.")