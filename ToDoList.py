tasks = []

def addTask():
    task = input("What task would you like to add?: \n")
    tasks.append(task)
    print (f"Task {task} added to the list")

def listTasks():
    if not tasks:
        print ("There are no tasks currently.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
def deleteTask():
    try:
        tasktToDelete = int(input("# of task to delete: "))
        if tasktToDelete >= 0 and tasktToDelete < len(tasks):
            tasks.pop(tasktToDelete)
            print(f"Task #{tasktToDelete} has been removed")
        else:
            print(f"Task #{tasktToDelete} was not found.")
    except:
        print("Invalid input")

if __name__ == "__main__":
    #app loop
    print("To do list")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("---------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")
        choice = int(choice)
        
        match choice:
            case 1:
                addTask()
            case 2:
                deleteTask()
            case 3:
                listTasks()
            case 4:
                break
            case _:
                print("Invalid input, try again")