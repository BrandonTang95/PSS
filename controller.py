
# controller.py

from scheduler import Scheduler

# Controller Class
class Controller:
       
       """Initialize the controller."""
       def __init__(self, scheduler):
              self.scheduler = scheduler  
       
       """Create a new task."""       
       def create_task(self, task):
              existing_task = self.scheduler.find_task(task.name)
              if existing_task:
                     print("Task with the same name already exists")
                     return 
              
              if self._check_task_overlap(task):
                     print("Tasks overlaps with existing tasks.")
                     return
              
              self.scheduler.add_task(task)
              
       """Delete a task."""
       def delete_task(self, name):
              if not self.scheduler.find_task(name):
                     print("Task not found.")
                     return
              
              self.scheduler.delete_task(name)
              
       """Edit a task."""
       def edit_task(self, name, new_task):
              existing_task = self.scheduler.find_task(name)
              if not existing_task:
                     print("Task not found.")
                     return
              if self._check_task_overlap(new_task):
                     print("Edited task overlaps with existing tasks.")
                     return
              
              self.scheduler.edit_task(name, new_task)
       
       """Find a task by name."""
       def find_task(self, name):
              task = self.scheduler.find_task(name)
              if task:
                     print(task)
              else:
                     print("Task not found.")
       
       """Write schedule to JSON file."""
       def write_schedule_to_file(self, file_name):
              self.scheduler.write_schedule_to_file(file_name)
       
       """Read schedule from JSON file."""
       def read_schedule_from_file(self, file_name):
              self.scheduler.read_schedule_from_file(file_name)
       
       """View schedule for a specific day."""
       def view_schedule_for_day(self, date):
              self.scheduler.view_schedule_for_day(date)

       """View schedule for a specific week."""
       def view_schedule_for_week(self, start_date):
              self.scheduler.view_schedule_for_week(start_date)

       """View schedule for a specific month."""
       def view_schedule_for_month(self, start_date):
              self.scheduler.view_schedule_for_month(start_date)
       
       """Search for a task by type."""
       def search_task_by_type(self, task_type):
              tasks = [task for task in self.scheduler.tasks if task.type == task_type]
              if tasks:
                     for task in tasks:
                            print(task)
              else:
                     print("No tasks found with the given type.")
       
       
       """Sort tasks by name."""
       def sort_tasks(self, sort_by='name'):
              if sort_by == 'name':
                     sorted_tasks = sorted(self.scheduler.tasks, key=lambda x: x.name)
              elif sort_by == 'type':
                     sorted_tasks = sorted(self.scheduler.tasks, key=lambda x: x.type)
              elif sort_by == 'start_time':
                     sorted_tasks = sorted(self.scheduler.tasks, key=lambda x: x.start_time)
              else:
                     print("Invalid sorting option.")
                     return
              for task in sorted_tasks:
                     print(task)
       
       """Check if a new tasks overlaps with existing tasks.""" 
       def _check_task_overlap(self, task):
              return self.scheduler._check_task_overlap(task)