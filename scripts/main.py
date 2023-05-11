from nis import match







# todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            
            file = open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'show':
            file = open('/home/domen/Desktop/To-do-app/scripts/todos.txt', 'r')
            todos= file.readlines()
            file.close()
            
            # new_todos = []
            
            # for item in todos:
            #     new_item = item.strip()
            #     new_todos.append(new_item)
                
            new_todos = [item.strip('\n') for item in todos]   # Does same thing as above grayed-out for loop.
            
            for index, i in enumerate(new_todos):
                item = item.strip('\n')
                row = (f"{index + 1} - {i}")
                print(row)
        case "edit":
            number = int(input("Wich word would you like to edit?"))
            number = number - 1
            new_todo = input("How should we rename this?")
            todos[number] = new_todo
        case "complete":
            number = int(input("Wich word would you like to complete?"))
            todos.pop(number - 1)
            
            
                    
              
           
        
    
        
        case 'exit':
            break
        
    
    
   
   
