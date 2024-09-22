import tkinter as tk
from tkinter import Label, messagebox, ttk
from excepciones.excepciones import *
from src.babilon import Babilon
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *


# Clase para la ventana Toplevel (Eliminar Producto)
class EliminarProductoWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.title("Eliminar Producto")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False,False)
        self.self.babilon = self.babilon
        self.inventario=self.babilon.getInventario()
        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para seleccionar el producto a eliminar
        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Talla", "Precio", "Tipo","Cantidad"), show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Talla", text="Talla")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Talla", width=50, anchor="w")
        self.tree.column("Precio", width=70, anchor="e")
        self.tree.column("Tipo", width=80, anchor="w")
        self.tree.column("Cantidad", width=80, anchor="w")
        
        cantidad_eliminar=Label(contenedor,text="Cantidad a eliminar")
        cantidad_eliminar.pack()

        self.entry_nombre = tk.Entry(contenedor, width=20)
        self.entry_nombre.pack()

        # Botón para eliminar el producto seleccionado
        boton_eliminar = tk.Button(contenedor, text="Eliminar Producto", command=self.eliminar_producto)
        boton_eliminar.pack(pady=10)

        # Rellenar el Treeview con los productos
        self.actualizar_lista()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Añadir los productos a la vista
        for producto in self.inventario:
            self.tree.insert("", "end", iid=producto.nombre, values=(producto.nombre, producto.talla, producto.precio, producto.tipo.value,producto.cantidad))

    def eliminar_producto(self):
        cantidad=self.entry_nombre.get()
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para eliminar.")
            return
        if validar_num(cantidad,"Cantidad"):
            item_values = self.tree.item(selected_item[0])['values']
            nombre = item_values[0]
            cantidad=int(cantidad)
        # Buscar y eliminar el producto
            new_inv=self.babilon.eliminar_producto(nombre,cantidad, Babilon.inventario)
            self.inventario=new_inv
            self.babilon.setInv(self.inventario)
        messagebox.showinfo("Éxito", f"{cantidad} de '{nombre}' eliminado correctamente.")
        self.actualizar_lista()