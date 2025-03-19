import csv
import json

def export_to_csv(tasks, filename="info_tarefas.csv"):
    if not tasks:
        print("Nenhuma tarefa encontrada para exportação.")
        return
    
    fieldnames = ["key", "summary", "status", "priority", "assignee", "created", "resolution_date"]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        
        for task in tasks:
            writer.writerow({
                "key": task.get("key", ""),
                "summary": task["fields"].get("summary", ""),
                "status": task["fields"]["status"].get("name", ""),
                "priority": task["fields"]["priority"].get("name", ""),
                "assignee": task["fields"]["assignee"]["displayName"] if task["fields"].get("assignee") else "Unassigned",
                "created": task["fields"].get("created", ""),
                "resolution_date": task["fields"].get("resolutiondate", "")  # Pode ser None
            })

    print(f"Dados exportados para {filename}")



def export_to_json(tasks, filename="info_tarefas.json"):
    if not tasks:
        print("Nenhuma tarefa encontrada para exportação.")
        return
    
    # Formatar os dados das tarefas conforme necessário
    formatted_tasks = []
    
    for task in tasks:
        formatted_task = {
            "key": task.get("key", ""),
            "summary": task["fields"].get("summary", ""),
            "status": task["fields"]["status"].get("name", ""),
            "priority": task["fields"]["priority"].get("name", ""),
            "assignee": task["fields"]["assignee"]["displayName"] if task["fields"].get("assignee") else "Unassigned",
            "created": task["fields"].get("created", ""),
            "resolution_date": task["fields"].get("resolutiondate", "")  # Pode ser None
        }
        formatted_tasks.append(formatted_task)
    
    # Escrever os dados formatados no arquivo JSON
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(formatted_tasks, file, ensure_ascii=False, indent=4)
    
    print(f"Dados exportados para {filename}")


