import tkinter as tk
from src.cliente import Cliente
from excepciones.excepciones import *

# Clase para la ventana Toplevel (Crear Cliente)
class CrearClienteWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.title("Añadir Cliente")
        self.geometry("300x200")
        self.configure(bg="azure")
        self.resizable(False,False)
        self.babilon = babilon
        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')
        self.clientes=babilon.getClientes()
        # Campo para el nombre
        tk.Label(contenedor, text="Nombre").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(contenedor, width=20)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Campo para la talla
        tk.Label(contenedor, text="Dirección").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_direccion = tk.Entry(contenedor, width=20)
        self.entry_direccion.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Campo para el precio
        tk.Label(contenedor, text="Teléfono").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_telefono = tk.Entry(contenedor, width=20)
        self.entry_telefono.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Botón para crear el producto
        boton_crear = tk.Button(contenedor, text="Añadir Cliente", command=self.crear_cliente)
        boton_crear.grid(row=4, columnspan=2, pady=10)

    def crear_cliente(self):
        
        nuevo_id = f"{len(self.clientes) + 1:03}"
        nombre = self.entry_nombre.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()

        if validar_nombre(nombre, "Nombre") and validar_dir(direccion, "Dirección") and validar_tel(telefono, "Teléfono"):            
            cliente = Cliente(nuevo_id, nombre, direccion, telefono)
            self.babilon.agregar_cliente(cliente)  # Añadir el producto a la lista
            # Mostrar un messagebox con la información del producto creado
            messagebox.showinfo("Éxito", f"Cliente creado:\nID: {cliente.id}\nNombre: {cliente.nombre}\nDirección: {cliente.direccion}\nTeléfono: {cliente.telefono}")
            self.destroy()  # Cierra la ventana después de crear el producto
            # Actualizar la lista en la ventana de mostrar productos, si está abierta
