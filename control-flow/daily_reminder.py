
# Step 1: Get user input
task = input("What is your task for today? ")
priority = input("Set the task priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Step 2: Match Case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}'is a high priority task that requires immediate attention today!"
    case "medium":
        reminder = f"🟠 Important Task: {task} [Priority: MEDIUM]"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"⚠️ Unknown priority level for: {task}"

# Step 3: Time sensitivity check
if time_bound == "yes":
    reminder += " — This task requires immediate attention today!"

# Step 4: Print final message
print("\n📝 Reminder:")
print(reminder)
