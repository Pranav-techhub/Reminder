from service.reminder_service import ReminderStorage
from controller.reminder_controller import ReminderController
from view.reminder_view import format_all

def main():
    storage = ReminderStorage()
    controller = ReminderController(storage)

    while True:
        print("\n ReminderApp Menu")
        print("1. Set Reminder")
        print("2. Mark Reminder as Done")
        print("3. Display All Reminders")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            text = input("Enter reminder text: ")
            reminder = controller.add_reminder(text)
            print(f"Reminder added with ID {reminder.id}")

        elif choice == "2":
            try:
                reminder_id = int(input("Enter reminder ID to mark as done: "))
                updated = controller.mark_done(reminder_id)
                if updated:
                    print("Reminder marked as done.")
                else:
                    print("Reminder ID not found.")
            except ValueError:
                print("Please enter a valid number.")
          
        elif choice == "3":
            print("\n📝 Your Reminders:")
            print(format_all(controller.get_reminders()))

        elif choice == "4":
            print("Exiting ReminderApp. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
