
class Task:
    def __init__(self, name, task_type, start_time, duration):
        self.name = name
        self.task_type = task_type
        self.start_time = start_time
        self.duration = duration

class RecurringTask(Task):
    def __init__(self, name, task_type, start_date, start_time, duration, end_date, frequency):
        super().__init__(name, task_type, start_time, duration)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

class TransientTask(Task):
    def __init__(self, name, task_type, date, start_time, duration):
        super().__init__(name, task_type, start_time, duration)
        self.date = date

class AntiTask(Task):
    def __init__(self, name, task_type, date, start_time, duration):
        super().__init__(name, task_type, start_time, duration)
        self.date = date
