import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry
class generarBalancesWindows(tk.Toplevel):
    def __init__(self, master=None, babilon=None):
        super().__init__(master)
        self.title("Generar Balances")
        self.geometry("400x300")
        self.configure(bg="azure")
        self.resizable(False, False)
        self.babilon = babilon
        self.fecha_inicio_var = tk.StringVar()
        self.fecha_fin_var = tk.StringVar()
        # Etiquetas y entradas para las fechas
        tk.Label(self, text="Fecha Inicio (Dia/Mes/Año):", bg="azure").pack(pady=5)
        calendarioInicio = DateEntry(self, textvariable=self.fecha_inicio_var, date_pattern='dd/mm/yyyy', width=15)
        calendarioInicio.pack(pady=5)

        tk.Label(self, text="Fecha Fin (Dia/Mes/Año):", bg="azure").pack(pady=5)
        calendarioFin = DateEntry(self, textvariable=self.fecha_fin_var, date_pattern='dd/mm/yyyy', width=15)
        calendarioFin.pack(pady=5)

        # Combobox para seleccionar tipo de venta
        tk.Label(self, text="Selecciona el tipo de venta:", bg="azure").pack(pady=5)
        self.tipo_venta_combobox = ttk.Combobox(self, values=["Ventas Totales", "Ventas Locales", "Ventas Nacionales"])
        self.tipo_venta_combobox.pack(pady=5)
        self.tipo_venta_combobox.current(0)  # Selecciona "Ventas Totales" por defecto

        tk.Button(self, text="Generar Balance", command=self.generar_balance).pack(pady=20)

    def generar_balance(self):
        # Obtener fechas desde las entradas
        fecha_inicio_str = self.fecha_inicio_var.get()
        fecha_fin_str = self.fecha_fin_var.get()

        # Convertir las fechas al formato datetime
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%d/%m/%Y")
            fecha_fin = datetime.strptime(fecha_fin_str, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Usa Dia/Mes/Año.")
            return

        # Obtener el tipo de venta seleccionado
        tipo_venta = self.tipo_venta_combobox.get()

        # Calcular balance dependiendo del tipo de venta
        balance_total = self.calcular_balance(fecha_inicio, fecha_fin, tipo_venta)

        messagebox.showinfo("Balance Generado", f"Balance para {tipo_venta}: ${balance_total:.2f}")

    def calcular_balance(self, fecha_inicio, fecha_fin, tipo_venta):
        ventas_filtradas = []

        # Seleccionar la lista de ventas basada en el tipo de venta
        if tipo_venta == "Ventas Totales":
            ventas = self.babilon.getVentasT()
        elif tipo_venta == "Ventas Locales":
            ventas = self.babilon.getVentasL()
        elif tipo_venta == "Ventas Nacionales":
            ventas = self.babilon.getVentasN()
        else:
            ventas = []

        # Filtrar las ventas según las fechas
        for venta in ventas:
            fecha_venta = datetime.strptime(venta.fecha, "%d/%m/%Y")  # Ajustar al formato de fecha de las ventas
            if fecha_inicio <= fecha_venta <= fecha_fin:
                ventas_filtradas.append(venta)

        # Calcular el balance sumando los valores de las ventas filtradas
        balance_total = sum(venta.valor_total for venta in ventas_filtradas)

        return balance_total
