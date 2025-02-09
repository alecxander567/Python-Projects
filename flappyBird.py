import tkinter as tk
import os
import random


# Gui 
root = tk.Tk()
root.title("Flappy Bird My Own Version")
root.geometry("1000x1000")


# Bird and canvas
canvas_width = 1000
canvas_height = 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
bird = canvas.create_oval(150, 100, 180, 130, fill="red", outline="black")
canvas.pack()


# Game Variables
obstacles = []
obstacle_tasks = [] 
score = 0
high_score = 0
obs_speed = 5
obs_interval = 4000
game_over_flag = False
gravity = 5 
jump_strength = -25
gap_size = 100  
score_text = canvas.create_text(50, 20, text="Score: 0", font=("Arial", 16))
highscore_text = canvas.create_text(900, 20, text=f"Highscore: {high_score}", font=("Arial", 16))


# Create obstacles
def create_obs():
    if not game_over_flag:
        y = random.randint(30, canvas_height - 150)  
        gap = 100  

        top_obstacle = canvas.create_rectangle(canvas_width, 0, canvas_width + 50, y, fill="green")
        bottom_obstacle = canvas.create_rectangle(canvas_width, y + gap, canvas_width + 50, canvas_height, fill="green")

        obstacles.append((top_obstacle, bottom_obstacle))
        
        root.after(2000, create_obs)
        
        
# Move Obstacles
def move_obs():
    if not game_over_flag:
        for top_obs, bottom_obs in obstacles[:]:
            canvas.move(top_obs, -obs_speed, 0)
            canvas.move(bottom_obs, -obs_speed, 0)

            x1, _, x2, _ = canvas.coords(top_obs)
            if x2 < 0:
                canvas.delete(top_obs)
                canvas.delete(bottom_obs)
                obstacles.remove((top_obs, bottom_obs))

        root.after(50, move_obs)
        
        
# Move bird
def up(event):
    if not game_over_flag:
        canvas.move(bird, 0, jump_strength)
        

# Constant falling of the bird
def apply_gravity():
    if not game_over_flag:
        x1, y1, x2, y2 = canvas.coords(bird)
        
        if y2 < canvas_height: 
            canvas.move(bird, 0, gravity)
        
        root.after(50, apply_gravity) 
        
        
# Check collision of obs and bird
def check_collision():
    circle_x1, circle_y1, circle_x2, circle_y2 = canvas.coords(bird)

    if circle_y1 <= 0 or circle_y2 >= canvas_height:
        game_over()  
        return True  

    for top_obs, bottom_obs in obstacles:
        top_x1, top_y1, top_x2, top_y2 = canvas.coords(top_obs)
        bottom_x1, bottom_y1, bottom_x2, bottom_y2 = canvas.coords(bottom_obs)

        if (circle_x1 < top_x2 and circle_x2 > top_x1 and
            circle_y1 < top_y2 and circle_y2 > top_y1):
            game_over()
            return True

        if (circle_x1 < bottom_x2 and circle_x2 > bottom_x1 and
            circle_y1 < bottom_y2 and circle_y2 > bottom_y1):
            game_over()
            return True

    return False


def game_loop():
    global game_over_flag
    if check_collision():
        game_over()
        return  

    root.after(50, game_loop)  

game_loop()


# If game over
def game_over():
    global game_over_flag, score, high_score
    game_over_flag = True

    if score > high_score:
        high_score = score
        save_highscore()

    canvas.create_text(canvas_width // 2, canvas_height // 2, text="GAME OVER", font=("Arial", 24), fill="red")
    canvas.create_text(canvas_width // 2, canvas_height // 2 + 40, text=f"Score: {score}", font=("Arial", 16), fill="black")
    canvas.itemconfig(highscore_text, text=f"Highscore: {high_score}")
    
    restart_button.config(state=tk.NORMAL)
    
    
# Update Score
def update_score():
    global score
    
    if game_over_flag:
        return  
    
    score += 1  
    canvas.itemconfig(score_text, text=f"Score: {score}") 

    root.after(1000, update_score) 

  
# Restart the game
def restart_game(): 
    global game_over_flag, score, obstacles, obstacle_tasks

    game_over_flag = True  
    for task in obstacle_tasks:
        root.after_cancel(task) 
    obstacle_tasks.clear()  

    root.after_cancel(update_score) 

    game_over_flag = False 
    score = 0 
    obstacles = []  
    canvas.delete("all")  
    save_highscore()
    
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="white")

    global score_text
    score_text = canvas.create_text(50, 20, text=f"Score: {score}", font=("Arial", 16))
    canvas.create_text(900, 20, text=f"Highscore: {high_score}", font=("Arial", 16))

    global bird
    bird = canvas.create_oval(150, 100, 180, 130, fill="red", outline="black")

    canvas.itemconfig(score_text, text="Score: 0")

    restart_button.config(state=tk.DISABLED) 

    load_highscore()

    create_obs()  
    move_obs()  
    apply_gravity()  
    update_score()
    game_loop()

    
# Save high score
def save_highscore():
    with open("highscore.txt", "w") as file:
        file.write(str(high_score))
        

# Load high Score
def load_highscore():
    global highscore
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            highscore = int(file.read())
    canvas.itemconfig(highscore_text, text=f"Highscore: {high_score}")
    

# Delete the current high score
def delete_highscore():
    global high_score
    high_score = 0  
    save_highscore()  
    canvas.itemconfig(highscore_text, text=f"Highscore: {high_score}")
    
    
# Buttons
restart_button = tk.Button(root, text="Restart", font=("Arial", 14), command=restart_game, state=tk.DISABLED, fg="blue")
restart_button.pack(pady=20)
delete_button = tk.Button(root, text="Delete Highscore", font=("Arial", 14), command=delete_highscore, fg="red")
delete_button.pack()
     

# Run program
root.bind("<space>", up)
apply_gravity()
create_obs()
check_collision() 
move_obs()
update_score() 
root.mainloop()
