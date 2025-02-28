import os 
import time
import random


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    

def your_motivation_for_today(based_survey, motivation):
    print("Quiz will begin now...")
    time.sleep(1)
    clear_screen()
    
    quiz_list = based_survey.copy()
    
    while quiz_list:
        quiz = random.choice(quiz_list) 
    
        answer = input(quiz["question"] + "\nAnswer : ").strip()
    
        if answer.lower() == quiz["answer"].lower():
            motivation += 20
        else:
            motivation -= 20
                    
        quiz_list.remove(quiz) 
        
        clear_screen()
        time.sleep(1)
    
    return motivation


def learning(learning_survey, motivation):
    print("Please wait for a minute...")
    time.sleep(1)
    clear_screen()
    
    quiz_list = learning_survey.copy()
    
    while quiz_list:
        quiz = random.choice(quiz_list)
        
        answer = input(quiz["question"] + "\nAnswer : ").strip()
        
        if answer.lower() == quiz["answer"].lower():
            motivation += 20
        else:
            motivation -= 20
            
        quiz_list.remove(quiz)
        
        clear_screen()
        time.sleep(1)
        
    return motivation
        
        
# Main Function
print("Motivation Quiz")

based_survey = [
        {"question": "Do you want to code today?", "answer": "Yes"},
        {"question": "Are you afraid of AI?", "answer": "No"},
        {"question": "What makes you motivated?", "answer": "To become successful"},
        {"question": "Do you think AI will replace you?", "answer": "No"}
    ]

learning_survey = [
        {"question": "Are you still locked in?", "answer": "Yes"},
        {"question": "Are you not relying on someone but yourself?", "answer": "Yes"},
        {"question": "Is your learning effective?", "answer": "Yes"},
        {"question": "Do you absorb everything that you are learning?", "answer": "Yes"}
    ]

motivation = 0 

while True:
    try:   
        print("\n[1]Test your motivation")
        print("[2]Check your learning motivation")
        print("[0] Leave")
        
        your_choice = int(input("\nEnter your choice : "))
        
        if your_choice == 1:
            motivation = your_motivation_for_today(based_survey, motivation)
            print(f"Your motivation for today : {motivation}") 
            
            if motivation >= 50:
                print("Keep grinding gang👌")
            else:
                print("Job market is cooked buddy, better learn how to cook burgers now...🧑")
        elif your_choice == 2:
            motivation = learning(learning_survey, motivation)
            print(f"Your motivation for today : {motivation}")
            
            if motivation >= 50:
                print("Chill you're doing the right thing bro...👌")
            else:
                print("Just focus buddy you know where to focus🧑")
        elif your_choice == 0:
            print("\nProgram Exiting...")
            break
        else:
            print("\nPlease pick from the choices only.")
        
    except ValueError:
        print("\nInvalid input")
        continue
