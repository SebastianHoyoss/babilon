import tkinter as tk
from src.cliente import Cliente
from excepciones.excepciones import *


# Clase para la ventana Toplevel (Crear Cliente)
class CrearClienteWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None, id=None):
        super().__init__(master)
        self.title("Añadir Cliente")
        self.geometry("300x200")
        self.configure(bg="azure")
        self.resizable(False,False)
        self.babilon = babilon
        self.id_cliente = id
        self.clientes=babilon.getClientes()
        
        # Debug: imprime el ID
        #print(f"ID del cliente: {self.id_cliente}")  

        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')
        
        #Campo para el ID
        tk.Label(contenedor, text="ID").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_id = tk.Entry(contenedor, state='normal', width=20) 
        self.entry_id.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        if self.id_cliente is not None:  
            self.entry_id.insert(0, self.id_cliente)
            self.entry_id.config(state='readonly')
        
        # Campo para el nombre
        tk.Label(contenedor, text="Nombre").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(contenedor, width=20)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Campo para la talla
        tk.Label(contenedor, text="Dirección").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_direccion = tk.Entry(contenedor, width=20)
        self.entry_direccion.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Campo para el precio
        tk.Label(contenedor, text="Teléfono").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_telefono = tk.Entry(contenedor, width=20)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Botón para crear el producto
        boton_crear = tk.Button(contenedor, text="Añadir Cliente", command=self.crear_cliente)
        boton_crear.grid(row=4, columnspan=2, pady=10)

    def crear_cliente(self):
        nombre = self.entry_nombre.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()

        if validar_nombre(nombre, "Nombre") and validar_dir(direccion, "Dirección") and validar_tel(telefono, "Teléfono"):            
            cliente = Cliente(self.id_cliente, nombre, direccion, telefono)
            self.babilon.agregar_cliente(cliente)  # Añadir el producto a la lista
            # Mostrar un messagebox con la información del producto creado
            messagebox.showinfo("Éxito", f"Cliente creado:\nID: {cliente.id}\nNombre: {cliente.nombre}\nDirección: {cliente.direccion}\nTeléfono: {cliente.telefono}")
            self.destroy()  # Cierra la ventana después de crear el producto
            
