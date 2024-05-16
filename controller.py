
import sys
from task import TransientTask, RecurringTask, AntiTask
from scheduler import Scheduler

########## Controller ##########
#
# The controller is the main object that interacts with the user.
# It decides what actions to take based on user input.

# Work in progress at the moment...

class Controller:
    def main():
        # Initialize the scheduler
        scheduler = Scheduler()

        # Read tasks from a file
        filename = input("Enter the file name to load tasks from: ")
        
        try:
            scheduler.readschedulefromfile(filename)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Exiting program.")
            sys.exit(1)

        while True:
            print("\nOptions:")
            print("1. Create a task")
            print("2. Delete a task")
            print("3. View tasks")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter task name: ")
                task_type = input("Enter task type: ")
                date = input("Enter task date: ")
                start_time = input("Enter task start time: ")
                duration = input("Enter task duration: ")
                task = TransientTask(name, task_type, date, start_time, duration)
                scheduler.create_task(task)

            elif choice == "2":
                task_name = input("Enter the name of the task to delete: ")
                scheduler.delete_task(task_name)
            elif choice == "3":
                print("\nTasks:")
                for task in scheduler.task_list:
                    print(task)
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose again.")

    if __name__ == "__main":
        main()
