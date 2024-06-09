class TodoList:
    def _init_(self):
        self.tasks = []
    def add_task(self,task):
        self.tasks.append(task)
        print("Task added successfully")
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully")
        else:
                print("Task not found in the list")
    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index,task in enumerate(self.tasks,start=1):
                print(f"{index}.{task}")
        else:
            print("Your To-Do List is empty")
def main():
    todo_list = TodoList()
    while True:
        print("\n1.Add Task")
        print("2.Remove Task")
        print("3.Display Task")
        print("4.Exit")
        choice = input("enter your choice:")
        if choice == '1':
            task=input("enter the task:")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.Please try again")

if _name_ == "_main_":
    main()
