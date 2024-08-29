import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from enum import Enum
import time

# Definir Enums
class Tipo(Enum):
    Tennis = "Tennis"
    Bota = "Bota"
    Sandalia = "Sandalia"

class Tipo2(Enum):
    Aceptado = "Aceptado"
    Cancelado = "Cancelado"
    Devuelto = "Devuelto"

# Clases de datos
class Producto:
    def __init__(self, nombre, talla, precio, tipo):
        self.nombre = nombre
        self.talla = talla
        self.precio = precio
        self.tipo = tipo

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
    def __init__(self, nombre="Babiloon", clientes=[], inventario=[]):
        self.nombre = nombre
        self.clientes = clientes
        self.inventario = inventario

    def getClientes(self):
        return self.clientes

    def getInventario(self):
        return self.inventario

# Lista global para productos
productos = []

# Funciones de validación
def validar_num(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")

        if ' ' in entry_text:
            raise ValueError(f"El campo '{nombre_campo}' no debe contener espacios.")

        if '.' in entry_text:
            raise ValueError(f"El campo '{nombre_campo}' no debe contener decimales.")

        if any(c in "!@#$%^&*()_+=-{}[]|\:;<>,?/'\"" for c in entry_text):
            raise ValueError(f"El campo '{nombre_campo}' no debe contener símbolos.")

        numero = int(entry_text)

        if numero < 0:
            raise ValueError(f"El campo '{nombre_campo}' no puede ser negativo.")

        return True
    except ValueError as e:
        messagebox.showerror("Error", f"Manejo de errores de la Aplicación:\n{str(e)}")
        return False

def validar_string(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")

        if ' ' in entry_text:
            raise ValueError(f"El campo '{nombre_campo}' no debe contener espacios.")

        if not entry_text.isalpha():
            raise ValueError(f"El campo '{nombre_campo}' solo debe contener letras.")

        return True
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_producto(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")
        
        if any(c in "!@#$%^&*()_+=-{}[]|\:;<>,?/'\"" for c in entry_text):
            raise ValueError(f"El campo '{nombre_campo}' no debe contener símbolos.")

        return True
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return False

# Funciones para manejar productos
def crear_producto():
    nombre = entry_nombre.get()
    talla = entry_talla.get()
    precio = entry_precio.get()
    tipo = tipo_var.get()

    if validar_producto(nombre, "Nombre") and validar_num(talla, "Talla") and validar_num(precio, "Precio") and tipo:
        producto = Producto(nombre, talla, float(precio), Tipo(tipo))
        productos.append(producto)
        messagebox.showinfo("Éxito", f"Producto creado:\nNombre: {producto.nombre}\nTalla: {producto.talla}\nPrecio: {producto.precio}\nTipo: {producto.tipo.value}")
        ventana_producto.destroy()
        if hasattr(ventana_mostrar_productos, 'actualizar_lista'):
            ventana_mostrar_productos.actualizar_lista()

def mostrar_productos():
    global ventana_mostrar_productos
    ventana_mostrar_productos = tk.Toplevel(root)
    ventana_mostrar_productos.title("Productos")
    ventana_mostrar_productos.geometry("400x300")
    
    contenedor = tk.Frame(ventana_mostrar_productos)
    contenedor.pack(expand=True, fill='both')

    tree = ttk.Treeview(contenedor, columns=("Nombre", "Talla", "Precio", "Tipo"), show='headings')
    tree.heading("Nombre", text="Nombre")
    tree.heading("Talla", text="Talla")
    tree.heading("Precio", text="Precio")
    tree.heading("Tipo", text="Tipo")
    tree.pack(expand=True, fill='both')

    tree.column("Nombre", width=100, anchor="w")
    tree.column("Talla", width=50, anchor="w")
    tree.column("Precio", width=70, anchor="e")
    tree.column("Tipo", width=80, anchor="w")

    for producto in productos:
        tree.insert("", "end", values=(producto.nombre, producto.talla, producto.precio, producto.tipo.value))

    def actualizar_lista():
        for item in tree.get_children():
            tree.delete(item)
        for producto in productos:
            tree.insert("", "end", values=(producto.nombre, producto.talla, producto.precio, producto.tipo.value))

    ventana_mostrar_productos.actualizar_lista = actualizar_lista

def eliminar_producto():
    global ventana_eliminar_producto
    ventana_eliminar_producto = tk.Toplevel(root)
    ventana_eliminar_producto.title("Eliminar Producto")
    ventana_eliminar_producto.geometry("400x300")
    
    contenedor = tk.Frame(ventana_eliminar_producto)
    contenedor.pack(expand=True, fill='both')

    tree = ttk.Treeview(contenedor, columns=("Nombre", "Talla", "Precio", "Tipo"), show='headings')
    tree.heading("Nombre", text="Nombre")
    tree.heading("Talla", text="Talla")
    tree.heading("Precio", text="Precio")
    tree.heading("Tipo", text="Tipo")
    tree.pack(expand=True, fill='both')

    tree.column("Nombre", width=100, anchor="w")
    tree.column("Talla", width=50, anchor="w")
    tree.column("Precio", width=70, anchor="e")
    tree.column("Tipo", width=80, anchor="w")

    for producto in productos:
        tree.insert("", "end", iid=producto.nombre, values=(producto.nombre, producto.talla, producto.precio, producto.tipo.value))

    def eliminar_producto_seleccionado():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para eliminar.")
            return

        item_values = tree.item(selected_item[0])['values']
        nombre = item_values[0]
        
        global productos
        productos = [p for p in productos if p.nombre != nombre]

        messagebox.showinfo("Éxito", f"Producto '{nombre}' eliminado correctamente.")
        tree.delete(selected_item[0])

    boton_eliminar = tk.Button(contenedor, text="Eliminar Producto", command=eliminar_producto_seleccionado)
    boton_eliminar.pack(pady=10)

# Funciones de interfaz principal
def abrir_func1():
    global ventana_producto
    ventana_producto = tk.Toplevel(root)
    ventana_producto.title("Crear Producto")
    ventana_producto.geometry("300x200")

    contenedor = tk.Frame(ventana_producto)
    contenedor.pack(expand=True, fill='both')

    tk.Label(contenedor, text="Nombre").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    global entry_nombre
    entry_nombre = tk.Entry(contenedor, width=20)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    tk.Label(contenedor, text="Talla").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    global entry_talla
    entry_talla = tk.Entry(contenedor, width=20)
    entry_talla.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    tk.Label(contenedor, text="Precio").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    global entry_precio
    entry_precio = tk.Entry(contenedor, width=20)
    entry_precio.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    tk.Label(contenedor, text="Tipo").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    global tipo_var
    tipo_var = tk.StringVar()
    tipo_var.set(Tipo.Tennis.value)
    tk.OptionMenu(contenedor, tipo_var, *[t.value for t in Tipo]).grid(row=3, column=1, padx=10, pady=5, sticky="w")

    tk.Button(contenedor, text="Crear Producto", command=crear_producto).grid(row=4, columnspan=2, pady=10)

def abrir_func2():
    mostrar_productos()

def abrir_func3():
    eliminar_producto()

def salir():
    root.quit()

def hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, hora)

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("babilon.ico.ico")
    root.title("Babiloon Shoes")
    root.geometry("750x500")
    root.resizable(False, False)

    frame1 = tk.Frame(root, padx=10, pady=20, bd=1, relief="solid")
    frame2 = tk.Frame(root, padx=10, pady=20, bd=1, relief="solid")

    frame1.grid(row=1, column=0, sticky="nsew")
    frame1.pack_propagate(False)
    frame2.grid(row=1, column=1, sticky="nsew")
    frame2.pack_propagate(False)

    etiqueta = tk.Label(frame1, text="Hora")
    hora()

    boton_func1 = tk.Button(frame1, text="Crear Producto", command=abrir_func1)
    boton_func2 = tk.Button(frame1, text="Mostrar Productos", command=abrir_func2)
    boton_func3 = tk.Button(frame1, text="Eliminar Producto", command=abrir_func3)
    boton_salir = tk.Button(frame1, text="Salir", command=salir)

    etiqueta.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")
    boton_func1.grid(row=1, column=0, padx=0, pady=10, sticky="nsew")
    boton_func2.grid(row=2, column=0, padx=0, pady=10, sticky="nsew")
    boton_func3.grid(row=3, column=0, padx=0, pady=10, sticky="nsew")
    boton_salir.grid(row=4, column=0, padx=0, pady=10, sticky="nsew")

    frame1.configure(width=200, height=500, bg="azure", bd=5)
    frame2.configure(width=670, height=500, bg="light blue", bd=5)
    root.mainloop()
