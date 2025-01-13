import tkinter as tk

def submit_input():
    user_input = entry.get().lower()

    if user_input.strip() == "": 
        return
    
    response = get_bot_response(user_input) 
    display_conversation(user_input, response)
    entry.delete(0, tk.END)

def get_bot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!",
        "what is your name": "I am your friendly chatbot."
    }
    
    return responses.get(user_input, "Sorry, I didn't understand that.")

def display_conversation(user_input, response):
    label_user = tk.Label(root, text=f"You: {user_input}", font=("Arial", 12), anchor="w", justify="left", fg="blue")
    label_user.pack(fill="x", padx=10, pady=5)

    label_bot = tk.Label(root, text=f"Bot: {response}", font=("Arial", 12), anchor="e", justify="right", fg="black")
    label_bot.pack(fill="x", padx=10, pady=5)

root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("700x600")

label_prompt = tk.Label(root, text="Ask me something:", font=("Arial", 14))
label_prompt.pack(pady=10)

frame = tk.Frame(root)
frame.pack(side="bottom", pady=10)

entry = tk.Entry(frame, font=("Arial", 14))
entry.pack(side="left", padx=10) 

button = tk.Button(frame, text="Submit", command=submit_input)
button.pack(side="left", padx=10) 

root.mainloop()
