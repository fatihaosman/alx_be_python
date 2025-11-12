task = input("Enter your task: ")
timebound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task. Plan to complete it soon!")
    case "low":
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time!")
