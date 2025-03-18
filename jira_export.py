import csv

def export_to_csv(tasks, filename="info_tarefas.csv"):
    if not tasks:
        print("Nenhuma tarefa encontrada para exportação.")
        return
    
    fieldnames = ["key", "summary", "status", "assignee", "created", "resolution_date"]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        
        for task in tasks:
            writer.writerow({
                "key": task.get("key", ""),
                "summary": task["fields"].get("summary", ""),
                "status": task["fields"]["status"].get("name", ""),
                "assignee": task["fields"]["assignee"]["displayName"] if task["fields"].get("assignee") else "Unassigned",
                "created": task["fields"].get("created", ""),
                "resolution_date": task["fields"].get("resolutiondate", "")  # Pode ser None
            })

    print(f"Dados exportados para {filename}")
