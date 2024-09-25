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
        self.resizable(False, False)
        self.babilon = babilon
        self.clientes = babilon.getClientes()

        # Para almacenar el estado de la ordenación (ascendente o descendente) por cada columna
        self.orden_actual = {"Nombre": True, "Dirección": True, "Teléfono": True}

        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para mostrar los clientes
        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Dirección", "Teléfono"), show='headings')

        # Configurar los encabezados de las columnas con eventos de ordenación
        self.tree.heading("Nombre", text="Nombre", command=lambda: self.ordenar_columnas("Nombre"))
        self.tree.heading("Dirección", text="Dirección", command=lambda: self.ordenar_columnas("Dirección"))
        self.tree.heading("Teléfono", text="Teléfono", command=lambda: self.ordenar_columnas("Teléfono"))

        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Dirección", width=100, anchor="w")
        self.tree.column("Teléfono", width=100, anchor="e")

        # Rellenar el Treeview con los productos
        self.actualizar_lista()

        # Actualizar la lista cada segundo
        self.actualizar_periodicamente()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        self.tree.delete(*self.tree.get_children())  # Borra todos los elementos de la tabla

        # Añadir los clientes a la vista (tabla)
        for cliente in self.clientes:
            self.tree.insert("", "end", values=(cliente.nombre, cliente.direccion, cliente.telefono))

    def actualizar_periodicamente(self):
        # Actualizar la lista de clientes periódicamente
        self.actualizar_lista()
        # Volver a llamar a esta función después de 1000 ms (1 segundo)
        self.after(1000, self.actualizar_periodicamente)

    def ordenar_columnas(self, columna):
        # Mapeo entre los nombres de las columnas y los atributos del cliente
        mapeo_atributos = {
            "Nombre": "nombre",
            "Dirección": "direccion",
            "Teléfono": "telefono"
        }

        # Obtener el nombre del atributo del cliente basado en la columna seleccionada
        atributo = mapeo_atributos[columna]

        # Obtener el estado actual de la ordenación para la columna seleccionada
        orden_ascendente = self.orden_actual[columna]

        # Ordenar la lista de clientes con base en la columna seleccionada
        self.clientes.sort(key=lambda cliente: getattr(cliente, atributo), reverse=not orden_ascendente)

        # Actualizar la cabecera de la columna con una flecha que indica el sentido de ordenación
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)  # Restablecer encabezados

        if orden_ascendente:
            self.tree.heading(columna, text=f"{columna} ↑")
        else:
            self.tree.heading(columna, text=f"{columna} ↓")

        # Cambiar el estado de la ordenación para la próxima vez
        self.orden_actual[columna] = not orden_ascendente

        # Actualizar la lista de clientes con los datos ordenados
        self.actualizar_lista()
