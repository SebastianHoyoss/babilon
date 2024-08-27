from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from enum import Enum

class Tipo(Enum):
    Tennis = "Tennis"
    Bota = "Bota"
    Sandalia = "Sandalia"

class Tipo2(Enum):
    Aceptado = "Aceptado"
    Cancelado = "Cancelado"
    Devuelto = "Devuelto"

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

class AdministradorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Administración")
        
        # Crear datos ficticios para clientes y productos
        self.clientes = [Cliente("Juan Pérez", "Calle 123", "555-1234"),
                         Cliente("Maria Lopez", "Avenida 45", "555-5678")]
        
        self.productos = [Producto("Tennis", "M", 50.00, Tipo.Tennis),
                          Producto("Bota", "L", 75.00, Tipo.Bota)]
        
        # Crear las funcionalidades
        self.create_buttons()
        
    def create_buttons(self):
        # Botones para las funcionalidades
        btn_registro_ventas = tk.Button(self.root, text="Registro de Ventas", command=self.registrar_ventas)
        btn_registro_ventas.pack(pady=10)

        btn_generar_reportes = tk.Button(self.root, text="Generar Reportes", command=self.generar_reportes)
        btn_generar_reportes.pack(pady=10)

        btn_consulta_historial = tk.Button(self.root, text="Consultar Historial de Cliente", command=self.consultar_historial)
        btn_consulta_historial.pack(pady=10)

        btn_visualizacion_inventario = tk.Button(self.root, text="Visualización de Inventario", command=self.visualizar_inventario)
        btn_visualizacion_inventario.pack(pady=10)

        btn_actualizacion_inventario = tk.Button(self.root, text="Actualización de Inventario", command=self.actualizar_inventario)
        btn_actualizacion_inventario.pack(pady=10)

    # Funcionalidades
    def registrar_ventas(self):
        # Código para el registro de ventas
        venta_window = tk.Toplevel(self.root)
        venta_window.title("Registro de Ventas")
        
        # Mostrar los campos para registrar una venta
        tk.Label(venta_window, text="Cliente:").pack()
        clientes_combo = ttk.Combobox(venta_window, values=[c.nombre for c in self.clientes])
        clientes_combo.pack()
        
        tk.Label(venta_window, text="Productos:").pack()
        productos_combo = ttk.Combobox(venta_window, values=[p.nombre for p in self.productos])
        productos_combo.pack()

        tk.Label(venta_window, text="Fecha:").pack()
        fecha_entry = tk.Entry(venta_window)
        fecha_entry.pack()

        tk.Button(venta_window, text="Registrar", command=lambda: self.procesar_venta(clientes_combo.get(), productos_combo.get(), fecha_entry.get())).pack()

    def procesar_venta(self, cliente_nombre, producto_nombre, fecha):
        cliente = next((c for c in self.clientes if c.nombre == cliente_nombre), None)
        producto = next((p for p in self.productos if p.nombre == producto_nombre), None)
        if cliente and producto:
            pedido = Pedido(1, datetime.now(), None, [producto], Tipo2.Aceptado)
            venta = Venta(1, cliente, fecha, pedido, producto.precio)
            cliente.pedidos.append(pedido)
            messagebox.showinfo("Éxito", "Venta registrada exitosamente.")
        else:
            messagebox.showerror("Error", "Datos incorrectos.")

    def generar_reportes(self):
        # Código para generar reportes
        report_window = tk.Toplevel(self.root)
        report_window.title("Generar Reportes")

        tk.Label(report_window, text="Fecha Inicio:").pack()
        fecha_inicio = tk.Entry(report_window)
        fecha_inicio.pack()

        tk.Label(report_window, text="Fecha Final:").pack()
        fecha_final = tk.Entry(report_window)
        fecha_final.pack()

        tk.Button(report_window, text="Generar", command=lambda: self.procesar_reporte(fecha_inicio.get(), fecha_final.get())).pack()

    def procesar_reporte(self, fecha_inicio, fecha_final):
        # Generar el reporte basado en el rango de fechas
        messagebox.showinfo("Reporte", f"Generando reporte desde {fecha_inicio} hasta {fecha_final}.")

    def consultar_historial(self):
        # Código para consultar el historial de clientes
        historial_window = tk.Toplevel(self.root)
        historial_window.title("Consulta de Historial")

        tk.Label(historial_window, text="Seleccione Cliente:").pack()
        clientes_combo = ttk.Combobox(historial_window, values=[c.nombre for c in self.clientes])
        clientes_combo.pack()

        tk.Button(historial_window, text="Consultar", command=lambda: self.mostrar_historial(clientes_combo.get())).pack()

    def mostrar_historial(self, cliente_nombre):
        cliente = next((c for c in self.clientes if c.nombre == cliente_nombre), None)
        if cliente:
            pedidos_info = "\n".join([f"Pedido {p.numero}: {p.estado.name}" for p in cliente.pedidos])
            messagebox.showinfo("Historial", pedidos_info)
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

    def visualizar_inventario(self):
        # Código para visualizar el inventario
        inventario_window = tk.Toplevel(self.root)
        inventario_window.title("Visualización de Inventario")

        inventario_info = "\n".join([f"{p.nombre} - {p.tipo.name} - {p.precio}" for p in self.productos])
        tk.Label(inventario_window, text=inventario_info).pack()

    def actualizar_inventario(self):
        # Código para actualizar el inventario
        update_window = tk.Toplevel(self.root)
        update_window.title("Actualizar Inventario")

        tk.Label(update_window, text="Producto:").pack()
        productos_combo = ttk.Combobox(update_window, values=[p.nombre for p in self.productos])
        productos_combo.pack()

        tk.Label(update_window, text="Nuevo Precio:").pack()
        nuevo_precio = tk.Entry(update_window)
        nuevo_precio.pack()

        tk.Button(update_window, text="Actualizar", command=lambda: self.procesar_actualizacion(productos_combo.get(), nuevo_precio.get())).pack()

    def procesar_actualizacion(self, producto_nombre, nuevo_precio):
        producto = next((p for p in self.productos if p.nombre == producto_nombre), None)
        if producto:
            producto.precio = float(nuevo_precio)
            messagebox.showinfo("Éxito", "Inventario actualizado.")
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdministradorApp(root)
    root.mainloop()
