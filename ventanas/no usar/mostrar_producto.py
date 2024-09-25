import tkinter as tk
from tkinter import Label, messagebox, ttk
from excepciones.excepciones import *
from src.babilon import Babilon
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *


# Clase para la ventana Toplevel (Mostrar Productos)
import tkinter as tk
from tkinter import ttk

class ProductosWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.title("Productos")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False, False)
        self.babilon = babilon
        self.inventario=self.babilon.getInventario()
        self.ids_disponibles = []

        # Diccionario para rastrear el estado de ordenación de cada columna
        self.orden_actual = {
            "ID": True,
            "Nombre": True,
            "Talla": True,
            "Precio": True,
            "Tipo": True,
            "Cantidad": True
        }

        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para mostrar los productos
        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Talla", "Precio", "Tipo", "Cantidad"), show='headings')
        self.tree.heading("Nombre", text="Nombre", command=lambda: self.ordenar_columnas("Nombre"))
        self.tree.heading("Talla", text="Talla", command=lambda: self.ordenar_columnas("Talla"))
        self.tree.heading("Precio", text="Precio", command=lambda: self.ordenar_columnas("Precio"))
        self.tree.heading("Tipo", text="Tipo", command=lambda: self.ordenar_columnas("Tipo"))
        self.tree.heading("Cantidad", text="Cantidad", command=lambda: self.ordenar_columnas("Cantidad"))
        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Talla", width=50, anchor="w")
        self.tree.column("Precio", width=70, anchor="e")
        self.tree.column("Tipo", width=80, anchor="w")
        self.tree.column("Cantidad", width=80, anchor="w")

        # Rellenar el Treeview con los productos
        self.actualizar_lista()
        
        # Actualizar la lista periódicamente
        self.actualizar_periodicamente()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        self.tree.delete(*self.tree.get_children())  # Borra todos los elementos de la tabla

        # Añadir los productos a la vista (tabla)
        inventario = self.babilon.getInventario()
        for producto in inventario:
            self.tree.insert("", "end", values=(producto.nombre, producto.talla, producto.precio, producto.tipo.value, producto.cantidad))

    def actualizar_periodicamente(self):
        # Actualizar la lista de productos periódicamente
        self.actualizar_lista()
        # Volver a llamar a esta función después de 1000 ms (1 segundo)
        self.after(1000, self.actualizar_periodicamente)

    def ordenar_columnas(self, columna):
        # Mapeo entre los nombres de las columnas y los atributos del producto
        mapeo_atributos = {
            "Nombre": "nombre",
            "Talla": "talla",
            "Precio": "precio",
            "Tipo": "tipo",  # Assuming tipo has a string value
            "Cantidad": "cantidad"
        }

        # Obtener el nombre del atributo del producto basado en la columna seleccionada
        atributo = mapeo_atributos[columna]

        # Obtener el estado actual de la ordenación para la columna seleccionada
        orden_ascendente = self.orden_actual[columna]

        # Obtener el inventario
        inventario = self.babilon.getInventario()

        # Ordenar la lista de productos con base en la columna seleccionada
        inventario.sort(key=lambda producto: getattr(producto, atributo) if atributo != "tipo" else producto.tipo.value, 
                       reverse=not orden_ascendente)

        # Actualizar la cabecera de la columna con una flecha que indica el sentido de ordenación
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)  # Restablecer encabezados

        if orden_ascendente:
            self.tree.heading(columna, text=f"{columna} ↑")
        else:
            self.tree.heading(columna, text=f"{columna} ↓")

        # Cambiar el estado de la ordenación para la próxima vez
        self.orden_actual[columna] = not orden_ascendente

        # Actualizar la lista de productos con los datos ordenados
        self.actualizar_lista()

