import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, height=15, width=50, selectmode=tk.SINGLE, bg="#A0C3F4", fg="black")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.task_entry = tk.Entry(root, width=50, bg="#231E25", fg="white")
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#464447", fg="white")
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, bg="#464447", fg="white")
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#464447", fg="white")
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = simpledialog.askstring("Update Task", "Enter new task:")
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
