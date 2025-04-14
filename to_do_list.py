filename = "tasks.txt"

def load():
    try:
        with open(filename,'r') as file:
            tasks = file.readlines()
            return[line.strip() for line in tasks]
    except FileNotFoundError:
        return []
    
def save(tasks):
    with open(filename,'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add(tasks):
    task = input("Enter a task :")
    tasks.append(task)
    save(tasks)

def view(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    
def delete(tasks):
    
    try:
        view(tasks)
        choice = int(input("Choose the number of the Task: "))
        if(1<= choice <= len(tasks)):
            remove = tasks.pop(choice-1)
            save(tasks)
            print(f"{remove},deleted")
            
        else:
            print("Enter a valid number :")

    except FileNotFoundError:
        print("No tasks Found")
    

def show():
    print("\nTo do List\n")
    print("1.Add a Task")
    print("2.Delete a Task")
    print("3.View a Task")
    print("4.Exit")

tasks = load()
while(True):
    show()
    ch = input("Enter your Choice :")
    if(ch =='1'):
        add(tasks)

    elif(ch =='2'):
        delete(tasks)
    elif(ch == '3'):
        view(tasks)
    elif(ch == '4'):
        print("Good Bye !")
        break
    else:
        print("Enter  a valid number")
