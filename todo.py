#Basic To-Do Application Project By AAKHS B6 Students 
tasks = []

def add_task(task_description, priority):
    task = {
        'description': task_description,
        'priority': priority,
        'done': False
    }
    tasks.append(task)
    print(f"Task '{task_description}' added with priority {priority}.")

def complete_task(task_number):
    if 0 <= task_number < len(tasks):
        tasks[task_number]['done'] = True
        print(f"Task '{tasks[task_number]['description']}' marked as complete.")
    else:
        print("Invalid task number.")

def list_tasks():
    print("To-Do List:")
    for index, task in enumerate(tasks):
        status = 'Done' if task['done'] else 'Not Done'
        print(f"{index}: {task['description']} - Priority: {task['priority']} - Status: {status}")

def edit_task(task_number, new_description=None, new_priority=None):
    if 0 <= task_number < len(tasks):
        if new_description:
            tasks[task_number]['description'] = new_description
        if new_priority:
            tasks[task_number]['priority'] = new_priority
        print(f"Task '{task_number}' updated.")
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. List Tasks")
    print("4. Edit Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task_description = input("Enter task description: ")
        priority = input("Enter task priority (High/Medium/Low): ")
        add_task(task_description, priority)
    elif choice == '2':
        task_number = int(input("Enter task number to mark as done: "))
        complete_task(task_number)
    elif choice == '3':
        list_tasks()
    elif choice == '4':
        task_number = int(input("Enter task number to edit: "))
        new_description = input("Enter new task description (leave blank to keep current): ")
        new_priority = input("Enter new priority (leave blank to keep current): ")
        edit_task(task_number, new_description, new_priority)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1-5.")