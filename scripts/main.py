while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()


    if 'add' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = item.strip('\n')
            row = (f"{index + 1} - {item}")
            print(row)

    elif 'edit' in user_action:

        number = int(input("Wich word would you like to edit?"))
        number = number - 1

        with open('todos.txt', 'r') as file:
             todos = file.readlines()

        new_todo = input("How should we rename this?")
        todos[number] = new_todo + '\n'


        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(input("Wich word would you like to complete?"))

        with open('todos.txt', 'r') as file:
            file.readlines(todos)
            index = number - 1
            removed_todo = todos[index].strip('\n')
            todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {removed_todo} was removed from the list."

        print(message)

    elif 'exit' in user_action:
       file = open('todos.txt', 'w')
       file.close()
       break







            
        
    
    
   
   
