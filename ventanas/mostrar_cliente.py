import tkinter as tk
from tkinter import Label, messagebox, ttk
from excepciones.excepciones import *
from src.babilon import Babilon
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *


# Clase para la ventana Toplevel (Crear Cliente)

class MostrarClientesWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.title("Clientes")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False,False)
        self.babilon = babilon
        self.clientes=babilon.getClientes()
        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para mostrar los productos
        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Dirección", "Teléfono"), show='headings')
        self.tree.heading("Nombre", text="Nombre", command=lambda: self.ordenar_columnas("Nombre"))
        self.tree.heading("Dirección", text="Dirección", command=lambda: self.ordenar_columnas("Dirección"))
        self.tree.heading("Teléfono", text="Teléfono", command=lambda: self.ordenar_columnas("Teléfono"))
        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Dirección", width=50, anchor="w")
        self.tree.column("Teléfono", width=70, anchor="e")

        # Rellenar el Treeview con los productos
        self.actualizar_lista()

        # Actualizar la lista cada segundo
        self.actualizar_periodicamente()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Añadir los productos a la vista
        self.clientes=self.babilon.getClientes()
        for cliente in self.clientes:
            self.tree.insert("", "end", values=(cliente.nombre, cliente.direccion, cliente.telefono))

    def actualizar_periodicamente(self):
        # Actualizar la lista
        self.actualizar_lista()
        # Volver a llamar a esta función después de 1000 ms (1 segundo)
        self.after(1000, self.actualizar_periodicamente)

    def ordenar_columnas(self, columna):
        # Determinar el orden actual
        items = list(self.tree.get_children())
        if self.tree.heading(columna, "text").endswith(" ↑"):
            # Ordenar en orden descendente
            items.sort(key=lambda x: self.tree.item(x, 'values')[self.tree["columns"].index(columna)], reverse=True)
            self.tree.heading(columna, text=f"{columna} ↓")
        else:
            # Ordenar en orden ascendente
            items.sort(key=lambda x: self.tree.item(x, 'values')[self.tree["columns"].index(columna)])
            self.tree.heading(columna, text=f"{columna} ↑")

        # Reinsertar los elementos ordenados
        for item in items:
            self.tree.move(item, '', 'end')