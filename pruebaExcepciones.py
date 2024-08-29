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
        messagebox.showerror("Error", "Manejo de errores de la Aplicación:\nEl dato en el campo '{self.nombre_campo}' debe ser un número.")
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

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_producto(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False
# Clase para la ventana Toplevel
class ProductoWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Crear Producto")
        self.geometry("300x200")
        
        # Campo para el nombre
        tk.Label(self, text="Nombre").grid(row=0, column=0, padx=10)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=0, column=1)

        # Campo para la talla
        tk.Label(self, text="Talla").grid(row=1, column=0, padx=10)
        self.entry_talla = tk.Entry(self)
        self.entry_talla.grid(row=1, column=1)

        # Campo para el precio
        tk.Label(self, text="Precio").grid(row=2, column=0, padx=10)
        self.entry_precio = tk.Entry(self)
        self.entry_precio.grid(row=2, column=1)

        # Menú desplegable para el tipo de producto
        tk.Label(self, text="Tipo").grid(row=3, column=0, padx=10)
        self.tipo_var = tk.StringVar()
        self.combo_tipo = ttk.Combobox(self, textvariable=self.tipo_var)
        self.combo_tipo['values'] = [tipo.value for tipo in Tipo]
        self.combo_tipo.grid(row=3, column=1, padx=(19,0))

        # Botón para crear el producto
        boton_crear = tk.Button(self, text="Crear Producto", command=self.crear_producto)
        boton_crear.grid(row=4, columnspan=2)

    def crear_producto(self):
        nombre = self.entry_nombre.get()
        talla = self.entry_talla.get()
        precio = self.entry_precio.get()
        tipo = self.tipo_var.get()

        if validar_producto(nombre, "Nombre") and validar_num(talla, "Talla") and validar_num(precio, "Precio") and tipo:
            producto = Producto(nombre, talla, float(precio), Tipo(tipo))
            print(f"Producto creado: {vars(producto)}")
            self.destroy()  # Cierra la ventana después de crear el producto

# Función para abrir la ventana Toplevel
def abrir_ventana_producto():
    ProductoWindow(root)

# Configurar la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("300x100")

# Botón en la ventana principal para abrir la ventana Toplevel
boton_abrir = tk.Button(root, text="Crear Producto", command=abrir_ventana_producto)
boton_abrir.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
