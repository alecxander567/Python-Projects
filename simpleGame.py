import random
import os
import time

# Function to clear the screen for clean display
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    

# Function to play the game
def start_game(your_hp, enemy_hp, quiz):
    while True:
        try:
            print("\nPlease select a character :")
            print("1. Knight 🤺")
            print("2. Wizard 🧙🏼‍♂️")
            print("3. Dragon 🐉")
            
            char = int(input("\nYour character : "))
            
            if char == 1:
                print("\nAdventure is starting...")
                # Load the screen
                time.sleep(2)
                
                while your_hp > 0 and enemy_hp > 0:
                    # Clear the screen shows only the questions
                    clear_screen()
                      
                    # Randomly select a question
                    q = random.choice(quiz)
                    
                    # User answer
                    user_answer = input(q["question"] + "\nAnswer: ").strip()
                
                    if user_answer.lower() == q["answer"].lower():
                        print("\n✅ Correct! You damaged the enemy.")
                        # Damage the enemy
                        enemy_hp -= 50
                        
                        # Shows update on your HP and enemy HP
                        print("\nYou :  🤺")
                        print(f"HP : {your_hp}")
                        
                        print("\nEnemy : 🧙🏼‍♂️")
                        print(f"HP : {enemy_hp}")
                    else:
                        print("\n❌ Wrong! The enemy attacks you.")
                        # Damage you
                        your_hp -= 50
                        
                        # Shows update on your HP and enemy HP                       
                        print("\nYou :  🤺")
                        print(f"HP : {your_hp}")
                        
                        print("\nEnemy : 🧙🏼‍♂️")
                        print(f"HP : {enemy_hp}")
                    
                    # Ask the player if wants to continue playing
                    next_question = input("\nContinue? (y/n) : ")
                        
                    if next_question.lower() == "y":
                        # If yes then clear screen and proceed to next question
                        clear_screen()
                    elif next_question.lower() == "n":
                        print("\nReturning to menu...")
                        break
                    else:
                        # Auto continue if inputted the wrong key
                        clear_screen()
                        
                    # Short delay before returning to menu
                    time.sleep(1)

                    # Game over messages
                    if your_hp <= 0:
                        print("\n💀 You have been defeated! Game Over.")
                    elif enemy_hp <= 0:
                        print("\n🏆 You defeated the enemy! Congratulations!")    
                break
            elif char == 2:
                print("\nAdventure is starting...")
                # Load the screen
                time.sleep(2)
                
                while your_hp > 0 and enemy_hp > 0:
                    # Clear the screen shows only the questions
                    clear_screen()
                      
                    # Picks random questions
                    q = random.choice(quiz)
                    
                    # Player answer
                    user_answer = input(q["question"] + "\nAnswer : ").strip()
                
                    if user_answer.lower() == q["answer"].lower():
                        print("\n✅ Correct! You damaged the enemy.")
                        # Damage the enemy
                        enemy_hp -= 50
                        
                        # shows update of you HP and enemy HP
                        print("\nYou :  🧙🏼‍♂️")
                        print(f"HP : {your_hp}")
                        
                        print("\nEnemy : 🤺")
                        print(f"HP : {enemy_hp}")
                
                    else:
                        print("\n❌ Wrong! The enemy attacks you.")
                        # Damage you 
                        your_hp -= 50
                        
                        # Shows update of your HP and enemy HP
                        print("\nYou :  🧙🏼‍♂️")
                        print(f"HP : {your_hp}")
                        
                        print("\nEnemy : 🤺")
                        print(f"HP : {enemy_hp}")
                        
                    # Ask the player if wants to continue playing    
                    next_question = input("\nContinue? (y/n) : ")
                        
                    if next_question.lower() == "y":
                        # If yes then clear screen and proceed to next question
                        clear_screen()
                    elif next_question.lower() == "n":
                        print("\nReturning to menu...")
                        break
                    else:
                        clear_screen()
                        
                    # Short delay before returning to menu
                    time.sleep(1)

                # Game over messages
                if your_hp <= 0:
                    print("\n💀 You have been defeated! Game Over.")
                elif enemy_hp <= 0:
                    print("\n🏆 You defeated the enemy! Congratulations!")
                    
                break  
            elif char == 3:
                print("\nAdventure is starting...")
                # Load the screen
                time.sleep(2)
                
                while your_hp > 0 and enemy_hp > 0:
                    # Clear the screen shows only the questions
                    clear_screen()
                      
                    # Randomly select a question
                    q = random.choice(quiz)
                    
                    # User answer
                    user_answer = input(q["question"] + "\nAnswer: ").strip()
                
                    if user_answer.lower() == q["answer"].lower():
                        print("\n✅ Correct! You damaged the enemy.")
                        # Damage the enemy
                        enemy_hp -= 50
                        
                        # Shows update on your HP and enemy HP
                        print("\nYou :  🐉")
                        print(f"HP : {your_hp}")
                        
                        print("\nEnemy : 🧙🏼‍♂️")
                        print(f"HP : {enemy_hp}")
                    else:
                        print("\n❌ Wrong! The enemy attacks you.")
                        # Damage you
                        your_hp -= 50
                        
                        # Shows update on your HP and enemy HP                       
                        print("\nYou :  🐉")
                        print(f"HP : {your_hp}")
                        
                        print("\nEnemy : 🧙🏼‍♂️")
                        print(f"HP : {enemy_hp}")
                        
                    # Ask the player if wants to continue playing  
                    next_question = input("\nContinue? (y/n) : ")
                        
                    if next_question.lower() == "y":
                        # If yes then clear screen and proceed to next question
                        clear_screen()
                    elif next_question.lower() == "n":
                        print("\nReturning to menu...")
                        break
                    else:
                        clear_screen()
                        
                    # Short delay before returning to menu
                    time.sleep(1)

                    # Game over messages
                    if your_hp <= 0:
                        print("\n💀 You have been defeated! Game Over.")
                    elif enemy_hp <= 0:
                        print("\n🏆 You defeated the enemy! Congratulations!")    
                break
            else:
                print("\nCharacter not found!")
                continue
                      
        except ValueError:
            print("\nInput invalid!")
            continue


