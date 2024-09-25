import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class HistorialCliente(tk.Toplevel):
    def __init__(self, parent, cliente_id, pedidos):
        super().__init__(parent)
        self.title(f"Historial de Pedidos - Cliente {cliente_id}")
        self.geometry("600x400")

        # Crear el TreeView
        self.tree = ttk.Treeview(self, columns=("ID", "Fecha", "Producto", "Valor", "Localidad"), show='headings')
        self.tree.heading("ID", text="Número de Pedido")
        self.tree.heading("Fecha", text="Fecha de Venta")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("Valor", text="Valor Total")
        self.tree.heading("Localidad", text="Local/Nacional")

        self.tree.column("ID", width=100, anchor=tk.CENTER)
        self.tree.column("Fecha", width=120, anchor=tk.CENTER)
        self.tree.column("Producto", width=150, anchor=tk.CENTER)
        self.tree.column("Valor", width=100, anchor=tk.CENTER)
        self.tree.column("Localidad", width=100, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Agregar los pedidos al TreeView
        for pedido in pedidos:
            self.tree.insert("", tk.END, values=(
                pedido.numero,  # Usar el atributo correcto
                pedido.fecha,
                pedido.producto.nombre,
                pedido.valor_total,
                'Local' if pedido.cliente.direccion == 'Medellín' else 'Nacional'  # Cambia esto según tu lógica para definir localidad
            ))



