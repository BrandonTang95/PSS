
# scheduler.py

# Imports
import json
from datetime import datetime, timedelta
from task import RecurringTask, TransientTask, AntiTask

# Scheduler Class
class Scheduler:
       
       # Initialize the scheduler.
       def __init__(self):
              self.tasks = []
       
       
       
       # Add a task to the scheduler.
       def add_tasks(self, task):
              self.tasks.append(task)
       
       
       
       # Delete a task from the scheduler.
       def delete_task(self, name):
              self.tasks = [task for task in self.tasks if task.name != name]
       
       
       
       # Edit an existing task in the scheduler.
       def edit_task(self, name, new_task):
              for task in self.tasks:
                     if task.name == name:
                            task.name = new_task.name
                            task.type = new_task.type
                            task.start_time = new_task.start_time
                            task.duration = new_task.duration
                            if isinstance(new_task, RecurringTask):
                                   task.start_date = new_task.start_date
                                   task.end_date = new_task.end_date
                                   task.frequency = new_task.frequency
                            elif isinstance(new_task, TransientTask) or isinstance(new_task, AntiTask):
                                   task.date = new_task.date
       
       
       
       # Find a task by name.
       def find_task(self, name):
              for task in self.tasks:
                     if task.name == name:
                            return task
              return None
       
       
       
       # Write the schedule to a JSON file.
       def write_schedule_to_file(self, file_name):
              tasks_data = []
              for task in self.tasks:
                     task_data = {
                            "Name":task.name,
                            "Type":task.type,
                            "StartTime":task.start_time,
                            "Duration":task.duration
                     }
                     
                     if isinstance(task, RecurringTask):
                            task_data["StartDate"] = task.start_date
                            task_data["EndDate"] = task.end_date
                            task_data["Frequency"] = task.frequency
                     elif isinstance(task, TransientTask) or isinstance(task, AntiTask):
                            task_data["Date"] = task.date
                     tasks_data.append(task_data)       
              
              with open(file_name, 'w') as f:
                     json.dump(tasks_data, f, indent = 4)
       
       
       
       # Read the schedule from a JSON file
       def read_schedule_from_file(self, file_name):
              try:
                     with open(file_name, 'r') as f:
                            tasks_data = json.load(f)
                            for task_data in tasks_data:
                                   if "StartDate" in task_data: # RecurringTask
                                          task = RecurringTask(
                                                 task_data["Name"],
                                                 task_data["Type"],
                                                 task_data["StartDate"],
                                                 task_data["StartTime"],
                                                 task_data["Duration"],
                                                 task_data["EndDate"],
                                                 task_data["Frequency"]
                                          )
                                   else: # TransientTask or AntiTask
                                          task = TransientTask(
                                                 task_data["Name"],
                                                 task_data["Type"],
                                                 task_data["Date"],
                                                 task_data["StartTime"],
                                                 task_data["Duration"]
                                          )
                                   if self._check_task_overlap(task):
                                          print(f"Adding task '{task.name}' has failed: Task overlaps with existing tasks.")
                                   else:
                                          self.add_tasks(task)
                                          print(f"Adding task '{task.name}' has succeeded.")
              except FileNotFoundError:
                     print("File not found.")
              except json.JSONDecodeError:
                     print("Invalid JSON format in file.")
       
       
       
       # View the schedule for a specific day.
       def view_schedule_for_day(self, date):
              start_datetime = datetime.strptime(str(date), "%Y%m%d")
              end_datetime = start_datetime + timedelta(days=1)
              daily_tasks = [task for task in self.tasks if isinstance(task, TransientTask) and task.date == date]
              for task in self.tasks:
                     if isinstance(task, RecurringTask):
                            current_date = datetime.strptime(str(task.start_date), "%Y%m%d")
                            end_date = datetime.strptime(str(task.end_date), "%Y%m%d")
                            while current_date < end_date:
                                   if current_date.strftime("%Y%m%d") == date:
                                          daily_tasks.append(TransientTask(task.name, task.type, date, task.start_time, task.duration))
                                   current_date += timedelta(days=task.frequency)
              daily_tasks.sort(key=lambda x: x.start_time)
              for task in daily_tasks:
                     print(task)
                     
       
                    
       # View the schedule for a specific week. 
       def view_schedule_for_week(self, start_date):
              start_datetime = datetime.strptime(str(start_date), "%Y%m%d")
              end_datetime = start_datetime + timedelta(days=7)
              weekly_tasks = [task for task in self.tasks if isinstance(task, TransientTask) and
                            start_datetime <= datetime.strptime(str(task.date), "%Y%m%d") < end_datetime]
              for task in self.tasks:
                     if isinstance(task, RecurringTask):
                            current_date = datetime.strptime(str(task.start_date), "%Y%m%d")
                            end_date = datetime.strptime(str(task.end_date), "%Y%m%d")
                            while current_date < end_date:
                                   if start_datetime <= current_date < end_datetime:
                                          weekly_tasks.append(TransientTask(task.name, task.type, current_date.strftime("%Y%m%d"),
                                                          task.start_time, task.duration))
                                   current_date += timedelta(days=task.frequency)
              weekly_tasks.sort(key=lambda x: (x.date, x.start_time))
              for task in weekly_tasks:
                     print(task)
                     
                     
                     
       # View the schedule for a specific month.
       def view_schedule_for_month(self, start_date):
              start_datetime = datetime.strptime(str(start_date), "%Y%m%d")
              end_datetime = start_datetime + timedelta(days=30)
              monthly_tasks = [task for task in self.tasks if isinstance(task, TransientTask) and
                            start_datetime <= datetime.strptime(str(task.date), "%Y%m%d") < end_datetime]
              for task in self.tasks:
                     if isinstance(task, RecurringTask):
                            current_date = datetime.strptime(str(task.start_date), "%Y%m%d")
                            end_date = datetime.strptime(str(task.end_date), "%Y%m%d")
                            while current_date < end_date:
                                   if start_datetime <= current_date < end_datetime:
                                          monthly_tasks.append(TransientTask(task.name, task.type, current_date.strftime("%Y%m%d"),task.start_time, task.duration))
                                   current_date += timedelta(days=task.frequency)
              monthly_tasks.sort(key=lambda x: (x.date, x.start_time))
              for task in monthly_tasks:
                     print(task)
                     

       
       # Check if a new task overlaps with existing tasks
       def _check_task_overlap(self, task):
              task_start = task.start_time
              task_end = task.start_time + task.duration
              for existing_task in self.tasks:
                     if existing_task != task and existing_task.name == task.name and existing_task.date == task.date and existing_task.type == task.type:
                            # Check for overlap based on task name and date
                            existing_start = existing_task.start_time
                            existing_end = existing_task.start_time + existing_task.duration
                            if (existing_start <= task_start < existing_end) or (existing_start < task_end <= existing_end) or \
                                   (task_start <= existing_start < task_end) or (task_start < existing_end <= task_end):
                                   return True
              return False
       