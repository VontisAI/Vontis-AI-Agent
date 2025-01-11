import datetime

def perform_task(task):
    if task == 'schedule_meeting':
        # Simulate scheduling a meeting
        meeting_time = datetime.datetime.now() + datetime.timedelta(days=1)
        return f"Meeting scheduled for {meeting_time.strftime('%Y-%m-%d %H:%M:%S')}"
    
    elif task == 'send_email':
        # Simulate sending an email
        return "Email sent to the recipient."
    
    else:
        return "Task not recognized."
