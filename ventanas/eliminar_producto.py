import tkinter as tk
from tkinter import Label, messagebox, ttk
from excepciones.excepciones import *
from src.babilon import Babilon
from src.producto import Producto
from src.tipo import Tipo
from excepciones.excepciones import *

# Clase para la ventana Toplevel (Eliminar Producto)
class EliminarProductoWindow(tk.Toplevel):
    def __init__(self, master=None, producto=None, actualizar_producto=None, eliminar_selected=None):
        super().__init__(master)
        self.title("Eliminar Producto")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False, False)
        
        # Centrar la ventana en la pantalla
        self.center_window(400, 300)
        
        self.producto = producto
        self.actualizar_producto = actualizar_producto
        self.eliminar_selected = eliminar_selected
        
        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')
        
        # Campo para el ID
        tk.Label(contenedor, text="ID").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_id = tk.Entry(contenedor, state='normal', width=20) 
        self.entry_id.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        if self.producto.id is not None:  
            self.entry_id.insert(0, self.producto.id)
            self.entry_id.config(state='readonly')

        # Campo para el nombre
        tk.Label(contenedor, text="Producto").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_producto = tk.Entry(contenedor, state='normal', width=20) 
        self.entry_producto.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        if self.producto.nombre is not None:  
            self.entry_producto.insert(0, self.producto.nombre)
            self.entry_producto.config(state='readonly')
        
        tk.Label(contenedor, text="Cantidad actual").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_cantidad = tk.Entry(contenedor, state='normal', width=20) 
        self.entry_cantidad.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        if self.producto.cantidad is not None:  
            self.entry_cantidad.insert(0, self.producto.cantidad)
            self.entry_cantidad.config(state='readonly')
            
        tk.Label(contenedor, text="Cantidad a eliminar").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_cantidad_eliminar = tk.Entry(contenedor, state='normal', width=20) 
        self.entry_cantidad_eliminar.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        
        # Botones
        boton_eliminar = tk.Button(contenedor, text="Eliminar cantidad", command=self.eliminar_parcial)
        boton_eliminar.grid(row=5, columnspan=3, pady=10)
        boton_eliminar = tk.Button(contenedor, text="Eliminar Producto Totalmente", command=self.confirmar_eliminar_total)
        boton_eliminar.grid(row=6, columnspan=3, pady=10)

    def center_window(self, width, height):
        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calcular las coordenadas para centrar la ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Establecer la geometría de la ventana
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def eliminar_parcial(self):
        cantidad_a_eliminar = self.entry_cantidad_eliminar.get()
        if validar_num(cantidad_a_eliminar, "Cantidad a eliminar"):
            cantidad_a_eliminar = int(cantidad_a_eliminar)
            
            if cantidad_a_eliminar > self.producto.cantidad:
                messagebox.showwarning("Advertencia", "No puedes eliminar más de la cantidad actual.")
            else:
                self.producto.cantidad -= cantidad_a_eliminar
                messagebox.showinfo("Éxito", f"Se han eliminado {cantidad_a_eliminar} unidades del producto '{self.producto.nombre}'.")

                if self.producto.cantidad == 0:
                    messagebox.showinfo("Info", "El producto ahora tiene 0 en stock, pero no se eliminará de la lista.")
                    
                self.actualizar_producto()  # Refrescar la tabla principal
                self.destroy()
    
    def confirmar_eliminar_total(self):
        # Mostrar un mensaje de confirmación
        respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar este producto completamente?")
        if respuesta:
            self.eliminar_total()

    def eliminar_total(self):
        # Aquí se eliminará el producto completamente
        self.eliminar_selected(self.producto)
        messagebox.showinfo("Eliminado", f"El producto '{self.producto.nombre}' ha sido eliminado completamente.")
        self.actualizar_producto()  # Refrescar la tabla principal
        self.destroy()
