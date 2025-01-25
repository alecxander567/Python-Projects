import json
import os

def doneTask(myTask, tasksDone):
  while True:
        print("\nSelect a task to mark as done:")

        if not myTask:
            print("\nAll tasks are done.")
            return myTask, tasksDone
        else:
            for i, task in enumerate(myTask):
                print(f"{i}: {task}")

        done = int(input("Select (-1 to exit): "))

        if done == -1:
            return myTask, tasksDone 

        if done < 0 or done >= len(myTask):
            print("\nTask not in the list")
            continue

        tasksDone.append(myTask.pop(done))
        if len(myTask) == 0:
            print("\nAll tasks are done!")
            return myTask, tasksDone

        print("\nTask marked as done!")
        save_tasks(myTask, tasksDone)
        return myTask, tasksDone

def addTask(myTask):
    try:
        add = int(input("\nEnter how many task to add : "))

        if add <= 0:
            print("\n0 and negative numbers are not allowed!")
            return myTask
        else:      
            for i in range(add):
                addedTask = input("Enter the tasks to add : ")
                myTask.append(addedTask)
           
        save_tasks(myTask)
        print("\nTasks added successfully!")
        return myTask

    except ValueError:
        print("\nPlease enter a valid number")
    
def removeTask(myTask):
    while True:
        try:
            
            print("\n1. Remove a task")
            print("2. Delete all task")
            print("0. Exit")

            delete = int(input("\nSelect an option : "))

            if delete == 1:
                if not myTask:
                    print("\nNo tasks available to remove.")
                    continue
                
                for i, task in enumerate(myTask):
                 print(f"{i}: {task}")

                fromTask = int(input("\nSelect a task to remove : "))

                if fromTask < 0 or fromTask >= len(myTask):
                    print("\nTask to remove not found!")
                    continue

                myTask.pop(fromTask)

                print(f"\nSuccessfully deleted")                  
            elif delete == 2:
                clarify = input("\nAre you sure to delete all task? (y/n) : ")

                if clarify.lower() == "y":
                    myTask.clear()
                    print("\nSuccessfully deleted!")
                else:
                    print("\nNo tasks deleted.")
            elif delete == 0:
                break

            return myTask
        except ValueError:
            print("\nInvalid input. Please enter from the options")
            continue

def load_tasks():
    try:
        if os.path.exists("local_storage.json"):
            with open("local_storage.json", "r") as file:
                data = json.load(file)
                tasks = data.get("tasks", [])
                completed_tasks = data.get("completed_tasks", [])
                return tasks if tasks is not None else [], completed_tasks if completed_tasks is not None else []
        return [], []
    except json.JSONDecodeError:
        print("Error: Corrupted JSON file. Starting with an empty task list.")
        return [], []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return [], []

def save_tasks(myTask, tasksDone=None):
    try:
        with open("local_storage.json", "w") as file:
            json.dump({"tasks": myTask, "completed_tasks": tasksDone or []}, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Main function
print("To-Do List Python")

myTask, tasksDone = load_tasks() 

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
            if not myTask:
                print("\nNo available tasks.")
            else:
                for i, task in enumerate(myTask):
                    print(f"{i}: {task}")
        elif yourChoice == 2:
            myTask, tasksDone = doneTask(myTask, tasksDone)
        elif yourChoice == 3:
            myTask = addTask(myTask)
        elif yourChoice == 4:
            if not tasksDone:
                print("\nNo tasks completed yet.")
            else:
                for i, task in enumerate(tasksDone):
                    print(f"{i}: {task}")

            delete = input("\nDelete all done tasks? (yes/no): ")

            if delete.lower() == "yes":
                tasksDone.clear()
                print("\nAll completed tasks deleted successfully!")
            elif delete.lower() == "no":
                continue
        elif yourChoice == 5:
            myTask = removeTask(myTask)
            save_tasks(myTask, tasksDone)
        elif yourChoice == 0:
            print("\nAPP Exiting...")
            save_tasks(myTask, tasksDone)
            break
        else:
            print("\nInvalid Choice! Please try again.")
    except ValueError:
            print("\nInvalid input. Please try again.")

 
