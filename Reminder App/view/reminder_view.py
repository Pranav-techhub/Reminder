# view/reminder_view.py

def format_reminder(reminder):
    status = "✔️ Done" if reminder.is_done else "❌ Not Done"
    return f"[{reminder.id}] {reminder.text} - {status}"

def format_all(reminders):
    if not reminders:
        return "No reminders yet."
    return "\n".join([format_reminder(r) for r in reminders])
            