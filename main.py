from tasks.add import add_task
from tasks.list import list_tasks
from tasks.delete import delete_task

import os

DATA_FILE = os.path.join("data", "tasks.json")

def main():
    while True:
        print("\nTask Tracker:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(task, DATA_FILE)
            print("✅ Task added.")
        elif choice == "2":
            tasks = list_tasks(DATA_FILE)
            if not tasks:
                print("📭 No tasks found.")
            for idx, t in enumerate(tasks):
                print(f"{idx + 1}. {t['task']}")
        elif choice == "3":
            tasks = list_tasks(DATA_FILE)
            for idx, t in enumerate(tasks):
                print(f"{idx + 1}. {t['task']}")
            index = int(input("Enter task number to delete: ")) - 1
            if delete_task(index, DATA_FILE):
                print("🗑️ Task deleted.")
            else:
                print("⚠️ Invalid task number.")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
