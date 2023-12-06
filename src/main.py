from utils import add_todo, show_todos, edit_todo, delete_todo

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")

    if user_action.startswith('add'):
        todo = user_action[4:]  # Extract the todo text
        add_todo(todo, 'todos.txt')

    elif user_action.startswith('show'):
        show_todos('todos.txt')

    elif user_action.startswith('edit'):
        number = int(user_action.split()[1])
        new_todo = input("How should we rename this? ")
        edit_todo(number, new_todo, 'todos.txt')

    elif user_action.startswith("delete"):
        number = int(user_action.split()[1])
        delete_todo(number, file_path="todos.txt")

    elif user_action == 'exit':
        pass

    else:
        print("Command is not valid")
