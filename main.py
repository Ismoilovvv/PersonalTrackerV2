from expenses.expense_manager import ExpenseManager
from tasks.task_manager import TaskManager

def menu():
    print('\n------------------------------\n'
          'Menu:\n'
          '1.  Add Expense\n'
          '2.  View Expenses\n'
          '3.  Delete Expense\n'
          '4.  Total Spent\n'
          '5.  Report by Category\n'
          '6.  Add Task\n'
          '7.  View Tasks\n'
          '8.  View Pending Tasks\n'
          '9.  Mark Task as Completed\n'
          '10. Unmark Task\n'
          '11. Delete Task\n'
          '12. Task Summary\n'
          '13. Exit')

def check_is_digit(prompt, error_msg, convert):
    while True:
        try:
            return convert(input(prompt))
        except ValueError:
            print(error_msg)

def record_exists_check(record, msg):
        if not record:
            print(msg)
            return None
        return record

def print_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = '✅' if task['completed'] else '❌'
        print(f"{index}. {status} {task['title']}")

def main():
    e_manager = ExpenseManager()
    t_manager = TaskManager()

    while True:
        try:
            menu()
            choice = int(input('\nEnter your choice (1-13): '))

            match choice:

                #Add an Expense
                case 1:
                    amount = check_is_digit(
                        'Enter the amount: ',
                        'Invalid amount. Try again!\n',
                        convert=float
                    )
                    category = input('Enter the category: ').lower()
                    note = input('Enter the note: ')
                    e_manager.add_expense(amount, category, note)
                    print('Expenses added successfully!')

                #View Expenses
                case 2:
                    expenses = record_exists_check(
                        e_manager.get_all_expenses(),
                        'No expenses so far!')
                    if expenses is None:
                        continue

                    for index, expense in enumerate(expenses, start=1):
                        print(f'{index}. {expense["category"].capitalize()}'
                              f' - '
                              f'{expense["amount"]}¥ - {expense["date"]}\n'
                              f'   Note: {expense["note"]}')

                #Delete an Expense
                case 3:
                    expenses = record_exists_check(
                        e_manager.get_all_expenses(),
                        'No expenses to delete!')
                    if expenses is None:
                        continue

                    print('\nAll Expenses: ')
                    for index, expense in enumerate(expenses, start=1):
                        print(f"{index}. {expense['category']}: ¥{expense['amount']}")

                    index = check_is_digit(
                        '\nEnter the index of the expense: ',
                        'Invalid index. Try again!',
                        convert=int) - 1
                    if 0 <= index < len(expenses):
                        e_manager.delete_expense(index)
                        print("Expense is deleted successfully!")
                    else:
                        print('Invalid index. Try again!')

                #Total Spent
                case 4:
                    print(f'Total Spent: ¥{e_manager.get_total_spent():,.2f}')

                #Expense Report by Category
                case 5:
                    summary = e_manager.get_total_by_category()
                    if not summary:
                        print('No expenses so far!')
                        continue

                    for key, value in summary.items():
                        print(f'{key.capitalize()}: ¥{value}')

                #Add Task
                case 6:
                    title = input('Enter the title: ')
                    t_manager.add_task(title)
                    print('Task added successfully!')

                #View Tasks
                case 7:
                    tasks = record_exists_check(
                        t_manager.get_all_tasks(),
                        'No tasks so far!')
                    if tasks is None:
                        continue

                    print_tasks(tasks)

                #View Pending Tasks
                case 8:
                    tasks = record_exists_check(
                        t_manager.get_pending_tasks(),
                        'No pending tasks so far!')
                    if tasks is None:
                        continue

                    print('Pending Tasks: ')
                    for index, task in enumerate(tasks, start=1):
                        print(f"    {index}. {task['title']}")

                #Mark Task Completed
                case 9:
                    tasks = record_exists_check(
                        t_manager.get_all_tasks(),
                        'No tasks so far!')
                    if tasks is None:
                        continue

                    print('\nAll Tasks: ')
                    print_tasks(tasks)

                    index = check_is_digit(
                        '\nEnter the index of the task: ',
                        'Invalid index. Try again!',
                        convert=int) - 1
                    if index is None:
                        continue

                    if 0 <= index < len(tasks):
                        t_manager.mark_task_completed(index)
                        print('Task is "completed"!')
                    else:
                        print('Invalid index. Try again!')

                #Unmark Task
                case 10:
                    tasks = record_exists_check(
                        t_manager.get_all_tasks(),
                        'No tasks so far!')
                    if tasks is None:
                        continue

                    print('\nAll Tasks: ')
                    print_tasks(tasks)

                    index = check_is_digit(
                        '\nEnter the index of the task: ',
                        'Invalid index. Try again!',
                        convert=int) - 1

                    if 0 <= index < len(tasks):
                        t_manager.unmark_task(index)
                        print('Task is "unmarked"!')
                    else:
                        print('Invalid index. Try again!')

                #Delete Task
                case 11:
                    tasks = record_exists_check(
                        t_manager.get_all_tasks(),
                        'No tasks to delete!')
                    if tasks is None:
                        continue

                    print('\nAll Tasks: ')
                    print_tasks(tasks)

                    index = check_is_digit(
                        '\nEnter the index of the task: ',
                        'Invalid index. Try again!',
                        convert=int) - 1
                    t_manager.delete_task(index)
                    print('Task is deleted successfully!')

                #Task Summary
                case 12:
                    total, completed = t_manager.get_task_summary()
                    if total == 0:
                        print('No tasks so far!')
                        continue
                    print(f'Tasks completed: {completed}/{total}')

                #Exit/Quit
                case 13:
                    print('The program has been terminated successfully!')
                    break

                #Choices other than 1-9
                case _:
                    print('Invalid choice. Try again (1-13)!')

        except ValueError:
            print('Invalid choice. Please try again!')

if __name__ == '__main__':
    main()
