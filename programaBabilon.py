from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from enum import Enum
import time
from baseDatos.serializacion import serializar, deserializar
from excepciones import *

class Tipo(Enum):
    Tennis = "Tennis"
    Bota = "Bota"
    Sandalia = "Sandalia"

class Tipo2(Enum):
    Aceptado = "Aceptado"
    Cancelado = "Cancelado"
    Devuelto = "Devuelto"

class Producto:
    def __init__(self, nombre, talla, precio, tipo, cantidad):
        self.nombre = nombre
        self.talla = talla
        self.precio = precio
        self.tipo = tipo
        self.cantidad= cantidad

class Pedido:
    def __init__(self, numero, hora_salida, hora_entrega, productos, estado):
        self.numero = numero
        self.hora_salida = hora_salida
        self.hora_entrega = hora_entrega
        self.productos = productos
        self.estado = estado

class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.pedidos = []

class Venta:
    def __init__(self, numero, cliente, fecha, pedido, valor_total):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha
        self.pedido = pedido
        self.valor_total = valor_total

class Babilon:
    def __init__(self, nombre="Babiloon",clientes=[],inventario=[]):
        self.nombre=nombre
        self.clientes=[]
        self.inventario=[]

    def getClientes(self):
        return self.clientes

    def getInventario(self):
        return self.inventario

    def setInv(self,inventario):
        self.inventario=inventario

    def setClientes(self,clientes):
        self.clientes=clientes

    def agregar_producto(self, producto):

        for p in self.inventario:
            if p.nombre == producto.nombre and p.talla == producto.talla:
                p.cantidad += producto.cantidad
                return
        self.inventario.append(producto)

    def eliminar_producto(self, nombre, cantidad,inventario):
        self.inventario=inventario
        for p in self.inventario:
            if p.nombre == nombre:
                if p.cantidad <= cantidad:
                    self.inventario.remove(p)
                else:
                    p.cantidad -= cantidad
                return self.inventario

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        return self.clientes
    
    def retirar_cliente(self,nombre,clientes):
        self.clientes=clientes
        for p in self.clientes:
            if p.nombre==nombre:
                self.clientes.remove(p)
# Clase para la ventana Toplevel (Crear Producto)
class ProductoWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Añadir Producto")
        self.geometry("250x200")
        self.configure(bg="azure")
        self.resizable(False,False)
        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Campo para el nombre
        tk.Label(contenedor, text="Nombre").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(contenedor, width=20)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Campo para la talla
        tk.Label(contenedor, text="Talla").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_talla = tk.Entry(contenedor, width=20)
        self.entry_talla.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Campo para el precio
        tk.Label(contenedor, text="Precio").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_precio = tk.Entry(contenedor, width=20)
        self.entry_precio.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Menú desplegable para el tipo de producto
        tk.Label(contenedor, text="Tipo").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.tipo_var = tk.StringVar()
        self.combo_tipo = ttk.Combobox(contenedor, width=17, textvariable=self.tipo_var)
        self.combo_tipo['values'] = [tipo.value for tipo in Tipo]
        self.combo_tipo.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        tk.Label(contenedor, text="Cantidad").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_cantidad = tk.Entry(contenedor, width=20)
        self.entry_cantidad.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Botón para crear el producto
        boton_crear = tk.Button(contenedor, text="Añadir Producto", command=self.crear_producto)
        boton_crear.grid(row=5, columnspan=2, pady=10)

    def crear_producto(self):
        nombre = self.entry_nombre.get()
        talla = self.entry_talla.get()
        precio = self.entry_precio.get()
        tipo = self.tipo_var.get()
        cantidad = self.entry_cantidad.get()

        if validar_producto(nombre, "Nombre") and validar_num(talla, "Talla") and validar_num(precio, "Precio") and validar_num(cantidad, "Cantidad") and tipo:
            producto = Producto(nombre, talla, float(precio), Tipo(tipo), int(cantidad))
            babilon.agregar_producto(producto)  # Añadir el producto a la lista
            # Mostrar un messagebox con la información del producto creado
            messagebox.showinfo("Éxito", f"Producto creado:\nNombre: {producto.nombre}\nTalla: {producto.talla}\nPrecio: {producto.precio}\nTipo: {producto.tipo.value}\nCantidad: {producto.cantidad}")
            self.destroy()  # Cierra la ventana después de crear el producto
            # Actualizar la lista en la ventana de mostrar productos, si está abierta
            if hasattr(self.master, 'mostrar_productos_window'):
                self.master.mostrar_productos_window.actualizar_lista()

# Clase para la ventana Toplevel (Mostrar Productos)
class MostrarProductosWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Productos")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False,False)

        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para mostrar los productos
        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Talla", "Precio", "Tipo","Cantidad"), show='headings')
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
        
        # Actualizar la lista cada segundo
        self.actualizar_periodicamente()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Añadir los productos a la vista
        inventario=babilon.getInventario()
        for producto in inventario:
            self.tree.insert("", "end", values=(producto.nombre, producto.talla, producto.precio, producto.tipo.value,producto.cantidad))

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

