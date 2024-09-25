import tkinter as tk
from tkinter import Label, messagebox, ttk
from excepciones.excepciones import *
from src.babilon import Babilon
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *

from ventanas.actualizar_precios import ActualizarPreciosWindow
from ventanas.crear_producto import CrearProductoWindow
from ventanas.eliminar_producto import EliminarProductoWindow

class ProductoWindow(tk.Frame):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.configure(bg="azure")
        self.babilon = babilon
        self.inventario=self.babilon.getInventario()
        self.ids_disponibles = []
        
        # Establecer un tamaño mínimo para el frame
        self.update_idletasks()  # Actualiza los tamaños requeridos antes de usar geometry
        self.pack_propagate(False)  # Permite que el frame tenga un tamaño fijo
        self.config(width=400, height=300)  # Ajusta según sea necesario
        
        tk.Label(self, text="Gestión de Clientes", bg="azure").pack()
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
        self.tree = ttk.Treeview(contenedor, columns=("ID","Nombre", "Talla", "Precio", "Tipo", "Cantidad"), show='headings')
        self.tree.heading("ID", text="ID", command=lambda: self.ordenar_columnas("ID"))
        self.tree.heading("Nombre", text="Nombre", command=lambda: self.ordenar_columnas("Nombre"))
        self.tree.heading("Talla", text="Talla", command=lambda: self.ordenar_columnas("Talla"))
        self.tree.heading("Precio", text="Precio", command=lambda: self.ordenar_columnas("Precio"))
        self.tree.heading("Tipo", text="Tipo", command=lambda: self.ordenar_columnas("Tipo"))
        self.tree.heading("Cantidad", text="Cantidad", command=lambda: self.ordenar_columnas("Cantidad"))
        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("ID", width=40, anchor="w")
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Talla", width=50, anchor="w")
        self.tree.column("Precio", width=70, anchor="e")
        self.tree.column("Tipo", width=80, anchor="w")
        self.tree.column("Cantidad", width=80, anchor="w")
        
        # Botónes 
        boton_crear = tk.Button(contenedor, text="Añadir Producto", command=self.crear_producto)
        boton_crear.pack(side=tk.LEFT, padx=5, pady=5)
        boton_eliminar = tk.Button(contenedor, text="Eliminar Producto", command=self.eliminar_producto)
        boton_eliminar.pack(side=tk.LEFT, padx=5, pady=5)
        boton_eliminar = tk.Button(contenedor, text="Actualizar Precios", command=self.actualizar_precios)
        boton_eliminar.pack(side=tk.LEFT, padx=5, pady=5)

        contenedor.pack(anchor="center")

        # Rellenar el Treeview con los productos
        self.actualizar_lista()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(*self.tree.get_children())  # Borra todos los elementos de la tabla

        # Añadir los productos a la vista (tabla)
        for producto in self.inventario:
            self.tree.insert("", "end", iid=producto.id, values=(producto.id, producto.nombre, producto.talla, producto.precio, producto.tipo.value, producto.cantidad))

    def ordenar_columnas(self, columna):
        # Mapeo entre los nombres de las columnas y los atributos del producto
        mapeo_atributos = {
            "Nombre": "nombre",
            "Talla": "talla",
            "Precio": "precio",
            "Tipo": "tipo",  # Assuming tipo has a string value
            "Cantidad": "cantidad",
            "ID": "id"
        }

        # Obtener el nombre del atributo del producto basado en la columna seleccionada
        atributo = mapeo_atributos[columna]

        # Obtener el estado actual de la ordenación para la columna seleccionada
        orden_ascendente = self.orden_actual[columna]
        # Obtener 

        # Ordenar la lista de productos con base en la columna seleccionada
        self.inventario.sort(key=lambda producto: getattr(producto, atributo) if atributo != "tipo" else producto.tipo.value, 
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
    
    def crear_producto(self):
        self.actualizar_lista()
        nuevo_id = self.obtener_id_libre()
        # Abrir la ventana CrearClienteWindow pasando el master y el objeto babilon
        nueva_ventana = CrearProductoWindow(self, babilon=self.babilon, id=nuevo_id)
        self.wait_window(nueva_ventana)
        self.actualizar_lista()
        
    def obtener_id_libre(self):
        # Si hay IDs eliminadas, reutilizarlas primero
        if self.ids_disponibles:
            self.ids_disponibles.sort()  # Asegurarse de que estén en orden
            return self.ids_disponibles.pop(0)  # Reutilizar la primera ID disponible
    
        # Si no hay IDs eliminadas, usar el enfoque secuencial
        nuevo_id = 1
        while True:
            id_str = str(nuevo_id).zfill(3)  # Convertir el número a formato '001', '002', etc.
            if not any(cliente.id == id_str for cliente in self.clientes):
                return id_str  # Si no está en uso, devolverla
            nuevo_id += 1  # Continuar con la siguiente ID

        
    def eliminar_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para eliminar.")
            return
        
        # Obtener el producto seleccionado
        item_values = self.tree.item(selected_item[0])['values']
        id_producto = int(item_values[0])  # Asegúrate de que esto sea un entero
        
        producto_seleccionado = None
        for producto in self.inventario:
            if int(producto.id) == id_producto:  # Asegúrate de comparar como enteros
                producto_seleccionado = producto
                break

        if producto_seleccionado:
            # Abrir la ventana de eliminación
            ventana_eliminar = EliminarProductoWindow(
                self, 
                producto_seleccionado, 
                self.actualizar_lista, 
                self.eliminar_producto_completamente
            )
            self.wait_window(ventana_eliminar)
            self.actualizar_lista()
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

    def eliminar_producto_completamente(self, producto):
    # Lógica para eliminar el producto completamente
        self.inventario.remove(producto)
        self.ids_disponibles.append(producto.id)  # Añadir el ID eliminado a los disponibles
        self.actualizar_lista()
    
    def actualizar_precios(self):
        # Obtener el producto seleccionado directamente del Treeview
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para actualizar su precio.")
            return

        # Obtener la ID del producto seleccionado (suponiendo que está en la primera columna)
        item = seleccion[0]
        producto_id = self.tree.item(item, 'values')[0]  # Cambia esto para que obtenga la ID

        # Crear una ventana para actualizar precios pasando la ID del producto seleccionado
        ventana_actualizar = ActualizarPreciosWindow(self, self.inventario, producto_id)
        self.wait_window(ventana_actualizar)  # Espera a que la ventana se cierre
        self.actualizar_lista()  # Actualiza la lista después de cerrar la ventana


