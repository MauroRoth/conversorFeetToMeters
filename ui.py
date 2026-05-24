# ui.py

import tkinter as tk
from tkinter import ttk


def create_ui():
    # Ventana principal
    root = tk.Tk()
    root.title("Feet to Meters")
    root.geometry('600x400')
    
    # Marco principal
    mainframe = ttk.Frame(root, padding="12 12 12 12")
    mainframe.grid(column=0, row=0, sticky=("N", "W", "E", "S"))

    # Variables
    feet_var = tk.StringVar()
    meters_var = tk.StringVar()
    def validar_decimales(P):
        # Permite el campo vacío o un punto solitario en proceso de escritura
        if P == "" or P == ".":
            return True
        try:
            # Intenta convertir el texto a número decimal
            float(P)
            return True
        except ValueError:
            # Si la conversión falla (contiene letras u otros caracteres), se rechaza
            return False
    vcmd = (root.register(validar_decimales), '%P')
    # Widgets
    feet_entry = ttk.Entry(
        mainframe,
        width=10,
        textvariable=feet_var,
        validate="key",
        validatecommand=vcmd
    )

    result_label = ttk.Label(
        mainframe,
        textvariable=meters_var
    )

    calculate_button = ttk.Button(
        mainframe,
        text="Calculate"
    )

    # Layout
    feet_entry.grid(column=1, row=1)

    ttk.Label(mainframe, text="feet").grid(column=2, row=1)

    ttk.Label(mainframe, text="is equivalent to").grid(column=0, row=2)

    result_label.grid(column=1, row=2)

    ttk.Label(mainframe, text="meters").grid(column=2, row=2)

    calculate_button.grid(column=2, row=3)

    # Espaciado
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    feet_entry.focus()

    # Devolver referencias útiles
    return {
        "root": root,
        "feet_var": feet_var,
        "meters_var": meters_var,
        "feet_entry": feet_entry,
        "calculate_button": calculate_button
    }
    