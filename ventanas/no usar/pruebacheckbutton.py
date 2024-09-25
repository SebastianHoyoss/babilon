import tkinter as tk

def mostrar_estado():
    estado = var.get()
    if estado == 1:
        print("Checkbox seleccionada")
    else:
        print("Checkbox no seleccionada")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Checkbox")

# Variable para almacenar el estado de la checkbox (1=seleccionado, 0=no seleccionado)
var = tk.IntVar()

# Crear el Checkbutton
checkbox = tk.Checkbutton(root, text="Opción 1", variable=var, command=mostrar_estado)
checkbox.pack()

# Iniciar el loop de la aplicación
root.mainloop()