import tkinter as tk
from tkinter import Label, messagebox, ttk
from excepciones.excepciones import *
from src.babilon import Babilon
from src.cliente import Cliente
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *


# Clase para la ventana Toplevel (Crear Cliente)

class EliminarClienteWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.title("Eliminar Cliente")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False,False)
        self.clientes=babilon.getClientes()
        self.babilon = babilon
        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para seleccionar el cliente a eliminar
        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Dirección", "Teléfono"), show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Dirección", text="Dirección")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Dirección", width=50, anchor="w")
        self.tree.column("Teléfono", width=70, anchor="e")

        # Botón para eliminar el cliente seleccionado
        boton_eliminar = tk.Button(contenedor, text="Eliminar Cliente", command=self.eliminar_cliente)
        boton_eliminar.pack(pady=10)

        # Rellenar el Treeview con los clientes
        self.actualizar_lista()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Añadir los productos a la vista
        for cliente in self.clientes:
            self.tree.insert("", "end", iid=cliente.nombre, values=(cliente.nombre, cliente.direccion, cliente.telefono))

    def eliminar_cliente(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un cliente para eliminar.")
            return

        item_values = self.tree.item(selected_item[0])['values']
        nombre = item_values[0]
        
        # Buscar y eliminar el producto
        
        self.clientes = [p for p in self.clientes if p.nombre != nombre]
        self.babilon.setClientes(self.clientes)
        messagebox.showinfo("Éxito", f"Cliente '{nombre}' eliminado correctamente.")
        self.actualizar_lista()
