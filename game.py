import tkinter as tk
import random
import os

    
# GUI
root = tk.Tk()
root.title("Simple Obstacle Game")
root.geometry("1000x1000")


# For the shape
canvas_width = 1000
canvas_height = 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
circle = canvas.create_oval(150, 100, 200, 150, fill="red", outline="black")
canvas.pack()


# Obstacles, score, highscore, game speed
obstacles = []
score = 0
score_text = canvas.create_text(50, 20, text="Score: 0", font=("Arial", 16))
game_over_flag = False
highscore = 0
highscore_text = canvas.create_text(900, 20, text=f"Highscore: {highscore}", font=("Arial", 16))
obstacle_speed = 5  
obstacle_interval = 4000


# Obstacles
def create_obs():
    if not game_over_flag:
        y = random.randint(30, canvas_height - 50)
        x = canvas_width
        width = 20
        height = 50
        obstacle = canvas.create_rectangle(x, y, x + width, y + height, fill="blue")
        obstacles.append(obstacle)

        root.after(2000, create_obs)  


# Moving Obstacles
def move_obs():
    global score
    if not game_over_flag:       
        for obstacle in obstacles:
            canvas.move(obstacle, -obstacle_speed, 0)

            x1, y1, x2, y2 = canvas.coords(obstacle)
            if x2 < 0:
                canvas.coords(obstacle, canvas_width, random.randint(50, canvas_height - 50), canvas_width + 20, random.randint(50, canvas_height - 50) + 50)
          
            if check_collision(obstacle):
                game_over()

        root.after(50, move_obs)


# Move up and down
def up_and_down(event):
    if game_over_flag:
        return
    
    x1, y1, x2, y2 = canvas.coords(circle)
    
    if event.keysym == "Up" and y1 > 0:
        canvas.move(circle, 0, -15)
    elif event.keysym == "Down" and y2 < canvas_height:
        canvas.move(circle, 0, 15)
        
        
# Function to update the score
def update_score():
    global score
    
    if not game_over_flag:
        score += 1  
        canvas.itemconfig(score_text, text=f"Score: {score}")
        root.after(1000, update_score) 
    

# Function to check the collision between circle and obstacles
def check_collision(obstacles):
    circle_x1, circle_y1, circle_x2, circle_y2 = canvas.coords(circle)
    obstacle_x1, obstacle_y1, obstacle_x2, obstacle_y2 = canvas.coords(obstacles)

    if (circle_x1 < obstacle_x2 and circle_x2 > obstacle_x1 and
        circle_y1 < obstacle_y2 and circle_y2 > obstacle_y1):
        return True
    
    return False 


# Game over message
def game_over():
    global game_over_flag,  score, highscore
    game_over_flag = True
    
    if score > highscore:
        highscore = score
        save_highscore()
    
    canvas.create_text(canvas_width // 2, canvas_height // 2, text="GAME OVER", font=("Arial", 24), fill="red")
    canvas.create_text(canvas_width // 2, canvas_height // 2 + 40, text=f"Score: {score}", font=("Arial", 16), fill="black")
    canvas.itemconfig(highscore_text, text=f"Highscore: {highscore}")
    
    restart_button.config(state=tk.NORMAL)
    

# Function to restart the game
def restart_game():
    global game_over_flag, score, obstacles

    game_over_flag = False 
    score = 0 
    obstacles = []
    canvas.delete("all")
    save_highscore()
    
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="white")

    global score_text
    score_text = canvas.create_text(50, 20, text=f"Score: {score}", font=("Arial", 16))
    canvas.create_text(900, 20, text=f"Highscore: {highscore}", font=("Arial", 16))
    
    # Recreate the canvas and the circle
    global circle
    circle = canvas.create_oval(150, 100, 200, 150, fill="red", outline="black")

    # Reset the score display
    canvas.itemconfig(score_text, text="Score: 0")

    # Disable the restart button
    restart_button.config(state=tk.DISABLED)

    # Reload highscore
    load_highscore()

    # Start the game
    create_obs()
    move_obs()
    update_score()
    

# Function to clear or delete high score
def clear_highscore():
    global highscore
    if os.path.exists("highscore.txt"):
        os.remove("highscore.txt") 
    highscore = 0
    canvas.itemconfig(highscore_text, text=f"Highscore: {highscore}")
    
    
# Function to save high score
def save_highscore():
    with open("highscore.txt", "w") as file:
        file.write(str(highscore))


# Function to load the saved high score
def load_highscore():
    global highscore
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            highscore = int(file.read())
    canvas.itemconfig(highscore_text, text=f"Highscore: {highscore}")
     

# Function to set medium difficulty
def set_medium_level():
    global obstacle_speed, obstacle_interval
    obstacle_speed = 6
    obstacle_interval = 3000 
  
    restart_game() 


# Function to set hard difficulty
def set_hard_level():
    global obstacle_speed, obstacle_interval
    obstacle_speed = 7
    obstacle_interval = 2000

    restart_game()

# Buttons for restart, medium, hard, and clear high score
restart_button = tk.Button(root, text="Restart", font=("Arial", 14), command=restart_game, state=tk.DISABLED, fg="blue")
restart_button.pack(pady=20)
medium_button = tk.Button(root, text="Medium", font=("Arial", 14), command=set_medium_level, fg="green")
medium_button.pack(pady=20)
hard_button = tk.Button(root, text="Hard", font=("Arial", 14), command=set_hard_level, fg="red")
hard_button.pack(pady=20)
clear_button = tk.Button(root, text="Clear Highscore", font=("Arial", 14), command=clear_highscore)
clear_button.pack(pady=20)


# Functions to run the game
root.bind("<Up>", up_and_down)
root.bind("<Down>", up_and_down)
create_obs()
move_obs()
update_score()
load_highscore()
root.mainloop()


