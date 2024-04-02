import tkinter as tk
import random
import string

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        
        self.length_label = tk.Label(master, text="Enter password length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, columnspan=2, padx=5, pady=5)
        
        self.result_label = tk.Label(master, text="Generated Password:")
        self.result_label.grid(row=2, column=0, padx=5, pady=5)
        
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, state="readonly", textvariable=self.result_var)
        self.result_entry.grid(row=2, column=1, padx=5, pady=5)
        
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
            
            password_characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(password_characters) for _ in range(length))
            self.result_var.set(password)
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    password_generator_gui = PasswordGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
