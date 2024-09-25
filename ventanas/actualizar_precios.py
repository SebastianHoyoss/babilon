import tkinter as tk
from tkinter import ttk, messagebox

class ActualizarPreciosWindow(tk.Toplevel):
    def __init__(self, master=None, inventario=[], producto_id=None):
        super().__init__(master)
        self.title("Actualizar Precio de Producto")
        self.geometry("300x200")
        self.configure(bg="azure")
        self.resizable(False, False)

        self.inventario = inventario
        self.producto_id = producto_id  # Guardar la ID del producto

        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')
        # Crear la interfaz
        self.label = tk.Label(contenedor, text=f"Actualizar Precio para ID: {self.producto_id}")
        self.label.pack(pady=10)

        self.precio_entry = tk.Entry(contenedor)
        self.precio_entry.pack(pady=10)

        self.save_button = tk.Button(contenedor, text="Guardar Cambios", command=self.guardar_cambios)
        self.save_button.pack(pady=10)

        # Pre-cargar el precio actual
        self.cargar_precio_actual()

    def cargar_precio_actual(self):
        for producto in self.inventario:
            if producto.id == self.producto_id:  # Comparar por ID
                self.precio_entry.insert(0, str(producto.precio))
                break

    def guardar_cambios(self):
        nuevo_precio = self.precio_entry.get()
        try:
            nuevo_precio = float(nuevo_precio)
            for producto in self.inventario:
                if producto.id == self.producto_id:  # Comparar por ID
                    # Preguntar confirmación
                    confirmacion = messagebox.askyesno("Confirmar Cambios", 
                        f"¿Está seguro de que desea actualizar el precio a {nuevo_precio}?")
                    
                    if confirmacion:  # Si el usuario confirma
                        producto.precio = nuevo_precio
                        messagebox.showinfo("Éxito", "Precio actualizado correctamente.")
                    self.destroy()  # Cerrar la ventana
                    break
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un precio válido.")
