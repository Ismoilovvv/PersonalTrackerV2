from expenses.expense_manager import ExpenseManager
from tasks.task_manager import TaskManager

###Tasks to do tomorrow (13.01.2025)

#Convert repeating try-else statements into functions
#if not statements into functions
#Tuckle the issue with the tasks.json
#Add functions: 3. unmark a task
#

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
          '10. Delete Task\n'
          '11. Task Summary\n'
          '11. Exit')

def main():
    e_manager = ExpenseManager()
    t_manager = TaskManager()

    while True:
        try:
            menu()
            choice = int(input('\nEnter your choice (1-8): '))

            match choice:

                #Add an Expense
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

                #View Expenses
                case 2:
                    expenses = e_manager.get_all_expenses()
                    if not expenses:
                        print('No expenses so far!')
                        continue

                    for index, expense in enumerate(expenses, start=1):
                        print(f'{index}. {expense["category"].capitalize()}'
                              f' - '
                              f'{expense["amount"]}¥ - {expense["date"]}\n'
                              f'   Note: {expense["note"]}')

                #Delete an Expense
                case 3:
                    expenses = e_manager.get_all_expenses()
                    if not expenses:
                        print('No expenses to delete!')
                        continue

                    print('\nAll Expenses: ')
                    for index, expense in enumerate(expenses, start=1):
                        print(f"{index}. {expense['category']}: ¥{expense['amount']}")

                    try:
                        index = int(input('\nEnter the index of the expense: ')) - 1
                        e_manager.delet_expense(index)
                        print('Expenses deleted successfully!')
                    except ValueError:
                        print('Invalid index. Try again!')
                        continue

                #Total Spent
                case 4:
                    print(f'Total Spent: ¥{e_manager.get_total_spent():,.2f}')

                #Expense Report by Category
                case 5:
                    summary = e_manager.get_total_by_category()
                    for key, value in summary.items():
                        print(f'{key.capitalize()}: ¥{value}')

                #Add Task
                case 6:
                    title = input('Enter the title: ')
                    t_manager.add_task(title)
                    print('Task added successfully!')

                #View Tasks
                case 7:
                    tasks = t_manager.get_all_tasks()
                    if not tasks:
                        print('No tasks so far!')

                    for index, task in enumerate(tasks, start=1):
                        status = '✅' if task['completed'] else '❌'
                        print(f"{index}. {status} {task['title']}")

                #View Pending Tasks
                case 8:
                    tasks = t_manager.get_pending_tasks()
                    if not tasks:
                        print('No pending tasks so far!')
                        continue

                    print('Pending Tasks: ')
                    for index, task in enumerate(tasks, start=1):
                        print(f"    {index}. {task['title']}")

                #Mark Task Completed
                case 9:
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

                #Delete Task
                case 10:
                    tasks = t_manager.get_all_tasks()
                    if not tasks:
                        print('No tasks to delete!')
                        continue

                    print('\nAll Tasks: ')
                    for index, task in enumerate(tasks, start=1):
                        status = '✅' if task['completed'] else '❌'
                        print(f'{index}. {status} {task['title']}')

                    try:
                        index = int(input('\nEnter the index of the task: ')) - 1
                        t_manager.delete_task(index)
                        print('Task deleted successfully!')
                    except ValueError:
                        print('Invalid index. Try again!')
                        continue

                #Task Summary
                case 11:
                    total, completed = t_manager.get_task_summary()
                    print(f'Tasks completed: {completed}/{total}')

                #Exit/Quit
                case 12:
                    print('The program has been terminated successfully!')
                    break

                #Choices other than 1-9
                case _:
                    print('Invalid choice. Try again (1-8)!')

        except ValueError:
            print('Invalid choice. Please try again!')

if __name__ == '__main__':
    main()
