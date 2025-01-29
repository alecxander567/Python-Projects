import os
import json
from datetime import datetime

# Adding notes function
def addNote(myNote):
    try:
        addedNote = input("Enter the note to add :  ")
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        noteWithDate = f"{addedNote} \n\n- {current_date}"
        myNote.append(noteWithDate)
        
        print("\nNote added successfully!")
        return myNote   
    
    except ValueError:
        print("\nPlease enter a valid number")        
        return myNote


# Function to remove a note
def removeNote(myNote):
    while True:
        try:
            print("\n[1]Remove a note")
            print("[2]Remove all notes")
            print("[0]Exit")
            
            deleteNote = int(input("\nEnter your choice : "))
            
            # If the notes are empty
            if not myNote:
                print("\nNo notes to delete.")
                return myNote
                
            if deleteNote == 1:
                for i, note in enumerate(myNote):
                    print(f"{i}: {note}")
                    print("\n")
                        
                    fromNote = int(input("\nSelect a note to remove : "))
                    
                    # If the note doesn't exist
                    if deleteNote < 0 or deleteNote >= len(myNote):
                        print("\nNote to remove not found!")
                        continue
                        
                    myNote.pop(fromNote)
                    print(f"\nSuccessfully deleted")
                    return myNote
                
            elif deleteNote == 2:
                clarify = input("\nAre you sure you want to delete all notes? (yes/no) : ")
                
                if clarify.lower() == "yes":
                     myNote.clear()
                     print("\nAll notes deleted successfully!")
                     return myNote
                elif clarify.lower() == "no":
                    print("\nNo notes deleted.")
                    return myNote
                else:
                    print("\nInvalid input. Please enter 'yes' or 'no'.")
                    continue
            elif deleteNote == 0:
                    return myNote
            else:
                print("\nInvalid input. Please enter a valid number.")
                continue
        except ValueError:
            print("\nPlease enter a valid number")
            

# Function to save notes      
def save_notes(myNote):
    with open("local_storage.json", "w") as file:
        json.dump({"notes": myNote}, file, indent=4)
        
        
# Function to load notes   
def load_notes():
    try:
        if os.path.exists("local_storage.json"):
            with open("local_storage.json", "r") as file:
                data = json.load(file)
                notes = data.get("notes", [])
                return notes if notes is not None else []
        return []
    except json.JSONDecodeError:
        print("Error: Corrupted JSON file. Starting with an empty note list.")
        return []
    except Exception as e:
        print(f"Error loading notes: {e}")
        return []


# Main Function
print("Notes App Python")

# Your empty list to put your notes.
myNote = []
myNote = load_notes()

while True:
    try:
        print("\n1. Add a note")
        print("2. View all notes")
        print("3. Remove a note")
        print("0. Exit")
            
        print("\nSelect an option : ")
        yourChoice = int(input("\nEnter choice : "))
            
        if yourChoice == 1:
                myNote = addNote(myNote)
        elif yourChoice == 2:
            if not myNote:
                print("\nNo notes available.")
            else:
                for i, note in enumerate(myNote):
                    print(f"\n{i}: {note}")
        elif yourChoice == 3:
            myNote = removeNote(myNote)
        elif yourChoice == 0:
            print("\nApp exiting...")
            save_notes(myNote)
            break
        else:
            print("\nInvalid input. Please enter a valid number.")
    except ValueError:
            print("\nInvalid input!")
            continue
        

        