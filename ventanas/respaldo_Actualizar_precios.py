import tkinter as tk
from tkinter import ttk, messagebox

class actualizarPreciosWindow(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.title("Productos")
        self.geometry("400x400")
        self.configure(bg="azure")
        self.resizable(False, False)
        self.babilon = babilon

        # Diccionario para guardar los cambios
        self.modified_prices = {}

        # Crear el Frame que se centrará en la ventana
        contenedor = tk.Frame(self)
        contenedor.pack(expand=True, fill='both')

        self.tree = ttk.Treeview(contenedor, columns=("Nombre", "Precio", "Tipo"), show='headings')
        self.tree.heading("Nombre", text="Nombre", command=lambda: self.ordenar_columnas("Nombre"))
        self.tree.heading("Precio", text="Precio", command=lambda: self.ordenar_columnas("Precio"))
        self.tree.heading("Tipo", text="Tipo", command=lambda: self.ordenar_columnas("Tipo"))
        self.tree.pack(expand=True, fill='both')

        self.tree.column("Nombre", width=100, anchor="w")
        self.tree.column("Precio", width=70, anchor="e")
        self.tree.column("Tipo", width=80, anchor="w")

        self.tree.bind("<Double-1>", self.edit_price)  #Doble click para editar el precio

        # Boton para aplicar cambios
        self.update_button = tk.Button(self, text="Actualizar Precios", command=self.actualizar_precios)
        self.update_button.pack(pady=10)

        self.actualizar_lista()

    def actualizar_lista(self):
        # Limpiar la vista antes de actualizar
        self.tree.delete(*self.tree.get_children())  # Borra todos los elementos de la tabla

        # Añadir los productos a la vista (tabla)
        inventario = self.babilon.getInventario()
        for producto in inventario:
            self.tree.insert("", "end", values=(producto.nombre, producto.precio, producto.tipo.value))

    def edit_price(self, event):
        # Permite modificar el precio directamente en la celda
        selected_item = self.tree.selection()[0]  
        column_id = self.tree.identify_column(event.x)  
        if column_id == '#2':  # 2 corresponde a la columna de precio
            current_value = self.tree.item(selected_item, 'values')[1]

            self.edit_window = tk.Toplevel(self)
            self.edit_window.title(f'Editar Precio')
            self.edit_window.geometry("300x150")
            entry = tk.Entry(self.edit_window)
            entry.insert(0, current_value) # Insercion del nuevo valor
            entry.pack(pady=10)

            def save_price():
                new_value = entry.get()
                try:
                    new_value = float(new_value) # Validamos que el valor ingresado sea float

                    # Actualizamos los datos
                    current_values = list(self.tree.item(selected_item, 'values'))
                    current_values[1] = new_value  #Actualizacion del precio
                    self.tree.item(selected_item, values=current_values)

                    # Guardamos los nuevos precios en el diccionario
                    self.modified_prices[current_values[0]] = new_value
                    self.edit_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Por favor ingrese un precio válido")

            save_button = tk.Button(self.edit_window, text="Guardar", command=save_price)
            save_button.pack(pady=10)

    def actualizar_precios(self):
        if not self.modified_prices:
            messagebox.showinfo("Info", "No hay cambios de precio que aplicar.")
            return

        # Actualizamos los productos (asumiendo que su nombre es unico)
        for producto in self.babilon.getInventario():
            if producto.nombre in self.modified_prices:
                producto.precio = self.modified_prices[producto.nombre]

        self.modified_prices.clear()

        messagebox.showinfo("Éxito", "Todos los precios han sido actualizados correctamente")
        self.actualizar_lista()
