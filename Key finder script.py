import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Configure rows and columns to expand
for i in range(3):  # Three rows
    root.rowconfigure(i, weight=1)
for j in range(3):  # Three columns
    root.columnconfigure(j, weight=1)

# Create buttons and place them in a grid
buttons = []
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text=f"Button {i+1},{j+1}")
        btn.grid(row=i, column=j, sticky="nsew")
        buttons.append(btn)

root.mainloop()