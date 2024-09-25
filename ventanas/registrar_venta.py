import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class RegistrarVentaWindow(tk.Frame):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.babilon = babilon
        self.clientes = self.babilon.getClientes()
        self.productos = self.babilon.getInventario()
        self.master = master
        
        # Establecer un color de fondo
        self.config(bg="#f0f0f0")
        self.master.config(bg="#f0f0f0")

        # Establecer un tamaño mínimo para el frame
        self.update_idletasks()  
        self.pack_propagate(False)  
        self.config(width=400, height=300) 
        
        tk.Label(self, text="Registro de Ventas", bg="#f0f0f0", font=("Arial", 16)).grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

        # Variables para almacenar datos
        pedido_var = tk.StringVar()
        fecha_var = tk.StringVar()
        nombre_var = tk.StringVar()
        telefono_var = tk.StringVar()
        direccion_cll_var = tk.StringVar()
        producto_var = tk.StringVar()
        precio_var = tk.StringVar()
        cantidad_var = tk.StringVar()
        ciudad_var = tk.StringVar()

        def seleccionar_cliente(event):
            cliente_seleccionado = combobox_cliente.get()
            for cliente in self.clientes:
                if cliente.nombre == cliente_seleccionado:
                    nombre_var.set(cliente.nombre)
                    direccion_cll_var.set(cliente.direccion)
                    telefono_var.set(cliente.telefono)

        def seleccionar_producto(event):
            producto_seleccionado = combobox_producto.get()
            for producto in self.productos:
                if producto.nombre == producto_seleccionado:
                    precio_var.set(producto.precio)

        def agregar_pedido():
            # Lógica para agregar pedido
            self.destroy()

        # Crear etiquetas y campos de entrada con espacio
        tk.Label(self, text="Pedido:").grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        tk.Entry(self, textvariable=pedido_var).grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

        tk.Label(self, text="Fecha:").grid(row=1, column=2, sticky='nsew', padx=5, pady=5)
        calendario = DateEntry(self, textvariable=fecha_var, date_pattern='dd/mm/yyyy', width=15)
        calendario.grid(row=1, column=3, sticky='nsew', padx=5, pady=5)

        tk.Label(self, text="Cliente:").grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
        combobox_cliente = ttk.Combobox(self, values=[cliente.nombre for cliente in self.clientes])
        combobox_cliente.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)
        combobox_cliente.bind("<<ComboboxSelected>>", seleccionar_cliente)

        tk.Label(self, text="Nombre:").grid(row=3, column=0, sticky='nsew', padx=5, pady=5)
        tk.Entry(self, textvariable=nombre_var).grid(row=3, column=1, sticky='nsew', padx=5, pady=5)

        tk.Label(self, text="Teléfono:").grid(row=4, column=0, sticky='nsew', padx=5, pady=5)
        tk.Entry(self, textvariable=telefono_var).grid(row=4, column=1, sticky='nsew', padx=5, pady=5)

        tk.Label(self, text="Dirección:").grid(row=5, column=0, sticky='nsew', padx=5, pady=5)
        tk.Entry(self, textvariable=direccion_cll_var).grid(row=5, column=1, sticky='nsew', padx=5, pady=5)

        tk.Label(self, text="Ciudad:").grid(row=6, column=0, sticky='nsew', padx=5, pady=5)
        tk.Entry(self, textvariable=ciudad_var).grid(row=6, column=1, sticky='nsew', padx=5, pady=5)

        # Sección de detalles del pedido
        tk.Label(self, text="Producto:").grid(row=7, column=0, sticky='nsew', padx=5, pady=5)
        combobox_producto = ttk.Combobox(self, textvariable=producto_var, values=[producto.nombre for producto in self.productos])
        combobox_producto.grid(row=7, column=1, sticky='nsew', padx=5, pady=5)
        combobox_producto.bind("<<ComboboxSelected>>", seleccionar_producto)

        tk.Label(self, text="Precio:").grid(row=8, column=0, sticky='nsew', padx=5, pady=5)
        tk.Entry(self, textvariable=precio_var).grid(row=8, column=1, sticky='nsew', padx=5, pady=5)

        tk.Label(self, text="Cantidad:").grid(row=9, column=0, sticky='nsew', padx=5, pady=5)
        tk.Entry(self, textvariable=cantidad_var).grid(row=9, column=1, sticky='nsew', padx=5, pady=5)

        # Botones de aceptar y cancelar
        tk.Button(self, text="Aceptar", command=agregar_pedido).grid(row=10, column=1, sticky='nsew', padx=5, pady=5)
        tk.Button(self, text="Cancelar", command=self.destroy).grid(row=10, column=2, sticky='nsew', padx=5, pady=5)

        self.pack(fill='both', expand=True)
