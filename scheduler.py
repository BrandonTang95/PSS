
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
        if task.task_type not in self.VALID_TASK_TYPES:
            print(f"Error: '{task.task_type}' is not a valid task type.")
            return 
        
        if any(t.name == task.name for t in self.tasks):
            print("Error: Task name must be unique.")
            return 
        
        if self.is_overlapping(task):
            print(f"Error: Task '{task.name}' overlaps with an existing task.")
            return 
        
        self.tasks.append(task)
        print(f"Task '{task.name}' added successfully.")
        
    
    # def delete_task(self, task_name):

    
    # def view_task(self, name):

        
    # def edit_task(self, name, ):
        

    # Reading Test Files
    def read_schedule_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                for i in data:
                    print(i)
                print("Schedule loaded successfully.")
                
        except Exception as e:
            print(f"Failed to load tasks due to: {e}")
            return False
        
    # def write_schedule_to_file(self, file_name):
            
            
    # def view_schedule(self, start_date, period):
    

    
    