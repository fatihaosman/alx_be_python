task = input("Enter your task:")
timebound = input("Is it time-bound? (yes/no):")
priority = input("Priority (high/medium/low):")

match (priority, timebound):
    case ("high", "yes"):
        print(f"Reminder: '{task}', is a high priority task that requires immediate attention today!")
    case ("high", "no"):
      print(f"Reminder: '{task}', is a low priority task. Consider completing it when you have free time!")
    case ("medium", "yes"):
        print(f"Reminder: '{task}', is a medium priority task with a time constraint. Plan to complete it soon!")