FILEPATH = 'files/todos.txt'

def get_todos(filepath=FILEPATH):
    """ Function gets items from the text file."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes items from list in the file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# This will be executed only when functions executed directly
if __name__ == "__main__":
    print("Hello")
    print(get_todos())