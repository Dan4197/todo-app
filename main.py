#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%d.%m.%Y, %H:%M:%S")
print("It is", now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        todos.append(todo)

        # file = open('files/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        i=0;

        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        # new_todos = []
        #
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = item.title()
            row = f"{index+1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos('files/todos.txt')

            new_todo = input("Enter new item: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Invalid command. Try again")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            number = number - 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos(todos)

            print(f"{todo_to_remove} was completed.")
        except IndexError:
            print("No item with this number. Try again.")
            continue
        except ValueError:
            print("Incorrect or no value given. Try again.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command")

print("Bye!")