# Main function
print("SIMPLE GAME IN PYTHON")

# Your HP and Enemy HP
your_hp = 100
enemy_hp = 100

# Questions and answers
quiz = [
        {"question": "What is 5 + 3?", "answer": "8"},
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 10 * 2?", "answer": "20"},
        {"question": "Who wrote 'Harry Potter'?", "answer": "J.K. Rowling"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "Which element has the chemical symbol 'O'?", "answer": "Oxygen"},
        {"question": "How many legs does a spider have?", "answer": "8"},
        {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
        {"question": "What is the square root of 64?", "answer": "8"},
        {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
        {"question": "What is the chemical symbol for gold?", "answer": "Au"},
        {"question": "What is the capital of Japan?", "answer": "Tokyo"},
        {"question": "What is 12 x 12?", "answer": "144"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"},
        {"question": "How many continents are there on Earth?", "answer": "7"},
        {"question": "What is the speed of light in vacuum? (in km/s)", "answer": "299792"},
        {"question": "Who discovered gravity?", "answer": "Isaac Newton"},
        {"question": "What is the longest river in the world?", "answer": "Nile"},
        {"question": "Which is the smallest country in the world?", "answer": "Vatican City"},
    ]

while True:
    try:
        print("\nSelect an option : ")
        print("1. Start Game")
        print("0. Exit")
    
        choice = int(input("\nEnter your choice : "))
        
        if choice == 1:
            hp = start_game(your_hp, enemy_hp, quiz)
        elif choice == 0:
            print("\nGame exiting...")
            break
    except ValueError:
       print("\nChoice invalid!")
       continue
