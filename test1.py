
# test1.py

from scheduler import Scheduler
from controller import Controller
from task import Task, RecurringTask, TransientTask, AntiTask

def main():
       # Initialize the scheduler and controller
       scheduler = Scheduler()
       controller = Controller(scheduler)

       # Test reading Set1.json
       print("Reading Set1.json...")
       controller.read_schedule_from_file("Set1.json")

       # Test deleting the task "Intern Interview"
       print("\nDeleting the task 'Intern Interview'...")
       controller.delete_task("Intern Interview")

       # Test adding a new transient task "Intern Interview" for a different date
       print("\nAdding a new transient task 'Intern Interview' for a different date...")
       new_task1 = TransientTask("Intern Interview", "Appointment", 20200427, 17, 2.5)
       controller.create_task(new_task1)

       # Test adding a new transient task "Watch a movie" with an invalid type
       print("\nAdding a new transient task 'Watch a movie' with an invalid type...")
       new_task2 = TransientTask("Watch a movie", "Movie", 20200429, 21.5, 2)
       controller.create_task(new_task2)

       # Test adding a new transient task "Watch a movie" with a time conflict
       print("\nAdding a new transient task 'Watch a movie' with a time conflict...")
       new_task3 = TransientTask("Watch a movie", "Visit", 20200430, 18.5, 2)
       controller.create_task(new_task3)

       # Test reading Set2.json (should fail due to conflict)
       print("\nReading Set2.json...")
       controller.read_schedule_from_file("Set2.json")


if __name__ == "__main__":
       main()