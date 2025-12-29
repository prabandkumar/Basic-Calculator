import tkinter as tk
from tkinter import messagebox

def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "%":
        return a % b
    else:
        raise ValueError("Not valid operator")

root = tk.Tk()
root.title("My Calculator")
root.geometry("320x420")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), bd=4, relief="ridge", justify="right")
entry.pack(fill="x", padx=8, pady=10, ipady=8)

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ['C','<-','(',')']
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=8, pady=4)

def on_click(ch):
    if ch == 'C':
        entry.delete(0, tk.END)
    elif ch == '<-':
        entry.delete(len(entry.get()) - 1)
    elif ch == '=':
        expr = entry.get()
        try:
            for op in ['+','-','*','/','%']:
                if op in expr:
                    parts = expr.split(op)
                    a = float(parts[0])
                    b = float(parts[1])
                    result = calculate(a, op, b)
                    entry.delete(0, tk.END)
                    entry.insert(0, str(result))
                    return
            messagebox.showerror("Error", "Invalid Input")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        entry.insert(tk.END, ch)

for r,row in enumerate(buttons):
    for c,ch in enumerate(row):
        tk.Button(frame, text=ch, font=("Arial", 18),
                  command=lambda ch=ch: on_click(ch)).grid(
            row=r, column=c, sticky="nsew", padx=3, pady=3
        )

for i in range(5):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

root.mainloop()
