from utils.file_handler import load_data, save_data
from expenses.expense import Expense

EXPENSE_FILE = 'data/expenses.json'

class ExpenseManager:
    def add_expense(self, amount, category, note=''):
        expense = Expense(amount, category, note)
        expenses = load_data(EXPENSE_FILE)
        expenses.append(expense.to_dict())
        save_data(EXPENSE_FILE, expenses)

    def get_all_expenses(self):
        return load_data(EXPENSE_FILE)

    def get_total_spent(self):
        expenses = load_data(EXPENSE_FILE)
        return sum(expense['amount'] for expense in expenses)

    def get_total_by_category(self):
        expenses = load_data(EXPENSE_FILE)
        summary = {}

        for expense in expenses:
            category = expense['category']
            summary[category] = summary.get(category, 0) + expense['amount']

        return summary