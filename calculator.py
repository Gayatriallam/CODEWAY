import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        
        self.num1_label = tk.Label(master, text="Enter first number:")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(master)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.num2_label = tk.Label(master, text="Enter second number:")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry = tk.Entry(master)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.operation_label = tk.Label(master, text="Select operation:")
        self.operation_label.grid(row=2, column=0, padx=5, pady=5)
        self.operation_var = tk.StringVar()
        self.operation_var.set("+")
        self.operation_menu = tk.OptionMenu(master, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.grid(row=2, column=1, padx=5, pady=5)
        
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, columnspan=2, padx=5, pady=5)
        
        self.result_label = tk.Label(master, text="Result:")
        self.result_label.grid(row=4, column=0, padx=5, pady=5)
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, state="readonly", textvariable=self.result_var)
        self.result_entry.grid(row=4, column=1, padx=5, pady=5)
        
    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Invalid operation!")
                return
                
            self.result_var.set(result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    calculator_gui = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
