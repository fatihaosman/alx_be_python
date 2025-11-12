task = input("What is your main task for today? ")
priority = input("What is the priority level? (high/medium/low) ")
timebound = input("Is there a time constraint? (yes/no) ")

match (priority, timebound):
    case ("high", "yes"):
        print(f"Reminder: '{task}', is a high priority task that requires immediate attention today!")
    case ("high", "no"):
      print(f"Reminder: '{task}', is a low priority task. Consider completing it when you have free time!")
    case ("medium", "yes"):
        print(f"Reminder: '{task}', is a medium priority task with a time constraint. Plan to complete it soon!")