import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from enum import Enum
from excepciones import *

# Definir las clases y enums
class Tipo(Enum):
    Tennis = "Tennis"
    Bota = "Bota"
    Sandalia = "Sandalia"

class Producto:
    def __init__(self, nombre, talla, precio, tipo):
        self.nombre = nombre
        self.talla = talla
        self.precio = precio
        self.tipo = tipo

# Lista para almacenar los productos creados
productos = []

# Funciones de validación
def validar_num(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)

        if ' ' in entry_text:
            raise SinEspacios(nombre_campo)

        if '.' in entry_text:
            raise NoUsarDecimales(nombre_campo)

        if any(c in "!@#$%^&*()_+=-{}[]|\:;<>,?/'\"" for c in entry_text):
            raise NoUsarSimbolos(nombre_campo)

        numero = int(entry_text)

        if numero < 0:
            raise NoUsarNegativos(nombre_campo)

        return True
    except ValueError:
        messagebox.showerror("Error", f"Manejo de errores de la Aplicación:\nEl dato en el campo '{nombre_campo}' debe ser un número.")
        return False
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_string(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)

        if ' ' in entry_text:
            raise SinEspacios(nombre_campo)

        if not entry_text.isalpha():
            raise SoloLetras(nombre_campo)

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_nombre(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)

        if not entry_text.isalpha():
            raise SoloLetras(nombre_campo)
        
        if any(c in "!@#$%^&*()_+=-{}[]|\:;<>,?/'\"" for c in entry_text):
            raise NoUsarSimbolos(nombre_campo)

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_producto(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)
        
        if any(c in "!@#$%^&*()_+=-{}[]|\:;<>,?/'\"" for c in entry_text):
            raise NoUsarSimbolos(nombre_campo)

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

# Clase para la ventana Toplevel (Crear Producto)
class ProductoWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Crear Producto")
        self.geometry("300x200")
        
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

        # Botón para crear el producto
        boton_crear = tk.Button(contenedor, text="Crear Producto", command=self.crear_producto)
        boton_crear.grid(row=4, columnspan=2, pady=10)

    def crear_producto(self):
        nombre = self.entry_nombre.get()
        talla = self.entry_talla.get()
        precio = self.entry_precio.get()
        tipo = self.tipo_var.get()

        if validar_producto(nombre, "Nombre") and validar_num(talla, "Talla") and validar_num(precio, "Precio") and tipo:
            producto = Producto(nombre, talla, float(precio), Tipo(tipo))
            productos.append(producto)  # Añadir el producto a la lista
            # Mostrar un messagebox con la información del producto creado
            messagebox.showinfo("Éxito", f"Producto creado:\nNombre: {producto.nombre}\nTalla: {producto.talla}\nPrecio: {producto.precio}\nTipo: {producto.tipo.value}")
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

        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para mostrar los productos
        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Talla", "Precio", "Tipo"), show='headings')
        self.tree.heading("Nombre", text="Nombre", command=lambda: self.ordenar_columnas("Nombre"))
        self.tree.heading("Talla", text="Talla", command=lambda: self.ordenar_columnas("Talla"))
        self.tree.heading("Precio", text="Precio", command=lambda: self.ordenar_columnas("Precio"))
        self.tree.heading("Tipo", text="Tipo", command=lambda: self.ordenar_columnas("Tipo"))
        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Talla", width=50, anchor="w")
        self.tree.column("Precio", width=70, anchor="e")
        self.tree.column("Tipo", width=80, anchor="w")

        # Rellenar el Treeview con los productos
        self.actualizar_lista()
        
        # Actualizar la lista cada segundo
        self.actualizar_periodicamente()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Añadir los productos a la vista
        for producto in productos:
            self.tree.insert("", "end", values=(producto.nombre, producto.talla, producto.precio, producto.tipo.value))

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

        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        # Crear una Treeview para seleccionar el producto a eliminar
        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Talla", "Precio", "Tipo"), show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Talla", text="Talla")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.pack(expand=True, fill='both')

        # Configurar el ancho de las columnas
        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Talla", width=50, anchor="w")
        self.tree.column("Precio", width=70, anchor="e")
        self.tree.column("Tipo", width=80, anchor="w")

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
        for producto in productos:
            self.tree.insert("", "end", iid=producto.nombre, values=(producto.nombre, producto.talla, producto.precio, producto.tipo.value))

    def eliminar_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para eliminar.")
            return

        item_values = self.tree.item(selected_item[0])['values']
        nombre = item_values[0]
        
        # Buscar y eliminar el producto
        global productos
        productos = [p for p in productos if p.nombre != nombre]

        messagebox.showinfo("Éxito", f"Producto '{nombre}' eliminado correctamente.")
        self.actualizar_lista()

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

# Configurar la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("400x200")

# Botón en la ventana principal para crear un producto
boton_abrir = tk.Button(root, text="Crear Producto", command=abrir_ventana_producto)
boton_abrir.pack(pady=10)

# Botón en la ventana principal para mostrar productos
boton_mostrar = tk.Button(root, text="Mostrar Productos", command=abrir_ventana_mostrar_productos)
boton_mostrar.pack(pady=10)

# Botón en la ventana principal para eliminar un producto
boton_eliminar = tk.Button(root, text="Eliminar Producto", command=abrir_ventana_eliminar_producto)
boton_eliminar.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
