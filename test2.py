
from task import TransientTask, RecurringTask, AntiTask
from scheduler import Scheduler

def run_test_scenario_2():
    scheduler = Scheduler()

    # Step 1: Read the file Set2.json
    print("\nScenario 2 - Step 1: Read Set2.json")
    scheduler.read_schedule_from_file("Set2.json")

    # # Step 2: Add an anti-task "Skip-out" (Should fail)
    # print("\nScenario 2 - Step 2: Add 'Skip-out'")
    # scheduler.create_task(AntiTask("Skip-out", "Cancellation", 20200430, 19.25, 0.75))

    # # Step 3: Add an anti-task "Skip a meal"
    # print("\nScenario 2 - Step 3: Add 'Skip a meal'")
    # scheduler.create_task(AntiTask("Skip a meal", "Cancellation", 20200428, 17, 1))

    # # Step 4: Read the file Set1.json
    # print("\nScenario 2 - Step 4: Read Set1.json")
    # scheduler.read_schedule_from_file("Set1.json")
    
if __name__ == "__main__":
    run_test_scenario_2()