from datetime import datetime

class Expense:
    def __init__(self, amount, category, note='', date=None):
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'note': self.note,
            'date': self.date,
        }