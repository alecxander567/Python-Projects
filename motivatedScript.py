import os 
import time
import random

# Clear screen Function
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Quiz Function
def your_motivation_for_today(based_survey, motivation):
    print("Quiz will begin now...")
    time.sleep(1)
    clear_screen()
    
    quiz_list = based_survey.copy()
    
    while quiz_list:
        quiz = random.choice(quiz_list) # Random picking of questions
    
        answer = input(quiz["question"] + "\nAnswer : ").strip()
    
        if answer.lower() == quiz["answer"].lower():
            motivation += 20
        else:
            motivation -= 20
                    
        quiz_list.remove(quiz) # Removes a question after answering...
        
        # Clear screen before returning to menu
        clear_screen()
        time.sleep(1)
    
    return motivation
    
# Main Function
print("Motivation Quiz")

# Questions and answers
based_survey = [
        {"question": "Do you want to code today?", "answer": "Yes"},
        {"question": "Are you afraid of AI?", "answer": "No"},
        {"question": "What makes you motivated?", "answer": "To become successful"},
        {"question": "Do you think AI will replace you?", "answer": "No"}
    ]

motivation = 0 # Your motivation

while True:
    try:   
        print("\n[1] Take a quiz")
        print("[0] Leave")
        
        your_choice = int(input("\nEnter your choice : "))
        
        if your_choice == 1:
            motivation = your_motivation_for_today(based_survey, motivation)
            print(f"Your motivation for today : {motivation}") # Returns your motivation percent from the quiz
            
            # Checks your status...
            if motivation >= 50:
                print("Keep grinding gang👌")
            else:
                print("Job market is cooked buddy, better learn how to cook burgers now...🧑")
        elif your_choice == 0:
            print("\nProgram Exiting...")
            break
        else:
            print("\nPlease pick from the choices only.")
        
    except ValueError:
        print("\nInvalid input")
        continue