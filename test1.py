
from task import TransientTask, RecurringTask, AntiTask
from scheduler import Scheduler

def run_test_scenario_1():
    scheduler = Scheduler()

    # Step 1: Read the file Set1.json
    print("\nScenario 1 - Step 1: Read Set1.json (This should work.)")
    scheduler.read_schedule_from_file("Set1.json")

    # Step 2: Delete the task "Intern Interview"
    print("\nScenario 1 - Step 2: Delete 'Intern Interview' (This should work.)")
    scheduler.delete_task("Intern Interview")

    # Step 3: Add a new transient task "Intern Interview"
    print("\nScenario 1 - Step 3: Add 'Intern Interview' (This should work.)")
    scheduler.add_task(TransientTask("Intern Interview", "Appointment", 20200427, 17, 2.5))

    # Step 4: Add a new transient task "Watch a movie" (Should fail)
    # print("\nScenario 1 - Step 4: Add 'Watch a movie' with invalid type (This should fail. There is not transient task with type 'movie'.)")
    # scheduler.add_task(TransientTask("Watch a movie", "Movie", 20200429, 21.5, 2))

    # Step 5: Add a new transient task "Watch a movie" (Should fail due to conflict)
    # print("\nScenario 1 - Step 5: Add 'Watch a movie' with conflict (This should fail. You should be in class!)")
    # scheduler.add_task(TransientTask("Watch a movie", "Visit", 20200430, 18.5, 2))

    # Step 6: Read the file Set2.json (Should fail due to conflict)
    # print("\nScenario 1 - Step 6: Read Set2.json (expect failure)")
    # scheduler.read_schedule_from_file("Set2.json")

if __name__ == "__main__":
    run_test_scenario_1()
