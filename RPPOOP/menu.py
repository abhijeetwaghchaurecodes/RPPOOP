import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        
        # Create entry widget
        self.entry = tk.Entry(self.master, width=30, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Create buttons
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)
        
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)
        
        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)
        
        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('C', 4, 2)
        self.create_button('+', 4, 3)
        
        self.create_button('=', 5, 0, columnspan=4)
        
        # Create menu
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New", command=self.clear)
        self.file_menu.add_command(label="Exit", command=self.exit)
        
        self.function_menu = tk.Menu(self.menu, tearoff=0)
        self.function_menu.add_command(label="Square", command=self.square)
        self.function_menu.add_command(label="Square Root", command=self.square_root)
        
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.menu.add_cascade(label="Function", menu=self.function_menu)
    
    def create_button(self, text, row, col, columnspan=1):
        button = tk.Button(self.master, text=text, padx=10, pady=10, font=('Arial', 12), command=lambda:self.button_click(text))
        button.grid(row=row, column=col, columnspan=columnspan, padx=5, pady=5)
    
    def button_click(self, text):
        if text == 'C':
            self.clear()
        elif text == '=':
            self.calculate()
        else:
            self.entry.insert(tk.END, text)
    
    def clear(self):
        self.entry.delete(0, tk.END)
    
    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except:
            messagebox.showerror("Error", "Invalid expression")
    
    def square(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result**2)
        except:
            messagebox.showerror("Error", "Invalid expression")
    
    def square_root(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result**(1/2))
        except:
            messagebox.showerror("Error", "Invalid expression")

    def exit(self):
        self.master.destroy()


root = tk.Tk()
app = Calculator(root)
root.mainloop()
