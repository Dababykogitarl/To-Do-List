import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

def add_task():
    # Get the task description from the entry field
    task = entry.get()
    if task:
        # Add the task to the tasks list with a "done" status of False
        tasks.append({"task": "• " + task, "done": False})
        # Clear the entry field
        entry.delete(0, tk.END)
        # Save tasks to the file and update the task display
        save_tasks()
        update_task_display()
    else:
        # Show a warning if the entry field is empty
        messagebox.showwarning("Warning!", "Please enter a task.")

def delete_task():
    # Get the index of the selected task
    selected_task = listbox.curselection()
    # Remove the selected task from the tasks list
    if selected_task:
        tasks.pop(selected_task[0])
        # Save tasks to the file and update the task display
        save_tasks()
        update_task_display()
    else:
        # Show a warning if no task is selected for deletion
        messagebox.showwarning("Warning!", "Please select a task to delete.")

def mark_done():
    # Get the index of the selected task
    selected_task = listbox.curselection()
    if selected_task:
        # Toggle the "done" status of the selected task
        tasks[selected_task[0]]["done"] = not tasks[selected_task[0]]["done"]
        # Save tasks to the file and update the task display
        save_tasks()
        update_task_display()
    else:
        # Show a warning if no task is selected to mark as done
        messagebox.showwarning("Warning!", "Please select a task to mark as done.")

def update_task_display():
    # Clear the Listbox
    listbox.delete(0, tk.END)
    # Populate the Listbox with tasks, applying visual styles for completed tasks
    for task_info in tasks:
        task = task_info["task"]
        if task_info["done"]:
            listbox.insert(tk.END, task)
            listbox.itemconfig(tk.END, {'fg': 'lime green'})
        else:
            listbox.insert(tk.END, task)

def save_tasks():
    # Save tasks to the file in JSON format
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        # Load tasks from the file in JSON format
        with open("tasks.json", "r") as file:
            tasks.extend(json.load(file))
            update_task_display()
    except FileNotFoundError:
        pass  # File not found on the first run

# Create the main window
root = tk.Tk()
root.title("To-Do List ~Mansi Khand")

# Create a frame with a themed style
style = ttk.Style()
style.theme_use("alt")
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a listbox with a scrollbar to display tasks
listbox = tk.Listbox(frame, selectmode=tk.SINGLE, bg='white', height=10)
listbox.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky=tk.W+tk.E)

# Entry for adding new tasks
entry = ttk.Entry(frame, width=40)
entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W+tk.E)

# Buttons to add, delete, and mark tasks as done
add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=1, column=3, padx=5, pady=10, sticky=tk.W+tk.E)
delete_button = ttk.Button(frame, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=0, padx=5, pady=10, sticky=tk.W+tk.E)
done_button = ttk.Button(frame, text="Mark as Done", command=mark_done)
done_button.grid(row=2, column=1, padx=5, pady=10, sticky=tk.W+tk.E)

# Load tasks from file on startup
tasks = []
load_tasks()

# Run the main loop
root.mainloop()
