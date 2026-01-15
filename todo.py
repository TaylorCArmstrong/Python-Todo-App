tasks = []

def Add():

    try:
        task = input("Add Your Task: ")

        if not task.strip():
            print("Error: Task cannot be empty.\n")
            return

        tasks.append(tasks)

    except KeyboardInterrupt:
        print("\n\nTask addition cancelled.\n")
    except Exception as e:
        print(f"An error occurred while adding task: {e}\n")
    else:
        print(f"Task '{task}' added sucessfully!\n")
    finally:
        pass

def View():

    try:
        print("\nYour tasks:")

        if not tasks:
            print("No tasks to view. Your list is empty.\n")
            return


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

while True:
    greeting = input ('Welcome to your Todo list! Please type your option: Add, View, Delete, Quit: ').strip().lower()

    if greeting == 'add':
        Add()
    elif greeting == 'view':
        View()
    elif greeting == 'delete':
        Delete()
    elif greeting == 'quit':
        print("Goodbye!")
        break
    else:
        print("invalid option. Please try again.\n")