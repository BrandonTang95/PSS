
# task.py

# Task Class
class Task:
       """Class representing a generic task."""
       
       def __init__(self, name, type_, start_time, duration):
              """
              Initialize a task.

              Args:
                     name (str): The name of the task.
                     type_ (str): The type of the task.
                     start_time (float): The start time of the task (24-hour clock).
                     duration (float): The duration of the task (in hours).
              """
              self.name = name
              self.type = type_
              self.start_time = start_time
              self.duration = duration
              
              # Valid Task Types
              valid_types = ["Class", "Study", "Sleep", "Exercise", "Work", "Meal", "Visit", "Shopping", "Appointment", "Cancellation"]
              
              if self.type not in valid_types:
                     raise ValueError("Invalid task type. Allowed types: {}".format(valid_types))
              
              # Private Method
              self._validate_attributes()
              
       """Check the validity of task attributes during initialization."""
       def _validate_attributes(self):
              if not isinstance(self.name, str):
                     raise ValueError("Name must be a string.")
              if not isinstance(self.start_time, (int, float)) or not (0 <= self.start_time <= 23.75):
                     raise ValueError("Start time must be a number between 0 and 23.75.")
              if not isinstance(self.duration, (int, float)) or not (0.25 <= self.duration <= 23.75):
                     raise ValueError("Duration must be a number between 0.25 and 23.75.")
       
       def __str__(self):
              return f"Name: {self.name}, Type: {self.type}, Start Time: {self.start_time}, Duration: {self.duration}"
       


# RecurringTask Class
class RecurringTask(Task):
       def __init__(self, name, type_, start_date, start_time, duration, end_date, frequency):
              """
              Initialize a recurring task.

              Args:
                     name (str): The name of the task.
                     type_ (str): The type of the task.
                     start_date (int): The start date of the task (YYYYMMDD).
                     start_time (float): The start time of the task (24-hour clock).
                     duration (float): The duration of the task (in hours).
                     end_date (int): The end date of the task (YYYYMMDD).
                     frequency (int): The frequency of the task (1 for daily, 7 for weekly).
              """
              super().__init__(name, type_, start_time, duration)
              self.start_date = start_date
              self.end_date = end_date
              self.frequency = frequency
              


# TransientTask Class
class TransientTask(Task):
       def __init__(self, name, type_, date, start_time, duration):
              """
              Initialize a transient task.

              Args:
                     name (str): The name of the task.
                     type_ (str): The type of the task.
                     date (int): The date of the task (YYYYMMDD).
                     start_time (float): The start time of the task (24-hour clock).
                     duration (float): The duration of the task (in hours).
              """
              super().__init__(name, type_, start_time, duration)
              self.date = date
              


# AntiTask Class
class AntiTask(Task):
       def __init__(self, name, type_, date, start_time, duration):
              """
              Initialize an anti-task.

              Args:
                     name (str): The name of the task.
                     type_ (str): The type of the task.
                     date (int): The date of the task (YYYYMMDD).
                     start_time (float): The start time of the task (24-hour clock).
                     duration (float): The duration of the task (in hours).
              """
              super().__init__(name, type_, start_time, duration)
              self.date = date
              
