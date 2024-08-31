import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        # Create task list frame
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill="both", expand=True)

        # Create task list
        self.task_list = tk.Listbox(self.task_list_frame)
        self.task_list.pack(fill="both", expand=True)

        # Create entry field for new tasks
        self.new_task_entry = tk.Entry(self.root)
        self.new_task_entry.pack(fill="x")

        # Create buttons
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(fill="x")

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(fill="x")

        self.save_tasks_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_tasks_button.pack(fill="x")

        self.load_tasks_button = tk.Button(self.root, text="Load Tasks", command=self.load_tasks)
        self.load_tasks_button.pack(fill="x")

    def add_task(self):
        task = self.new_task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.new_task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showerror("Error", "Select a task to delete")

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Tasks Saved", "Tasks saved to tasks.txt")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
                self.task_list.delete(0, tk.END)
                for task in self.tasks:
                    self.task_list.insert(tk.END, task)
        except FileNotFoundError:
            messagebox.showerror("Error", "Tasks file not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()