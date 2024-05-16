import calendar

print("-----CALENDAR AND REMINDER-----")

def print_month_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    print(f"=== {month_name} {year} ===")
    print(" Mo Tu We Th Fr Sa Su")
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f"{day:2} "
        print(week_str)

def set_reminder(year, month, day, reminder):
    reminder_date = f"{year}-{month:02d}-{day:02d}"
    with open("reminders.txt", "a") as file:
        file.write(f"{reminder_date}: {reminder}\n")
    print(f"Reminder set for {reminder_date}: {reminder}")

def view_reminders():
    try:
        with open("reminders.txt", "r") as file:
            reminders = file.readlines()
            if not reminders:
                print("No reminders set.")
            else:
                print("Reminders:")
                for reminder in reminders:
                    print(reminder.strip())
    except FileNotFoundError:
        print("No reminders set.")

def main():
    while True:
        print("\n1. View Monthly Calendar")
        print("2. Set Reminder")
        print("3. View Reminders")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))
            print_month_calendar(year, month)
        elif choice == "2":
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))
            day = int(input("Enter day: "))
            reminder = input("Enter reminder: ")
            set_reminder(year, month, day, reminder)
        elif choice == "3":
            view_reminders()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

main()  
