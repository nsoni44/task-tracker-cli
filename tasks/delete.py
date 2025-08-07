import json

def delete_task(index, file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            if content.strip():
                tasks = json.loads(content)
            else:
                return False

        if 0 <= index < len(tasks):
            tasks.pop(index)
            with open(file_path, 'w') as f:
                json.dump(tasks, f, indent=2)
            return True
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return False
