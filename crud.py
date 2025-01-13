import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector # type: ignore

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        
        password="",        
        database="python_db" 
    )

def add_record():
    username = username_var.get()
    password = password_var.get()
    email = email_var.get()

    if not username or not password or not email:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO mytable (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        connection.commit()
        messagebox.showinfo("Success", "Record added successfully!")
        clear_fields()
        populate_table()
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Email must be unique!")
    finally:
        connection.close()

def populate_table():
    for row in table.get_children():
        table.delete(row)

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mytable")
    rows = cursor.fetchall()
    for row in rows:
        table.insert("", "end", values=row)
    connection.close()

def update_record():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No record selected!")
        return

    id = table.item(selected_item)["values"][0]
    username = username_var.get()
    password = password_var.get()
    email = email_var.get()

    if not username or not password or not email:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE mytable SET username = %s, password = %s, email = %s WHERE id = %s", (username, password, email, id))
        connection.commit()
        if cursor.rowcount == 0:
            messagebox.showerror("Error", "Record not found!")
        else:
            messagebox.showinfo("Success", "Record updated successfully!")
        clear_fields()
        populate_table()
    finally:
        connection.close()

def delete_record():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No record selected!")
        return

    id = table.item(selected_item)["values"][0]
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM mytable WHERE id = %s", (id,))
    connection.commit()
    if cursor.rowcount == 0:
        messagebox.showerror("Error", "Record not found!")
    else:
        messagebox.showinfo("Success", "Record deleted successfully!")
    connection.close()
    populate_table()

def clear_fields():
    username_var.set("")
    password_var.set("")
    email_var.set("")

root = tk.Tk()
root.title("CRUD Python App")
root.geometry("1080x620")
root.configure(bg="lightblue")

style = ttk.Style()

style.configure("TButton",
                background="blue", 
                foreground="black",
                font=("Arial", 20), 
                )
style.map("TButton", background=[('active', 'darkblue')])

style.configure("TLabel", font=("Arial", 12), padding=5)

style.configure("Custom.Treeview", 
                font=("Arial", 10), 
                background="#eaeaea", 
                foreground="black")
style.map("Custom.Treeview", background=[('selected', '#d5e8d4')])

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

username_var = tk.StringVar()
password_var = tk.StringVar()
email_var = tk.StringVar()

entry = tk.Label(frame, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry = tk.Entry(frame, textvariable=username_var, width=95).grid(row=0, column=1, padx=50, pady=10)

entry = tk.Label(frame, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry = tk.Entry(frame, textvariable=password_var, show="*", width=95).grid(row=1, column=1, padx=10, pady=10)

entry = tk.Label(frame, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry = tk.Entry(frame, textvariable=email_var, width=95).grid(row=2, column=1, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Add", command=add_record, style="TButton").grid(row=0, column=0, padx=15, pady=10)
ttk.Button(button_frame, text="Update", command=update_record, style="TButton").grid(row=0, column=1, padx=15, pady=10)
ttk.Button(button_frame, text="Delete", command=delete_record, style="TButton").grid(row=0, column=2, padx=15, pady=10)
ttk.Button(button_frame, text="Clear", command=clear_fields, style="TButton").grid(row=0, column=3, padx=15, pady=10)

table_frame = tk.Frame(root, bg="#f0f0f0")
table_frame.pack(pady=10)

columns = ("ID", "Username", "Password", "Email")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10, style="Custom.Treeview")
table.pack(fill="both", expand=True)

for col in columns:
    table.heading(col, text=col, anchor="center")
    table.column(col, anchor="center")

populate_table()

root.mainloop()
