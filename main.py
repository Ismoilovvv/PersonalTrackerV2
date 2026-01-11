from expenses.expense_manager import ExpenseManager
from tasks.task_manager import TaskManager

def menu():
    print('\n------------------------------\n'
          'Menu:\n'
          '1. Add Expense\n'
          '2. View Expenses\n'
          '3. Total Spent\n'
          '4. Add Task\n'
          '5. View Tasks\n'
          '6. View Pending Tasks\n'
          '7. Mark Task as Completed\n'
          '8. Exit')

def main():
    e_manager = ExpenseManager()
    t_manager = TaskManager()

    while True:
        try:
            menu()
            choice = int(input('\nEnter your choice (1-8): '))

            match choice:
                case 1:
                    try:
                        amount = float(input('Enter the amount: '))
                    except ValueError:
                        print('Invalid amount. Try again!')
                        continue

                    category = input('Enter the category: ').lower()
                    note = input('Enter the note: ')
                    e_manager.add_expense(amount, category, note)
                    print('Expenses added successfully!')

                case 2:
                    expenses = e_manager.get_all_expenses()
                    if not expenses:
                        print('No expenses so far!')
                        continue

                    for index, expense in enumerate(expenses, start=1):
                        print(f'{index}. {expense["category"].capitalize()} - {expense["amount"]}¥ - {expense["date"]}\n'
                              f'   Note: {expense["note"]}')

                case 3:
                    print(f'Total Spent: ¥{e_manager.get_total_spent():,.2f}')

                case 4:
                    title = input('Enter the title: ')
                    t_manager.add_task(title)
                    print('Task added successfully!')

                case 5:
                    tasks = t_manager.get_all_tasks()
                    if not tasks:
                        print('No tasks so far!')

                    for index, task in enumerate(tasks, start=1):
                        status = '✅' if task['completed'] else '❌'
                        print(f"{index}. {status} {task['title']}")

                case 6:
                    tasks = t_manager.get_pending_tasks()
                    if not tasks:
                        print('No pending tasks so far!')
                        continue

                    print('Pending Tasks: ')
                    for index, task in enumerate(tasks, start=1):
                        print(f"    {index}. {task['title']}")

                case 7:
                    tasks = t_manager.get_all_tasks()
                    if not tasks:
                        print('No tasks so far!')
                        continue

                    print('\nAll Tasks: ')
                    for index, task in enumerate(tasks, start=1):
                        status = '✅' if task['completed'] else '❌'
                        print(f"{index}. {status} {task['title']}")

                    try:
                        index = int(input('\nEnter the index of the task: ')) - 1
                    except ValueError:
                        print('Invalid index. Try again!')
                        continue

                    if 0 <= index < len(tasks):
                        t_manager.mark_task_completed(index)
                        print('Task is "completed"!')
                    else:
                        print('Invalid index. Try again!')

                case 8:
                    print('The program has been terminated successfully!')
                    break

                case _:
                    print('Invalid choice. Try again (1-8)!')

        except ValueError:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
