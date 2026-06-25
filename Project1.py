
the_todo_list = []

def add_task():
    task = input("Enter the task you want to add: ")
    the_todo_list.append({"task": task, "status": "pending"})
    print(f'Task "{task}" added to the list.\n')  

def view_tasks():
    if not the_todo_list:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        for index, item in enumerate(the_todo_list, start=1):
            print(f"{index}. {item['task']} - {item['status']}")
            print("\n")  
def remove_task():
    if not the_todo_list:
        print("No tasks to remove.")
    else:
        try:
             search_index = int(input("Enter the task number you want to remove: ")) - 1
             if 0 <= search_index < len(the_todo_list):
                removed_task = the_todo_list.pop(search_index)
                print(f'Task "{removed_task["task"]}" removed from the list.\n')
             else:
                print("Invalid task number.") 
        except ValueError:
                print("Please enter a valid number.")    
def mark_task_completed():
    if not the_todo_list:
        print("No tasks to mark as completed.")
    else:
        try:
            search_index = int(input("Enter the task number you want to mark as completed: ")) - 1
            if 0 <= search_index < len(the_todo_list):
                the_todo_list[search_index]["status"] = "completed"
                print(f'Task "{the_todo_list[search_index]["task"]}" marked as completed.\n')
            else:
                print("Invalid task number.") 
        except ValueError:
                print("Please enter a valid number.")                
def menu():
    while(True):
        print("\n**To-Do List Menu:**")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()    
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_completed()   
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            exit() 
        else:
            print("Invalid choice. Please try again.")

menu()
