def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

def add_task(tasks):
    task_id = input("Enter task number: ")
    if task_id in tasks:
        print("Task already exists")
    else:
        task_desc = input("Enter the description of the task: ")
        tasks[task_id] = {"desc": task_desc, "done": False}
        print(f"Task {task_id} added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        print("\n===== To-Do List =====")
        for task_id, task in tasks.items():
            if task["done"]:
                status = "✓ Done"
            else:
                status = "✗ Pending"
            print(f"{task_id}: {task['desc']} [{status}]")


def mark_done(tasks):
    task_id = input("Enter task number: ")
    if task_id in tasks:
        tasks[task_id]["done"] = True
        print(f"Task {task_id} marked as done!")
    else:
        print("Task not found")


def remove_task(tasks):
    task_id = input("Enter task number: ")
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} removed successfully!")
    else:
        print("Task not found")
    



def main():
    tasks = {}  # Dictionary to store tasks
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
