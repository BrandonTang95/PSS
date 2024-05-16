
import json
from datetime import datetime, timedelta
from task import TransientTask, RecurringTask, AntiTask

class Scheduler:
    
    # Global Class Variables
    VALID_TASK_TYPES = {"Class", "Study", "Sleep", "Exercise", "Work", "Meal", "Visit", "Shopping", "Appointment", "Cancellation"}

    # Initialize the scheduler
    def __init__(self):
        self.task_list = []

    # Task Methods 
    def create_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.name}' added successfully.")

    # def delete_task(self, task_name):

    
    # def view_task(self, name):

        
    # def edit_task(self, name):


    # Reading Test Files
    def read_schedule_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                task_data = json.load(file)
                for i in task_data:
                    print(i)
                print("Schedule loaded successfully.")
                
        except Exception as e:
            print(f"Failed to load tasks due to: {e}")
            return False
        
    # def write_schedule_to_file(self, file_name):
        
        
    # def view_schedule(self, start_date, period):
        
        