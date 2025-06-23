tasks = []

def welcome():
    print("Welcom to my to-do list!")
    print("------------------------")
    print("1. Add task")
    print("2. View the task")
    print("3. Mark the task")
    print("4. Remove the task")
    print("------------------------")
    print("5. Exit")

def add_task():
    choice = input("Choose your task sir: ")
    tasks.append(choice)
    print("Task has been added successfully!")

def view_task():
    i = 1
    for task in tasks:
        print(f"Task {i}: {task}")
        i += 1

def mark():
    task_number = int(input("Enter your task number: ")) -1
    if task_number > 0 and task_number < len(tasks):
        tasks[task_number] = f"{tasks[task_number]} - completed"
        print("Task marked as completed.")
    else:
        print("Invalid task number")

def delete():
        task_number = int(input("Enter your task number: "))
        if task_number > 0 and task_number < len(tasks):
             tasks.remove(tasks[task_number])
             print("Task deleted.")
        else:
             print("invalid number ma'am")

def main():
    welcome()
    while True:

        choice = input("choose an option")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
    
        elif choice == "3":
            mark()

        elif choice == "4":
            delete()

        elif choice == "5":
            print("thank you and bye now")
            return
    
        else:
            print("invalid input")

main()