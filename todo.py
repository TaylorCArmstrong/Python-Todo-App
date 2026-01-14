tasks = []

def Add():
    task = input("Add Your Task: ")
    tasks.append(task)
    print(f"Task '{task}' added!\n")

def View():
    print("\nYour tasks:")
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks yet.")
    print()

def Delete():
    if not tasks:
        print("No tasks to delete.\n")
        return
    View()
    try:
        index = int(input("Choose a task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed}' deleted!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

 