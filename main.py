from jira_task import get_all_tasks, aggregate_tasks_by_assignee
from jira_export import export_to_csv, export_to_json

email = "wagner.silva@atlasinovacoes.com.br"
api_token = "ATATT3xFfGF0t7j6k7Nf2dLGSUfUv1XUDiVW1UTl05cLKUV2eZY3Ymi3hhSDWKAHfvtpogwpsvKkwP6yQ4Y0eYqmAqqbfM16Q4Mg8Hn9nUtvR7BFbqFulq6np1k8JcQEGn4Vmp6ZxVwJVH_F_o8dzOlDbJD_CwbeLMJNvakiLTz1fsoeyBaE8nU=0673AA8B"
project_key = "GTMS"
issue_key = 'GTMS'


def main():
    # Obter todas as tasks do projeto
    try:
        tasks = get_all_tasks(project_key, email, api_token)
        print(f"Total de tasks retornadas: {len(tasks)}")
        export_to_json(tasks)
    except Exception as e:
        print(f"Erro ao obter tasks: {e}")
        return

    # Agregar as informações por colaborador (assignee)
    try:
        aggregated_data = aggregate_tasks_by_assignee(project_key, email, api_token)
        print("\nDados agregados por colaborador:")
        for data in aggregated_data:
            print(data)
    except Exception as e:
        print(f"Erro ao agregar tasks: {e}")

if __name__ == "__main__":
    main()