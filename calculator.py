import tkinter as tk

class Calculator:
    def __init__(self, master):
        """
        Initializes the Calculator application.

        Parameters:
        master (Tk): The main window of the application.
        """
        self.master = master
        master.title("Simple Calculator")

        self.result = tk.StringVar()

        # Entry widget to display the result
        self.entry = tk.Entry(master, textvariable=self.result, font=("Arial", 16), 
                              bd=10, insertwidth=1, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Define buttons with their respective positions
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create buttons using the predefined layout
        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        """
        Creates a button and places it in the grid.

        Parameters:
        text (str): The text displayed on the button.
        row (int): The row in the grid where the button will be placed.
        col (int): The column in the grid where the button will be placed.
        """
        button = tk.Button(self.master, text=text, padx=20, pady=20, font=("Arial", 16),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col)

    def on_button_click(self, char):
        """
        Handles button click events.

        Parameters:
        char (str): The character associated with the button that was clicked.
        """
        if char == 'C':
            # Clear the entry field
            self.result.set("")
        elif char == '=':
            # Evaluate the expression and set the result
            try:
                self.result.set(eval(self.result.get()))
            except Exception:
                self.result.set("Error")
        else:
            # Append the clicked character to the entry field
            current_text = self.result.get()
            new_text = current_text + str(char)
            self.result.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()