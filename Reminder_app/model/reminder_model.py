# model/reminder_model.py

class Reminder:
    def __init__(self, reminder_id, text):
        self.id = reminder_id
        self.text = text
        self.is_done = False
            