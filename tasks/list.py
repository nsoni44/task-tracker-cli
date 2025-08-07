import json

def list_tasks(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []
