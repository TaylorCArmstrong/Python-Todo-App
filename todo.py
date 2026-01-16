tasks = []

def Add():

    try:
        task = input("Add Your Task: ")

        if not task.strip():
            print("Error: Task cannot be empty.\n")
            return

        tasks.append(task)

    except KeyboardInterrupt:
        print("\n\nTask addition cancelled.\n")
    except Exception as e:
        print(f"An error occurred while adding task: {e}\n")
    else:
        print(f"Task '{task}' added successfully!\n")
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

def display_menu():
    """
    Display menu options to the user.
    """
    print("=" * 40)
    print("Menu Options:")
    print("  - Add: Add a new task")
    print("  - View: View all tasks")
    print("  - Delete: Delete a task")
    print("  - Quit: Exit the application")
    print("=" * 40)
    
def main():
    """
    Main function to run the Todo List application.
    Displays welcome message and handles user selections.
    """

    print("\n" + "=" * 40)
    print("Welcome to your ToDo List Application!")
    print("=" * 40 + "\n")

    while True:
        try:

            display_menu()

            choice = input("\nPlease type your option (Add/View/Delete/Quit): ").strip().lower()
            print()

            if choice == 'add':
                Add()
            elif choice == 'view':
                View()
            elif choice == 'delete':
                Delete()
            elif choice == 'quit':
                print("Thank you for using ToDo List! Goodbye!")
                break
            else:
                print(f"Error: '{choice}' is not a valid option. Please choose from Add, View, Delete, or Quit.")

        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
        finally:
            pass

if __name__ == "__main__":
    main()            