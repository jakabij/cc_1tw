choice=input("Please specify a command [list, add, mark, archive]: ")

if choice=="add":
    with open("todo.txt","a") as file:
        toDo=input("Add an item: ")
        file.write("[ ]"+toDo+"\n")
        print("Item added.")

if choice=="list":
    with open("todo.txt","r") as file:
        print("You saved the following to-do items:")
        db=1
        for line in file:
            print("{}. ".format(db),line)
            db+=1

if choice=="mark":
    lists=[]
    with open("todo.txt","r") as file:
        print("You saved the following to-do items:")
        db=1
        for line in file:
            print("{}. ".format(db),line)
            lists.append(line)
            db+=1
        
    with open("todo.txt","w") as file:
        toDelete=int(input("Which one you want to mark as completed: "))
        for i in range(db-1):
            if i==toDelete-1:
                file.write("[X] "+lists[i][3:])
                print(lists[i][3:(len(lists[i])-1)]+" is completed.")
            else:
                file.write("[ ] "+lists[i][3:])
            db+=1
    
if choice=="archive":
    lists=[]
    db=1
    with open("todo.txt","r") as file:
        for line in file:
            lists.append(line)
            db+=1

    with open("todo.txt","w") as file:
        for i in range(db-1):
            if not(lists[i][1]=="X"):
                file.write("[ ] "+lists[i][3:])
    
    print("All completed tasks got deleted.")
