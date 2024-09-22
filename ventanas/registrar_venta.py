import tkinter as tk
from tkinter import Label, messagebox, ttk
from src.babilon import Babilon
from src.cliente import Cliente
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *
from tkcalendar import DateEntry

class RegistrarVentaWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.babilon = babilon
        self.clientes = self.babilon.getClientes()
        self.productos = self.babilon.getInventario()
        self.master = master
        self.title("Registrar Venta")
        self.geometry("700x500")

        #variables para almacenar datos
        pedido_var=tk.StringVar()
        fecha_var=tk.StringVar()
        cliente_var=tk.StringVar()
        nombre_var=tk.StringVar()
        telefono_var=tk.StringVar()
        direccion_cll_var=tk.StringVar()
        producto_var=tk.StringVar()
        precio_var=tk.StringVar()
        cantidad_var=tk.StringVar()
        observacion_var=tk.StringVar()

        self.title("Registro de Pedidos")
        def seleccionar_cliente(event):
            cliente_seleccionado = combobox_cliente.get()
            for cliente in self.clientes:
                 if cliente.nombre == cliente_seleccionado:
                    nombre_var.set(cliente.nombre)
                    direccion_cll_var.set(cliente.direccion)
                    telefono_var.set(cliente.telefono)

        def seleccionar_prodcuto(event):
            producto_seleccionado = combobox_producto.get()
            for producto in self.productos:
                if producto.nombre == producto_seleccionado:
                    precio_var.set(producto.precio)

        def agregar_pedido():
            cliente_seleccionado = combobox_cliente.get()
            for cliente in self.clientes:
                if cliente.nombre == cliente_seleccionado:
                    cliente.agregar_pedido(pedido_var.get())
                    print(f"Pedidos actuales de {cliente.nombre}: {cliente.pedidos}")
        # Función de ejemplo para agregar detalle de pedido
        def agregar_detalle():
            print(f"Pedido agregado: {pedido_var.get()}, Producto: {producto_var.get()}")

        # Crear etiquetas y campos de entrada
        tk.Label(self, text="Pedido:").grid(row=0, column=0,sticky='nsew')
        tk.Entry(self, textvariable=pedido_var).grid(row=0, column=1,sticky='nsew')

        tk.Label(self, text="Fecha:").grid(row=0, column=2,sticky='nsew')
        calendario = DateEntry(self, textvariable=fecha_var, date_pattern='dd/mm/yyyy', width=15)
        calendario.grid(row=0, column=3)

        tk.Label(self, text="Cliente:").grid(row=1, column=0,sticky='nsew')
        combobox_cliente = ttk.Combobox(self, values=[cliente.nombre for cliente in self.clientes])
        combobox_cliente.grid(row=1, column=1,sticky='nsew')
        combobox_cliente.bind("<<ComboboxSelected>>", seleccionar_cliente)

        tk.Label(self, text="Nombre:").grid(row=2, column=0,sticky='nsew')
        tk.Entry(self, textvariable=nombre_var).grid(row=2, column=1,sticky='nsew')

        tk.Label(self, text="Teléfono:").grid(row=3, column=0,sticky='nsew')
        tk.Entry(self, textvariable=telefono_var).grid(row=3, column=1,sticky='nsew')

        tk.Label(self, text="Dirección:").grid(row=4, column=0,sticky='nsew')
        tk.Entry(self, textvariable=direccion_cll_var, width=5).grid(row=4, column=1, sticky='nsew')

        # Botón para agregar detalles del pedido
        tk.Button(self, text="Agregar Detalle Pedido", command=agregar_detalle).grid(row=6, column=0, columnspan=2,sticky='nsew')

        # Sección de detalles del pedido
        tk.Label(self, text="Producto:").grid(row=7, column=0,sticky='nsew')
        combobox_producto = ttk.Combobox(self, textvariable=producto_var, values=[producto.nombre for producto in self.productos])
        combobox_producto.grid(row=7, column=1,sticky='nsew')
        combobox_producto.bind("<<ComboboxSelected>>", seleccionar_prodcuto)

        tk.Label(self, text="Precio Lista:").grid(row=8, column=0,sticky='nsew')
        tk.Entry(self, textvariable=precio_var).grid(row=8, column=1,sticky='nsew')

        tk.Label(self, text="Cantidad:").grid(row=9, column=0,sticky='nsew')
        tk.Entry(self, textvariable=cantidad_var).grid(row=9, column=1,sticky='nsew')

        tk.Label(self, text="Observación:").grid(row=10, column=0,sticky='nsew')
        tk.Entry(self, textvariable=observacion_var).grid(row=10, column=1,sticky='nsew')

        # Botones de aceptar y cancelar
        tk.Button(self, text="Aceptar", command=agregar_pedido).grid(row=11, column=1,sticky='nsew')
        tk.Button(self, text="Cancelar",command=self.destroy).grid(row=11, column=2,sticky='nsew')