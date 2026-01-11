from utils.file_handler import load_data, save_data
from expenses.expense import Expense

EXPENSE_FILE = 'expenses/expenses.json'

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