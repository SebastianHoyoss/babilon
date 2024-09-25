import tkinter as tk
from tkinter import Label, messagebox, ttk
from excepciones.excepciones import *
from src.babilon import Babilon
from src.cliente import Cliente
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *
from ventanas.crear_cliente import CrearClienteWindow
from ventanas.historial_cliente import *

# Clase para la ventana Toplevel
class ClienteWindow(tk.Frame):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)  
        self.configure(bg="azure")
        self.clientes=babilon.getClientes()
        self.babilon = babilon
        self.ids_disponibles = []
        self.pedidos = []
        
        # Establecer un tamaño mínimo para el frame
        self.update_idletasks()  # Actualiza los tamaños requeridos antes de usar geometry
        self.pack_propagate(False)  # Permite que el frame tenga un tamaño fijo
        self.config(width=400, height=300)  # Ajusta según sea necesario
        
        tk.Label(self, text="Gestión de Clientes", bg="azure").pack()
        # Para almacenar el estado de la ordenación (ascendente o descendente) por cada columna
        self.orden_actual = {"ID": True, "Nombre": True, "Dirección": True, "Teléfono": True}
        
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

        # Botónes 
        boton_crear = tk.Button(contenedor, text="Añadir Cliente", command=self.crear_cliente)
        boton_crear.pack(side=tk.LEFT, padx=5, pady=5)
        boton_eliminar = tk.Button(contenedor, text="Eliminar Cliente", command=self.eliminar_cliente)
        boton_eliminar.pack(side=tk.LEFT, padx=5, pady=5)
        boton_historial = tk.Button(contenedor, text="Historial de Cliente", command=self.mostrar_historial)
        boton_historial.pack(side=tk.LEFT, padx=5, pady=5)

        contenedor.pack(anchor="center")
        
        # Rellenar el Treeview con los clientes
        self.actualizar_lista()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Añadir los productos a la vista
        for cliente in self.clientes:
            self.tree.insert("", "end", iid=cliente.id, values=(cliente.id, cliente.nombre, cliente.direccion, cliente.telefono))
        
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
        
        id = selected_item[0]
        
        # Preguntar confirmación antes de eliminar
        confirmacion = messagebox.askyesno("Confirmación", f"¿Estás seguro de que deseas eliminar al cliente con ID '{id}'?")
        
        if confirmacion:  # Si el usuario confirmó la eliminación
            # Buscar y eliminar el cliente
            self.clientes = [p for p in self.clientes if p.id != id]
            self.babilon.setClientes(self.clientes)
            self.ids_disponibles.append(id)
            
            messagebox.showinfo("Éxito", f"Cliente con ID {id} eliminado correctamente.")
            self.actualizar_lista()
        else:
            messagebox.showinfo("Cancelado", "Eliminación cancelada.")

        
    def crear_cliente(self):
        self.actualizar_lista()
        nuevo_id = self.obtener_id_libre()
        # Abrir la ventana CrearClienteWindow pasando el master y el objeto babilon
        nueva_ventana = CrearClienteWindow(self, babilon=self.babilon, id=nuevo_id)
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

    def mostrar_historial(self):
    # Obtener el cliente seleccionado
        selected_item = self.tree.selection()
        if selected_item:
            cliente_id = self.tree.item(selected_item, "values")[0]
            cliente = next((c for c in self.clientes if c.id == cliente_id), None)  # Obtener el cliente correspondiente
            if cliente and cliente.pedidos:  # Asegúrate de que el cliente tenga pedidos
                HistorialCliente(self, cliente_id, cliente.pedidos)  # Ahora pasas los pedidos correctamente
            else:
                messagebox.showinfo("Sin Pedidos", f"No hay pedidos para el cliente {cliente_id}")
        else:
            messagebox.showwarning("Selección", "Por favor selecciona un cliente")
