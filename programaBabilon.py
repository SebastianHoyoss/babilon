from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime
from enum import Enum
import time
from baseDatos.serializacion import serializar, deserializar
from excepciones.excepciones import *
from ventanas.crear_cliente import *
from ventanas.crear_producto import *
from ventanas.eliminar_producto import *
from ventanas.gestion_inv import *
from ventanas.registrar_venta import *
from ventanas.actualizar_precios import *
from ventanas.gestion_cliente import *
from ventanas.respaldo_Actualizar_precios import *

user="admin"
password="admin"
def salir():
    serializar(babilon)
    exit()

def validar_login():
    global password
    usuario = entry_usuario.get()
    contra = entry_contraseña.get()

    if usuario==user and contra==password:
        messagebox.showinfo("Bienvenido", f"Se ha iniciado sesión correctamente!")
        ventana_login.destroy()
        root.deiconify()
    else:
        messagebox.showinfo("Error", "Credenciales incorrectas")

#Centrar una ventana TopLevel
def center_window(window, width, height):
    # Obtener las dimensiones de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calcular las coordenadas para centrar la ventana
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Establecer la geometría de la ventana
    window.geometry(f"{width}x{height}+{x}+{y}")

# Función para abrir la ventana Toplevel (Crear Cliente)
def abrir_ventana_clientes():
    # Limpiar el frame2
    for widget in frame2.winfo_children():
        widget.destroy()
    
    # Crear y agregar el ClienteWindow al frame2
    cliente_window = ClienteWindow(frame2, babilon)
    cliente_window.pack(fill='both', expand=True)

# Función para abrir la ventana Toplevel (Crear Producto)
def abrir_ventana_producto():
    # Limpiar el frame2
    for widget in frame2.winfo_children():
        widget.destroy()
    
    # Crear y agregar el ProductoWindow al frame2
    producto_window = ProductoWindow(frame2, babilon)
    producto_window.pack(fill='both', expand=True)


def abrir_ventana_registrar_venta():
    # Limpiar el frame2
    for widget in frame2.winfo_children():
        widget.destroy()
    
    # Crear y agregar la ventana RegistrarVentaWindow al frame2
    venta_window = RegistrarVentaWindow(frame2, babilon)
    venta_window.pack(fill='both', expand=True)
def hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    serializar(babilon)
    root.after(1000,hora)

def abrir_ventana_actualizar_precios():
    actualizarPreciosWindow(root, babilon)


babilon=deserializar()
clientes=babilon.getClientes()
inventario=babilon.getInventario()
ventasT=babilon.getVentasT()
ventasL=babilon.getVentasL()
ventasN=babilon.getVentasN()

print("VENTAS TOTALES")
for venta in ventasT:
    print(venta.numero)
    print(venta.cliente.nombre)
    print(venta.fecha)
    print(venta.producto.nombre)
    print(venta.valor_total)
print("VENTAS LOCALES")
for venta in ventasL:
    print(venta.numero)
    print(venta.cliente.nombre)
    print(venta.fecha)
    print(venta.producto.nombre)
    print(venta.valor_total)
print("VENTAS NACIONALES")
for venta in ventasN:
    print(venta.numero)
    print(venta.cliente.nombre)
    print(venta.fecha)
    print(venta.producto.nombre)
    print(venta.valor_total)

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("assets/babilon.ico.ico")
    root.title("Babiloon Shoes")
    root.geometry("850x500")
    root.resizable(False,False)
    # Configura las filas y columnas para que ocupen el espacio
    root.rowconfigure(1, weight=1)  # Permitir que la fila 1 expanda
    root.columnconfigure(0, weight=0)  # La columna 0 (frame1) no expande
    root.columnconfigure(1, weight=1)  # La columna 1 (frame2) expande

    frame1 = tk.Frame(root, padx=10, pady=20, bd=1, relief="solid", bg="azure")
    frame2 = tk.Frame(root, padx=10, pady=20, bd=1, relief="solid", bg="light blue")

    frame1.grid(row=1, column=0, sticky="nsew")
    frame2.grid(row=1, column=1, sticky="nsew")

    # Elimina la restricción de tamaño y permite que el frame2 ocupe todo el espacio
    frame1.pack_propagate(False)
    frame2.pack_propagate(True)  # Permitir que frame2 se ajuste al contenido
    etiqueta=tk.Label(frame1,text="Hora")
    hora()

    boton_func1=tk.Button(frame1,text="Gestionar Clientes",command=abrir_ventana_clientes)
    boton_func2=tk.Button(frame1,text="Gestionar Inventario",command=abrir_ventana_producto)
    boton_func3=tk.Button(frame1,text="Registrar Venta",command=abrir_ventana_registrar_venta)
    boton_salir=tk.Button(frame1,text="Salir",command=salir)

    etiqueta.grid(row=0,column=0,padx=0,pady=10,sticky="nsew")
    boton_func1.grid(row=1,column=0,padx=0,pady=10,sticky="nsew")
    boton_func2.grid(row=2,column=0,padx=0,pady=10,sticky="nsew")
    boton_func3.grid(row=5,column=0,padx=0,pady=10,sticky="nsew")
    boton_salir.grid(row=7,column=0,padx=0,pady=10,sticky="nsew")

    # Ventana de Login
    ventana_login = tk.Toplevel(root)
    ventana_login.title("Iniciar Sesión")
    center_window(ventana_login, 300, 200)

    # Crear frame para centrar etiquetas y entradas
    frame_login = tk.Frame(ventana_login)
    frame_login.pack(pady=20)

    tk.Label(frame_login, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
    entry_usuario = tk.Entry(frame_login)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame_login, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
    entry_contraseña = tk.Entry(frame_login, show="*")
    entry_contraseña.grid(row=1, column=1, padx=10, pady=10)

    # Botón de login
    boton_login = tk.Button(frame_login, text="Iniciar sesión", command=validar_login)
    boton_login.grid(row=2, column=0, columnspan=2, pady=10)

    # Cerrar la ventana de login correctamente
    def cerrar_ventana_login():
        ventana_login.destroy()
        root.quit()  # Cierra la aplicación

    ventana_login.protocol("WM_DELETE_WINDOW", cerrar_ventana_login)

    # Ocultar la ventana principal al inicio
    root.withdraw()
    ventana_login.mainloop()
