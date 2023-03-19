from nis import match







todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, i in enumerate(todos):
                
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
        
    
    
   
   
