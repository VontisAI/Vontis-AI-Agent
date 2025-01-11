import time
import threading
import datetime

# Function to simulate a time-based task (e.g., sending a reminder)
def time_based_task(task_name, execute_time):
    # Get the current time
    current_time = datetime.datetime.now()
    
    # Calculate the time remaining until the task should execute
    time_diff = execute_time - current_time
    if time_diff.total_seconds() > 0:
        # Sleep until the task time
        time.sleep(time_diff.total_seconds())
    
    # Execute the task
    print(f"Executing task: {task_name} at {datetime.datetime.now()}")

# Example usage: Schedule a task to execute in 5 seconds
execute_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
task_thread = threading.Thread(target=time_based_task, args=("Send Reminder", execute_time))
task_thread.start()
