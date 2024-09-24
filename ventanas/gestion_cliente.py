import tkinter as tk
from tkinter import Label, messagebox, ttk
from excepciones.excepciones import *
from src.babilon import Babilon
from src.cliente import Cliente
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *
from ventanas.crear_cliente import CrearClienteWindow


# Clase para la ventana Toplevel
class ClienteWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.title("Gestionar Cliente")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False,False)
        self.clientes=babilon.getClientes()
        self.babilon = babilon
        
        # Para almacenar el estado de la ordenación (ascendente o descendente) por cada columna
        self.orden_actual = {"Nombre": True, "Dirección": True, "Teléfono": True}
        
        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para seleccionar el cliente a eliminar
        self.tree = ttk.Treeview(contenedor, columns=("ID", "Nombre", "Dirección", "Teléfono"), show='headings')
        self.tree.heading("ID", text="ID", command=lambda: self.ordenar_columnas("ID"))
        self.tree.heading("Nombre", text="Nombre", command=lambda: self.ordenar_columnas("Nombre"))
        self.tree.heading("Dirección", text="Dirección", command=lambda: self.ordenar_columnas("Dirección"))
        self.tree.heading("Teléfono", text="Teléfono", command=lambda: self.ordenar_columnas("Teléfono"))
        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("ID", width=20, anchor="w")
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Dirección", width=50, anchor="w")
        self.tree.column("Teléfono", width=70, anchor="e")

        # Botónnes 
        boton_crear = tk.Button(contenedor, text="Crear Cliente", command=self.crear_cliente)
        boton_crear.pack(side=tk.LEFT, padx=5, pady=5)
        boton_eliminar = tk.Button(contenedor, text="Eliminar Cliente", command=self.eliminar_cliente)
        boton_eliminar.pack(side=tk.LEFT, padx=5, pady=5)

        contenedor.pack(anchor="center")
        
        # Rellenar el Treeview con los clientes
        self.actualizar_lista()
        
        self.actualizar_periodicamente()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Añadir los productos a la vista
        for cliente in self.clientes:
            self.tree.insert("", "end", iid=cliente.id, values=(cliente.id, cliente.nombre, cliente.direccion, cliente.telefono))
    
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
            "Teléfono": "telefono",
            "ID": "id"
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


    def eliminar_cliente(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un cliente para eliminar.")
            return

        item_values = self.tree.item(selected_item[0])['values']
        id = item_values[0]
        
        # Buscar y eliminar el producto
        
        self.clientes = [p for p in self.clientes if p.id != id]
        self.babilon.setClientes(self.clientes)
        messagebox.showinfo("Éxito", f"Cliente con ID '{id}' eliminado correctamente.")
        self.actualizar_lista()
        
    def crear_cliente(self):
        # Abrir la ventana CrearClienteWindow pasando el master y el objeto babilon
        CrearClienteWindow(self, babilon=self.babilon)
        self.actualizar_lista()
