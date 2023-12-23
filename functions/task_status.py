def task_status(tasks, task_index):
    status = input("enter task completion percentage : ")
    tasks[task_index - 1]['status'] = status
    print("status edited successfully.")
