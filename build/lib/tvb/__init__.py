#!/usr/bin/env python3

import tkinter as tk

class Calculator:
    """Main class for calculator."""
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # expression label
        self.expression_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.expression_label.grid(row=0, column=0, columnspan=4)

        # number buttons
        self.number_buttons = []
        for i in range(10):
            button = tk.Button(self.master, text=str(i), width=5, height=2,
                               command=lambda i=i: self.add_to_expression(str(i)))
            self.number_buttons.append(button)

        # operator buttons
        self.add_button = tk.Button(self.master, text="+", width=5, height=2,
                                    command=lambda: self.add_operator("+"))
        self.subtract_button = tk.Button(self.master, text="-", width=5, height=2,
                                         command=lambda: self.add_operator("-"))
        self.multiply_button = tk.Button(self.master, text="*", width=5, height=2,
                                         command=lambda: self.add_operator("*"))
        self.divide_button = tk.Button(self.master, text="/", width=5, height=2,
                                       command=lambda: self.add_operator("/"))

        # equals button
        self.equals_button = tk.Button(self.master, text="=", width=5, height=2,
                                        command=self.calculate)

        # clear button
        self.clear_button = tk.Button(self.master, text="Clear", width=5, height=2,
                                        command=self.clear_expression)

        # layout
        for i, button in enumerate(self.number_buttons):
            button.grid(row=1 + i // 3, column=i % 3)
        self.add_button.grid(row=1, column=3)
        self.subtract_button.grid(row=2, column=3)
        self.multiply_button.grid(row=3, column=3)
        self.divide_button.grid(row=4, column=3)
        self.equals_button.grid(row=4, column=2)
        self.clear_button.grid(row=4, column=0)

        # expression
        self.expression = ""

    def add_to_expression(self, s):
        self.expression += s
        self.expression_label.configure(text=self.expression)

    def add_operator(self, op):
        self.expression += " " + op + " "
        self.expression_label.configure(text=self.expression)

    def clear_expression(self):
        self.expression = ""
        self.expression_label.configure(text=self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
        except (SyntaxError, ZeroDivisionError):
            result = "Error"
        self.expression = str(result)
        self.expression_label.configure(text=self.expression)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
