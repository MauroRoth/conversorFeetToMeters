# IMPORTANDO TK
import tkinter as tk
from tkinter import ttk

# IMPORTANDO LA FUNCION DE CONVERSION
from conversiones import feetToMeters

# REALIZANDO EL CÁLCULO
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(feetToMeters(value), 4))
    except ValueError:
        pass

# CONFIGURANDO LA VENTANA PRINCIPAL DE LA APLICACIÓN
root = tk.Tk()
root.title("Feet to Meters")

# CREANDO UN MARCO DE CONTENIDO
mainframe = ttk.Frame(root, padding=(3,3,12,12))
# INSERTANDO EL MARCO EN LA INTERFAZ DE USUARIO
mainframe.grid(column=0, row=0, sticky=(tk.NSEW))

# CREACIÓN DEL WIDGET DE ENTRADA
feet = tk.StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(tk.EW))

# CREANDO LOS WIDGETS RESTANTES
meters = tk.StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(tk.W,tk.E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3,row=3,sticky='w')

ttk.Label(mainframe, text="feet").grid(column=3,row=1,sticky=tk.W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1,row=2,sticky=tk.E)
ttk.Label(mainframe, text="meters").grid(column=3,row=2,sticky=tk.W)


# AÑADIENDO UN POCO DE PULIDO
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
mainframe.columnconfigure(2,weight=1)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)
feet_entry.focus()
root.bind('<Return>', calculate)


root.mainloop()