#imports
import tkinter as tk
from tkinter import Label, messagebox, ttk
from excepciones.excepciones import *
from src.babilon import Babilon
from src.cliente import Cliente
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *


# Clase para la ventana Toplevel (Crear Producto)
class ProductoWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.title("Añadir Producto")
        self.geometry("250x200")
        self.configure(bg="azure")
        self.resizable(False,False)
        self.babilon = babilon
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
            self.babilon.agregar_producto(producto)  # Añadir el producto a la lista
            # Mostrar un messagebox con la información del producto creado
            messagebox.showinfo("Éxito", f"Producto creado:\nNombre: {producto.nombre}\nTalla: {producto.talla}\nPrecio: {producto.precio}\nTipo: {producto.tipo.value}\nCantidad: {producto.cantidad}")
            self.destroy()  # Cierra la ventana después de crear el producto
            # Actualizar la lista en la ventana de mostrar productos, si está abierta
            if hasattr(self.master, 'mostrar_productos_window'):
                self.master.mostrar_productos_window.actualizar_lista()