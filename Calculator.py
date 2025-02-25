import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Variables
        self.current_input = tk.StringVar()
        self.history = []

        # Create GUI components
        self.create_display()
        self.create_buttons()
        self.create_history()

    # Create the display area
    def create_display(self):
        display_frame = tk.Frame(self.root, height=100)
        display_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        self.display = tk.Entry(
            display_frame,
            textvariable=self.current_input,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief=tk.RIDGE,
            state="readonly"
        )
        self.display.pack(fill=tk.BOTH, expand=True)

    # Create the buttons
    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("C", 3, 2), ("+", 3, 3),
            ("=", 4, 0, 1, 4)  # Span 1 row and 4 columns
        ]

        for button in buttons:
            if len(button) == 4:  # Handle the "=" button
                btn = tk.Button(
                    button_frame,
                    text=button[0],
                    font=("Arial", 18),
                    command=lambda b=button[0]: self.on_button_click(b)
                )
                btn.grid(row=button[1], column=button[2], rowspan=button[3], columnspan=button[4], sticky="nsew")
            else:
                btn = tk.Button(
                    button_frame,
                    text=button[0],
                    font=("Arial", 18),
                    command=lambda b=button[0]: self.on_button_click(b)
                )
                btn.grid(row=button[1], column=button[2], sticky="nsew")

        # Configure grid weights
        for i in range(4):
            button_frame.grid_rowconfigure(i, weight=1)
            button_frame.grid_columnconfigure(i, weight=1)

    # Create the history area
    def create_history(self):
        history_frame = tk.Frame(self.root, height=100)
        history_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        self.history_label = tk.Label(
            history_frame,
            text="History",
            font=("Arial", 14),
            anchor="w"
        )
        self.history_label.pack(fill=tk.X)

        self.history_text = tk.Text(
            history_frame,
            font=("Arial", 12),
            state="disabled",
            height=5
        )
        self.history_text.pack(fill=tk.BOTH, expand=True)

    # Handle button clicks
    def on_button_click(self, value):
        if value == "C":
            self.current_input.set("")
        elif value == "=":
            self.calculate_result()
        else:
            self.current_input.set(self.current_input.get() + value)

    # Calculate the result
    def calculate_result(self):
        try:
            expression = self.current_input.get()
            if not expression:
                return

            result = str(eval(expression))
            self.current_input.set(result)

            # Log history
            self.history.append(f"{expression} = {result}")
            self.update_history()
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.current_input.set("")

    # Update the history display
    def update_history(self):
        self.history_text.config(state="normal")
        self.history_text.delete(1.0, tk.END)
        for entry in self.history:
            self.history_text.insert(tk.END, entry + "\n")
        self.history_text.config(state="disabled")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()