# service/reminder_service.py
from model.reminder_model import Reminder

class ReminderStorage:
    def __init__(self):
        self.reminders = []
        self.counter = 1

    def add(self, text):
        reminder = Reminder(self.counter, text) 
        self.reminders.append(reminder)
        self.counter += 1
        return reminder

    def get_all(self):     
        return self.reminders  
                                                                        
    def mark_done(self, reminder_id):
        for reminder in self.reminders:
            if reminder.id == reminder_id:
                reminder.is_done = True
                return reminder
        return None