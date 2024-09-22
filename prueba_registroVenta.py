import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
# Crear ventana principal
root = tk.Tk()
root.title("Registro de Pedidos")

# Variables para almacenar datos
pedido_var = tk.StringVar()
fecha_var = tk.StringVar()
cliente_var = tk.StringVar()
nombre_var = tk.StringVar()
telefono_var = tk.StringVar()
direccion_cll_var = tk.StringVar()
direccion_cra_var = tk.StringVar()
direccion_no_var = tk.StringVar()
zona_var = tk.StringVar()
producto_var = tk.StringVar()
precio_var = tk.StringVar()
cantidad_var = tk.StringVar()
observacion_var = tk.StringVar()

clientes = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5"]
productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]
# Función de ejemplo para agregar detalle de pedido
def agregar_detalle():
    print(f"Pedido agregado: {pedido_var.get()}, Producto: {producto_var.get()}")

# Crear etiquetas y campos de entrada
tk.Label(root, text="Pedido:").grid(row=0, column=0,sticky='nsew')
tk.Entry(root, textvariable=pedido_var).grid(row=0, column=1,sticky='nsew')

tk.Label(root, text="Fecha:").grid(row=0, column=2,sticky='nsew')
calendario = DateEntry(root, textvariable=fecha_var, date_pattern='dd/mm/yyyy', width=15)
calendario.grid(row=0, column=3)

tk.Label(root, text="Cliente:").grid(row=1, column=0,sticky='nsew')
combobox_cliente = ttk.Combobox(root, textvariable=cliente_var, values=clientes).grid(row=1, column=1,sticky='nsew')

tk.Label(root, text="Nombre:").grid(row=2, column=0,sticky='nsew')
tk.Entry(root, textvariable=nombre_var).grid(row=2, column=1,sticky='nsew')

tk.Label(root, text="Teléfono:").grid(row=3, column=0,sticky='nsew')
tk.Entry(root, textvariable=telefono_var).grid(row=3, column=1,sticky='nsew')

tk.Label(root, text="Dirección:").grid(row=4, column=0,sticky='nsew')
tk.Entry(root, textvariable=direccion_cll_var, width=5).grid(row=4, column=1, sticky='nsew')

# Botón para agregar detalles del pedido
tk.Button(root, text="Agregar Detalle Pedido", command=agregar_detalle).grid(row=6, column=0, columnspan=2,sticky='nsew')

# Sección de detalles del pedido
tk.Label(root, text="Producto:").grid(row=7, column=0,sticky='nsew')
combobox_producto = ttk.Combobox(root, textvariable=producto_var, values=productos).grid(row=7, column=1,sticky='nsew')

tk.Label(root, text="Precio Lista:").grid(row=8, column=0,sticky='nsew')
tk.Entry(root, textvariable=precio_var).grid(row=8, column=1,sticky='nsew')

tk.Label(root, text="Cantidad:").grid(row=9, column=0,sticky='nsew')
tk.Entry(root, textvariable=cantidad_var).grid(row=9, column=1,sticky='nsew')

tk.Label(root, text="Observación:").grid(row=10, column=0,sticky='nsew')
tk.Entry(root, textvariable=observacion_var).grid(row=10, column=1,sticky='nsew')

# Botones de aceptar y cancelar
tk.Button(root, text="Aceptar", command=root.quit).grid(row=11, column=1,sticky='nsew')
tk.Button(root, text="Cancelar", command=root.quit).grid(row=11, column=2,sticky='nsew')

# Iniciar la aplicación
root.mainloop()
