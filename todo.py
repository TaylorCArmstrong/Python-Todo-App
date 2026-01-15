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
        
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}\n")
    else:
        print()
    finally:
        pass


def Delete():

    try:
        if not tasks:
            print("List empty,no tasks to delete.\n")
            return
        
        View()

        user_input = input("choose a task number to delete: ")

        index = int(user_input) - 1

        if index < 0 or index >= len(tasks):
            print(f"Error: Task number {user_input} doesnt exist. Please choose a valid task number.\n")
            return
        
        removed = tasks.pop(index)


    except ValueError:
        print("Error: Please enter a valid number.\n")
    except KeyboardInterrupt:
        print("\n\nTask deletion cancelled.\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")
    else:
        print(f"Task '{removed}' deleted successfully!\n")
    finally:
        pass

    