class ReminderController:
    def __init__(self, storage):
       self.storage = storage
    
    def add_reminder(self, text):
       return self.storage.add(text)
    
    def get_reminders(self):
       return self.storage.get_all()

    def mark_done(self, reminder_id):
       return self.storage.mark_done(reminder_id)