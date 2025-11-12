task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task, but not time-bound. Plan to do it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task with a time constraint. Plan to complete it soon!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. No immediate time constraint.")
    case "low":
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time!")
