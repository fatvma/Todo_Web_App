FILEPATH = r"C:\courses\python mega course, 20 apps\web app\todos.txt"


def get_todos(filepath=FILEPATH):
    """read a text file
    returns the items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos, filepath=FILEPATH):
    """write the to-do items in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)
