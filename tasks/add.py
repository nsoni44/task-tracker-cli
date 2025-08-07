import json

def add_task(task_text, file_path):
    tasks = []
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            if content.strip():
                tasks = json.loads(content)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass  # Handle corrupt/invalid JSON

    tasks.append({"task": task_text})

    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=2)
