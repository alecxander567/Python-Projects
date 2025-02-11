import tkinter as tk
import random

# Variables
width = 500
height = 500
rows = 3
cols = 3
user_choice = None
bot_choice = None
grid_values = [["" for _ in range (cols)] for _ in range(rows)]
cell_width = width // cols
cell_height = height // rows
game_over = False


# Gui
root = tk.Tk()
root.title("Tic Tac Toe Python")
root.geometry("1920x1080")


# Canvas Board
canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()
button_frame = tk.Frame(root)
button_frame.pack(pady=0)
choice_frame = tk.Frame(root)
choice_frame.pack(pady=0)


# Buttons to choose
label = tk.Label(root, text="Choose X or O", font=("Arial", 14))
label.pack(pady=10)
btn_x = tk.Button(button_frame, text="X", font=("Arial", 14), width=5, fg="red", command=lambda: choose("X"))
btn_x.pack(side="left", padx=10)  # Keep X and O next to each other
btn_o = tk.Button(button_frame,text="O", font=("Arial", 14), width=5, fg="green", command=lambda: choose("O"))
btn_o.pack(side="left",padx=10)

    
# Create grids
def create_grid(canvas, width, height, rows, cols):
    canvas.delete("all")
    cell_width = width // cols
    cell_height = height // rows

    for i in range(rows):
        for j in range(cols):
            x1 = j * cell_width
            y1 = i * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")
            

# Click for X and O
def on_click(self, event):
    col = event.x // self.cell_width
    row = event.y // self.cell_height
    x1 = col * self.cell_width
    y1 = row * self.cell_height
    x2 = x1 + self.cell_width
    y2 = y1 + self.cell_height

    if not self.canvas.find_withtag(f"{row}-{col}"):
        self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=self.current_player, font=("Arial", 24), tags=f"{row}-{col}")
        self.current_player = "O" if self.current_player == "X" else "X"


# Function for user choice
def choose(option):
    global user_choice, bot_choice
    user_choice = option
    bot_choice = "O" if user_choice == "X" else "X"  
    label.config(text=f"You selected: {user_choice} | Bot is {bot_choice}")
    

# PLayer Move
def on_click(event):
    global user_choice, game_over

    if user_choice is None or game_over:
        return  

    col = event.x // cell_width
    row = event.y // cell_height

    if grid_values[row][col] == "":
        x_center = col * cell_width + cell_width // 2
        y_center = row * cell_height + cell_height // 2
        canvas.create_text(x_center, y_center, text=user_choice, font=("Arial", 36), tags=f"{row}-{col}")
        grid_values[row][col] = user_choice 
        
        check_winner() 

        if not game_over: 
            root.after(500, bot_move) 


# Bot move 
def bot_move():
    global bot_choice, game_over

    if game_over:
        return 

    empty_cells = [(i, j) for i in range(rows) for j in range(cols) if grid_values[i][j] == ""]

    if empty_cells:
        row, col = random.choice(empty_cells)  # Pick a random empty cell
        x_center = col * cell_width + cell_width // 2
        y_center = row * cell_height + cell_height // 2
        canvas.create_text(x_center, y_center, text=bot_choice, font=("Arial", 36), tags=f"{row}-{col}")
        grid_values[row][col] = bot_choice  # Mark cell as filled

        check_winner()  


# Function to check for a winner
def check_winner():
    global game_over
    for i in range(rows):
        # Check rows & columns
        if grid_values[i][0] == grid_values[i][1] == grid_values[i][2] and grid_values[i][0] != "":
            label.config(text=f"{grid_values[i][0]} Wins!")
            game_over = True
            return
        if grid_values[0][i] == grid_values[1][i] == grid_values[2][i] and grid_values[0][i] != "":
            label.config(text=f"{grid_values[0][i]} Wins!")
            game_over = True
            return
          
    # Check diagonals
    if grid_values[0][0] == grid_values[1][1] == grid_values[2][2] and grid_values[0][0] != "":
        label.config(text=f"{grid_values[0][0]} Wins!")
        game_over = True
        return
    if grid_values[0][2] == grid_values[1][1] == grid_values[2][0] and grid_values[0][2] != "":
        label.config(text=f"{grid_values[0][2]} Wins!")
        game_over = True
        return
        
    # Check for a tie
    if all(grid_values[i][j] != "" for i in range(rows) for j in range(cols)):
        label.config(text="It's a Tie!")
        game_over = True
 
 
 # Restart the game
def restart_game():
    global grid_values, game_over, user_choice, bot_choice
    grid_values = [["" for _ in range(cols)] for _ in range(rows)]
    game_over = False
    user_choice = None
    bot_choice = None
    label.config(text="Choose X or O") 
    create_grid(canvas,width, height, rows, cols) 


# Restart Button (With Confirmation)
btn_restart = tk.Button(root, text="Restart Game", font=("Arial", 14), width=12, command=restart_game)
btn_restart.pack(pady=0)
       

# Bind the canvas click event
canvas.bind("<Button-1>", on_click) 
create_grid(canvas, width, height, rows, cols)

root.mainloop()