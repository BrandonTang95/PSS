
# scheduler.py

import json
from datetime import datetime, timedelta
from task import TransientTask, RecurringTask, AntiTask

class Scheduler:
    
    # Valid task types
    VALID_TASK_TYPES = {"Class", "Study", "Sleep", "Exercise", "Work", "Meal", "Visit", "Shopping", "Appointment", "Cancellation"}

    # Initialize the scheduler
    def __init__(self):
        self.task_list = []

    ########## Task Methods ##########
    
    # Adds a task to the list of tasks in the scheduler.
    # It will verify the task parameters before adding it in the list.
    def add_task(self, task): 
        task_dict = {
            'Name' : task.name,
            'Type' : task.task_type,
            'Date' : task.date,
            'StartTime' : task.start_time,
            'Duration' : task.duration
        }
        
        # Some task types might have additional or fewer fields, handle them with conditionals
        if hasattr(task, 'start_date'):
            task_dict['StartDate'] = task.start_date
        if hasattr(task, 'end_date'):
            task_dict['EndDate'] = task.end_date
        if hasattr(task, 'frequency'):
            task_dict['Frequency'] = task.frequency  
        
        self.task_list.append(task_dict)  
        
        # print("Debug: Check tasks after adding task.")
        # for i in self.task_list:
        #     print(i)

    # Deletes a task from the list of tasks.
    # Scans the list of task for a name match. If match, delete. Otherwise, task is not found.
    def delete_task(self, task_name):
        
        task_to_delete = None
        
        for task in self.task_list:
            if task['Name'] == task_name:
                task_to_delete = task
                print(f"Matching task name:'{task_name}' has been found.")

        
        if task_to_delete:
            self.task_list.remove(task_to_delete)
            print(f"Task '{task_name}' has been deleted successfully.")
        else:
            print(f"Task '{task_name}' not found.")
        
        # print("Debug: Check tasks after deleting task.")
        # for i in self.task_list:
        #     print(i)
    
    # Prints out the task list
    def display_tasks(self):
        for i in self.task_list:
            print(i)
    
    def view_task(self, name):
        # Implementation work in progress...
        pass
        
        
    def edit_task(self, name):
        # Implementation work in progress...
        pass

    # Reads the JSON file and populates task list
    def read_schedule_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                task_data = json.load(file)
                
                # Append JSON objects to task_list
                for t in task_data:
                    self.task_list.append(t)
                
                print("Debug: Print tasks in scheduler.")
                for i in self.task_list:
                    print(i)
                
                print("Schedule loaded successfully.")
                
        except Exception as e:
            print(f"Failed to load tasks due to: {e}")
            return False
        
    