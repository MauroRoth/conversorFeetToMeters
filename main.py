import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Feet to Meters")
mainframe = ttk.Frame(root, padding=(3,3,12,12))
mainframe.grid(column=0, row=0, sticky=("nsew"))

root.mainloop()