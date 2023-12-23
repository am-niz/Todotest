import os
from ..functions import add_task
from ..functions import delete_task
from ..functions import edit_task
from ..functions import task_status
from ..functions import view_task
from ..functions import save_task

def load_tasks_from_file(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                title, status = line.strip().split('|')
                tasks.append({'title': title, 'status': status})
    return tasks

def main():
    file_path = "data/tasks.txt"
    tasks = load_tasks_from_file(file_path)

    while True:
        print("\n1. Display tasks\n2. Add task\n3. Edit task\n4. Change task status\n5. Delete task\n6. Save and Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_task(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            task_index = int(input("Enter the task index to edit: "))
            new_task = input("Enter the new task: ")
            edit_task(tasks, task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter the task index : "))
            task_status(tasks, task_index)
        elif choice == '5':
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == '6':
            save_task(tasks, file_path)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

main()
