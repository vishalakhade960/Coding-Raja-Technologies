tasks = []

# Function to add a task
def add_task(task_name, priority, due_date):
    tasks.append({"name": task_name, "priority": priority, "due_date": due_date, "completed": False})

# Function to remove a task
def remove_task(task_index):
    del tasks[task_index]

# Function to mark a task as completed
def mark_completed(task_index):
    tasks[task_index]["completed"] = True

# Function to display tasks
def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Task List:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index + 1}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

# Main function
def main():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date = input("Enter due date (optional): ")
            add_task(name, priority, due_date)
            print("Task added successfully.")

        elif choice == "2":
            if tasks:
                display_tasks()
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    remove_task(index)
                    print("Task removed successfully.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to remove.")

        elif choice == "3":
            if tasks:
                display_tasks()
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(tasks):
                    mark_completed(index)
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to mark as completed.")

        elif choice == "4":
            display_tasks()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
