import tkinter as tk
from tkinter import messagebox

class TodoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.tasks = []
        
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(master, textvariable=self.task_var)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        self.view_button = tk.Button(master, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.complete_button = tk.Button(master, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=2, column=1, padx=5, pady=5)
        
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=3, column=0, padx=5, pady=5)
        
        self.save_button = tk.Button(master, text="Save Tasks", command=self.save_to_file)
        self.save_button.grid(row=3, column=1, padx=5, pady=5)
        
        self.load_button = tk.Button(master, text="Load Tasks", command=self.load_from_file)
        self.load_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
            
    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        if self.tasks:
            for task in self.tasks:
                self.task_listbox.insert(tk.END, task)
        else:
            messagebox.showinfo("Info", "No tasks.")
            
    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index] = "[Completed] " + self.tasks[index]
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, self.tasks[index])
        else:
            messagebox.showwarning("Warning", "Please select a task to complete.")
            
    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")
            
    def save_to_file(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, 'w') as file:
                for task in self.tasks:
                    file.write(task + '\n')
            messagebox.showinfo("Info", "Tasks saved to file successfully.")
            
    def load_from_file(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, 'r') as file:
                self.tasks = [line.strip() for line in file]
            self.view_tasks()
            messagebox.showinfo("Info", "Tasks loaded from file successfully.")

def main():
    root = tk.Tk()
    todo_list_gui = TodoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
