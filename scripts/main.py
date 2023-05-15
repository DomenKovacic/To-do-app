from nis import match







# todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"         
                        
            with open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)
                
            
            with open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'w') as file:
                file.writelines(todos)
            
            
        case 'show':
           
           
            with open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'r') as file:
                todos = file.readlines()
        
                
            new_todos = [item.strip('\n') for item in todos]   
            
            for index, item in enumerate(new_todos):
                item = item.strip('\n')
                row = (f"{index + 1} - {item}")
                print(row)
        case "edit":
            number = int(input("Wich word would you like to edit?"))
            number = number - 1
            
            with open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'r') as file:
                 todos = file.readlines()
            
            new_todo = input("How should we rename this?")
            todos[number] = new_todo + '\n'
            
            
            with open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'w') as file:
                file.writelines(todos)
                
        case "complete":
            number = int(input("Wich word would you like to complete?"))
            
            
            with open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'r') as file:
                file.readlines(todos)
                index = number - 1 
                removed_todo = todos[index].strip('\n')             
                todos.pop(index)
            
            
            with open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'w') as file:
                file.writelines(todos)
                
            
            message = f"Todo {removed_todo} was removed from the list."
            print(message)
        
        
            
                                                            
        case 'exit':
           file = open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'w')
           file.close()
           break
                
            
        
    
    
   
   
