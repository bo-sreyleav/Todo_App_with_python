from datetime import datetime
import json

class TodoLish:
    def __init__(self):
        self.tasks = []
        self.filename = "task.json"
        self.load_tasks()

    def add_task(self, description):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{description}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print ("\nNo tasks found. Your to-do list is empty.")
            return
        print("\nYour To-Do List:")
        print("-" * 50)
        for task in self.tasks:
            status = "Done" if task['completed'] else "Pending"
            print(f"{task['id']}. [{status}] {task['description']}")
        print("-" * 50)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task '{task_id}' marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task '{task_id}' deleted successfully.")
                return
        print(f"Task with ID {task_id} not found.")

    def save_tasks(self):
        with open(self.filename, 'w') as file:  
            json.dump(self.tasks, file, indent=2) 

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError): 
            self.tasks = [] 

# MOVED: This function is now OUTSIDE the class
def main():
    todo_lish = TodoLish()  

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            description = input("Enter task description: ")
            todo_lish.add_task(description)
        elif choice == '2':
            todo_lish.view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo_lish.complete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo_lish.delete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
