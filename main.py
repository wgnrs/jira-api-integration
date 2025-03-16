from jira_project import get_project_info
from jira_task import get_task_info

email = "wagner.silva@atlasinovacoes.com.br"
api_token = "ATATT3xFfGF0t7j6k7Nf2dLGSUfUv1XUDiVW1UTl05cLKUV2eZY3Ymi3hhSDWKAHfvtpogwpsvKkwP6yQ4Y0eYqmAqqbfM16Q4Mg8Hn9nUtvR7BFbqFulq6np1k8JcQEGn4Vmp6ZxVwJVH_F_o8dzOlDbJD_CwbeLMJNvakiLTz1fsoeyBaE8nU=0673AA8B"

project_info = get_project_info(10001, email, api_token)
print(project_info)

task_info = get_task_info("SCRUM-1", email, api_token)
print(task_info)

#testaaa