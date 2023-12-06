def add_todo(todo, file_path):
    with open(file_path, 'a') as file:
        file.writelines(todo + "\n")

def show_todos(file_path):
    with open(file_path, 'r') as file:
        todos = file.readlines()

    new_todos = [item.strip('\n') for item in todos]

    formatted_todos = []
    for index, item in enumerate(new_todos):
        row = f"{index + 1} - {item}"
        formatted_todos.append(row)

    return print('\n'.join(formatted_todos))

def edit_todo(number, new_todo, file_path):
    with open(file_path, 'r') as file:
        todos = file.readlines()
    todos[number] = new_todo + '\n'

    with open(file_path, 'w') as file:
        file.writelines(todos)

def delete_todo(number, file_path):
    with open(file_path, 'r') as file:
        todos = file.readlines()
        todos.pop(number)

    with open(file_path, "w") as file:
        file.writelines(todos)





    