# Clase para la ventana Toplevel (Eliminar Producto)
class EliminarProductoWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Eliminar Producto")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False,False)
        self.inventario=babilon.getInventario()
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
            new_inv=babilon.eliminar_producto(nombre,cantidad,inventario)
            self.inventario=new_inv
            babilon.setInv(self.inventario)
        messagebox.showinfo("Éxito", f"{cantidad} de '{nombre}' eliminado correctamente.")
        self.actualizar_lista()

class ClienteWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Añadir Cliente")
        self.geometry("250x200")
        self.configure(bg="azure")
        self.resizable(False,False)
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
        nombre = self.entry_nombre.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()

        if validar_producto(nombre, "Nombre") and validar_dir(direccion, "Dirección") and validar_tel(telefono, "Teléfono"):
            cliente = Cliente(nombre, direccion, telefono)
            babilon.agregar_cliente(cliente)  # Añadir el producto a la lista
            # Mostrar un messagebox con la información del producto creado
            messagebox.showinfo("Éxito", f"Cliente creado:\nNombre: {cliente.nombre}\nDirección: {cliente.direccion}\nTeléfono: {cliente.telefono}")
            self.destroy()  # Cierra la ventana después de crear el producto
            # Actualizar la lista en la ventana de mostrar productos, si está abierta
            if hasattr(self.master, 'mostrar_clientes_window'):
                self.master.mostrar_clientes_window.actualizar_lista()

class EliminarClienteWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Eliminar Cliente")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False,False)
        self.clientes=babilon.getClientes()
        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para seleccionar el producto a eliminar
        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Dirección", "Teléfono"), show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Dirección", text="Dirección")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Dirección", width=50, anchor="w")
        self.tree.column("Teléfono", width=70, anchor="e")

        # Botón para eliminar el producto seleccionado
        boton_eliminar = tk.Button(contenedor, text="Eliminar Cliente", command=self.eliminar_cliente)
        boton_eliminar.pack(pady=10)

        # Rellenar el Treeview con los productos
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
        babilon.setClientes(self.clientes)
        messagebox.showinfo("Éxito", f"Cliente '{nombre}' eliminado correctamente.")
        self.actualizar_lista()

class MostrarClientesWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Clientes")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False,False)
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
        self.clientes=babilon.getClientes()
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

def salir():
    serializar(babilon)
    exit()

def abrir_ventana_clientes():
    ClienteWindow(root)

def abrir_ventana_mostrar_clientes():
    global mostrar_clientes_window
    mostrar_clientes_window = MostrarClientesWindow(root)

def abrir_ventana_eliminar_clientes():
    EliminarClienteWindow(root)

# Función para abrir la ventana Toplevel (Crear Producto)
def abrir_ventana_producto():
    ProductoWindow(root)

# Función para abrir la ventana Toplevel (Mostrar Productos)
def abrir_ventana_mostrar_productos():
    global mostrar_productos_window
    mostrar_productos_window = MostrarProductosWindow(root)

# Función para abrir la ventana Toplevel (Eliminar Producto)
def abrir_ventana_eliminar_producto():
    EliminarProductoWindow(root)

def hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    root.after(1000,hora)

babilon=deserializar()
clientes=babilon.getClientes()
inventario=babilon.getInventario()

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("babilon.ico.ico")
    root.title("Babiloon Shoes")
    root.geometry("750x500")
    root.resizable(False,False)
    frame1=tk.Frame(root,padx=10,pady=20,bd=1,relief="solid")
    frame2=tk.Frame(root,padx=10,pady=20,bd=1,relief="solid")

    frame1.grid(row=1, column=0, sticky="nsew")
    frame1.pack_propagate(False)
    frame2.grid(row=1,column=1,sticky="nsew")
    frame2.pack_propagate(False)

    etiqueta=tk.Label(frame1,text="Hora")
    hora()

    boton_func1=tk.Button(frame1,text="Añadir Cliente",command=abrir_ventana_clientes)
    boton_func2=tk.Button(frame1,text="Eliminar Cliente",command=abrir_ventana_eliminar_clientes)
    boton_func3=tk.Button(frame1,text="Consultar Clientes",command=abrir_ventana_mostrar_clientes)
    boton_func4=tk.Button(frame1,text="Añadir Producto",command=abrir_ventana_producto)
    boton_func5=tk.Button(frame1,text="Eliminar Producto",command=abrir_ventana_eliminar_producto)
    boton_func6=tk.Button(frame1,text="Consultar Inventario",command=abrir_ventana_mostrar_productos)
    boton_salir=tk.Button(frame1,text="Salir",command=salir)

    etiqueta.grid(row=0,column=0,padx=0,pady=10,sticky="nsew")
    boton_func1.grid(row=1,column=0,padx=0,pady=10,sticky="nsew")
    boton_func2.grid(row=2,column=0,padx=0,pady=10,sticky="nsew")
    boton_func3.grid(row=3,column=0,padx=0,pady=10,sticky="nsew")
    boton_func4.grid(row=4,column=0,padx=0,pady=10,sticky="nsew")
    boton_func5.grid(row=5,column=0,padx=0,pady=10,sticky="nsew")
    boton_func6.grid(row=6,column=0,padx=0,pady=10,sticky="nsew")
    boton_salir.grid(row=7,column=0,padx=0,pady=10,sticky="nsew")

    frame1.configure(width=200,height=500,bg="azure",bd=5)
    frame2.configure(width=670,height=500,bg="light blue",bd=5)
    root.mainloop()