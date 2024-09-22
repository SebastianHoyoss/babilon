import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# Crear ventana principal
root = tk.Tk()
root.title("Seleccionador de Fecha")

# Variable para almacenar la fecha seleccionada
fecha_var = tk.StringVar()

# Etiqueta para el campo de la fecha
tk.Label(root, text="Fecha:").grid(row=0, column=0)

# Creando el widget de seleccionador de fecha (DateEntry)
calendario = DateEntry(root, textvariable=fecha_var, date_pattern='dd/mm/yyyy', width=15)
calendario.grid(row=0, column=1)

# Función para mostrar la fecha seleccionada
def mostrar_fecha():
    print(f"Fecha seleccionada: {fecha_var.get()}")

# Botón para confirmar la selección de fecha
tk.Button(root, text="Aceptar", command=mostrar_fecha).grid(row=1, column=1)

# Iniciar la aplicación
root.mainloop()
