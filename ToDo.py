import json
import os

def load_tasks():
    if os.path.exists("local_storage.json"):
        try:
            with open("local_storage.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Could not decode JSON. Starting with an empty list.")
            return []
    return []

def save_tasks(myTask):
    with open("local_storage.json", "w") as file:
        json.dump(myTask, file)

def doneTask(myTask, done):
    while True:
        if len(myTask) == 0:
            print("\nNo available tasks.")
            break

        print("\nSelect a task finished : ")

        for i, task in enumerate(myTask):
            print(f"{i}: {task}")

        print("\n")

        if done == -1:
            break

        if done < 0 or done >= len(myTask):
            print("\nTask not in the list")
            continue
        
        tasksDone.append(myTask.pop(done))
        if  myTask == None:
            print("\nAll task are done!")
            break

        print("\nTask done!")
        save_tasks(myTask)
        save_tasks(tasksDone)
        return myTask
    
def addTask(myTask):
    newTask = []
    try:
        add = int(input("\nEnter how many task to add : "))

        if add <= 0:
            print("\n0 and negative numbers are not allowed!")
            return myTask
        
        if myTask == None:
            print("\nAdd task : ")
        else:
            newTask = myTask.copy()

        for i in range(add):
            addedTask = input("Enter the tasks to add : ")
            newTask.append(addedTask)
            save_tasks(myTask)
        print("\nTasks added successfully!")
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
    save_tasks(myTask)

    return newTaskList
        
# Main function
print("To-Do List Python")

numOfTask = int(input("\nEnter the number of task : "))

myTask = []
tasksDone = []

myTask = load_tasks() or []
tasksDone = load_tasks() or []

for i in range(numOfTask):
    task = input("Enter task : ")
    myTask.append(task)

while True:
    try:
        print("\nSelect a choice : ")
        print("[1]Show Tasks")
        print("[2]Done Task")
        print("[3]Add Task")
        print("[4]Show Tasks Done")
        print("[5]Remove Task")
        print("[0]Exit")

        yourChoice = int(input("\nEnter choice : "))

        if yourChoice == 1:
            if myTask is not None:
                for i, task in enumerate(myTask):
                    print(f"Task {i}: {task}")
            else:
                print("\nNo available tasks.")
        elif yourChoice == 2:
            done = int(input("Select (-1 to exit): "))
            myTask = doneTask(myTask, done)   
        elif yourChoice == 3:
            myTask = addTask(myTask)
        elif yourChoice == 4:
            for i, task in enumerate(tasksDone):
                print(f"{i}: {task}")

            delete = input("\nDelete all done task? (yes/no): ")

            if delete.lower() == "yes":
                tasksDone = []
                print("\nDeleted successfully!")
            elif delete.lower() == "no":
                continue
        elif yourChoice == 5:
            myTask = removeTask(myTask)
        elif yourChoice == 0:
            print("\nAPP Exiting...")
            save_tasks(myTask)
            save_tasks(tasksDone)
            break
        else:
            print("\nInvalid Choice!")
    except ValueError:
            print("\nError ocured please try again.")

 
