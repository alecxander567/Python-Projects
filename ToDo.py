def doneTask(myTask):
    while True:
        print("\nSelect a task finished : ")

        for i, task in enumerate(myTask):
            print(f"{i}: {task}")

        print("\n")

        done = int(input("Select (-1 to exit): "))

        if done == -1:
            break

        if done < 0 or done >= len(myTask):
            print("\nTask not in the list")
            continue
        
        myTask.pop(done)  

        if len(myTask) == 0:
            print("\nAll task are done!")
            break

        print("\nTask done!")
        return myTask
    
def addTask(myTask):
    try:
        add = int(input("\nEnter how many task to add : "))

        if add <= 0:
            print("\nImaginary numbers are not allowed!")
            return myTask
        
        newTask = myTask.copy()

        for i in range(add):
            addedTask = input("\nEnter the tasks to add : ")
            newTask.append(addedTask)

            print("\nTask added successfully!")
            return newTask

    except ValueError:
        print("\nPlease enter a valid number")
        return myTask
    
def removeTask(myTask):
    for i, task in enumerate(myTask):
        print(f"{i}: {task}")

    removedTask = int(input("\nSelect the task to remove : "))

    if removedTask < 0 or removedTask >= len(myTask):
        print("\nTask to remove not in the list!")
        return myTask
    
    myTask.pop(removedTask)

    newTaskList = myTask.copy()

    print("\nTask removed successfully!")
    return newTaskList
        
print("To-Do List Python")

numOfTask = int(input("\nEnter the number of task : "))

myTask = []

for i in range(numOfTask):
    task = input("Enter task : ")
    myTask.append(task)

while True:
    print("\nSelect a choice : ")
    print("[1]Show Tasks")
    print("[2]Done Task")
    print("[3]Add Task")
    print("[4]Remove Task")
    print("[0]Exit")

    yourChoice = int(input("\nEnter choice : "))

    if yourChoice == 1:
       for task in myTask:
        print(task)
    elif yourChoice == 2:
        myTask = doneTask(myTask)
    elif yourChoice == 3:
        myTask = addTask(myTask)
    elif yourChoice == 4:
        myTask = removeTask(myTask)
    elif yourChoice == 0:
        print("\nAPP Exiting...")
        break
    else:
        print("\nInvalid Choice!")

