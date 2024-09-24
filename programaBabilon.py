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
from ventanas.eliminar_cliente import *
from ventanas.eliminar_producto import *
from ventanas.mostrar_cliente import *
from ventanas.mostrar_producto import *
from ventanas.registrar_venta import *
from ventanas.actualizar_precios import *

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


# Función para abrir la ventana Toplevel (Crear Cliente)
def abrir_ventana_clientes():
    ClienteWindow(root, babilon)

# Función para abrir la ventana Toplevel (Mostrar Cliente)
def abrir_ventana_mostrar_clientes():
    global mostrar_clientes_window
    mostrar_clientes_window = MostrarClientesWindow(root, babilon)

# Función para abrir la ventana Toplevel (Eliminar Cliente)
def abrir_ventana_eliminar_clientes():
    EliminarClienteWindow(root, babilon)

# Función para abrir la ventana Toplevel (Crear Producto)
def abrir_ventana_producto():
    ProductoWindow(root, babilon)

# Función para abrir la ventana Toplevel (Mostrar Productos)
def abrir_ventana_mostrar_productos():
    global mostrar_productos_window
    mostrar_productos_window = MostrarProductosWindow(root, babilon)

# Función para abrir la ventana Toplevel (Eliminar Producto)
def abrir_ventana_eliminar_producto():
    EliminarProductoWindow(root, babilon)

def abrir_ventana_registrar_venta():
    RegistrarVentaWindow(root, babilon)
def hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    serializar(babilon)
    root.after(1000,hora)

def abrir_ventana_actualizar_precios():
    actualizarPreciosWindow(root, babilon)


babilon=deserializar()
clientes=babilon.getClientes()
inventario=babilon.getInventario()

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("assets/babilon.ico.ico")
    root.title("Babiloon Shoes")
    root.geometry("750x500")
    root.resizable(False,False)
    frame1=tk.Frame(root,padx=10,pady=20,bd=1,relief="solid")
    frame2=tk.Frame(root,padx=10,pady=20,bd=1,relief="solid")

    frame1.grid(row=1, column=0, sticky="nsew")
    frame1.pack_propagate(False)
    frame2.grid(row=1,column=1,sticky="nsew")
    frame2.pack_propagate(False)

    etiqueta=tk.Label(frame1,text="Hora")
    hora()

    boton_func1=tk.Button(frame1,text="Añadir Cliente",command=abrir_ventana_clientes)
    boton_func2=tk.Button(frame1,text="Eliminar Cliente",command=abrir_ventana_eliminar_clientes)
    boton_func3=tk.Button(frame1,text="Consultar Clientes",command=abrir_ventana_mostrar_clientes)
    boton_func4=tk.Button(frame1,text="Añadir Producto",command=abrir_ventana_producto)
    boton_func5=tk.Button(frame1,text="Eliminar Producto",command=abrir_ventana_eliminar_producto)
    boton_func6=tk.Button(frame1,text="Consultar Inventario",command=abrir_ventana_mostrar_productos)
    boton_func7=tk.Button(frame1,text="Registrar Venta",command=abrir_ventana_registrar_venta)
    boton_func8=tk.Button(frame1,text="Actuializar Precios",command=abrir_ventana_actualizar_precios)
    boton_salir=tk.Button(frame1,text="Salir",command=salir)

    etiqueta.grid(row=0,column=0,padx=0,pady=10,sticky="nsew")
    boton_func1.grid(row=1,column=0,padx=0,pady=10,sticky="nsew")
    boton_func2.grid(row=2,column=0,padx=0,pady=10,sticky="nsew")
    boton_func3.grid(row=3,column=0,padx=0,pady=10,sticky="nsew")
    boton_func4.grid(row=4,column=0,padx=0,pady=10,sticky="nsew")
    boton_func5.grid(row=5,column=0,padx=0,pady=10,sticky="nsew")
    boton_func6.grid(row=6,column=0,padx=0,pady=10,sticky="nsew")
    boton_func7.grid(row=7,column=0,padx=0,pady=10,sticky="nsew")
    boton_func8.grid(row=7,column=0,padx=0,pady=10,sticky="nsew")
    boton_salir.grid(row=8,column=0,padx=0,pady=10,sticky="nsew")

    frame1.configure(width=200,height=500,bg="azure",bd=5)
    frame2.configure(width=670,height=500,bg="light blue",bd=5)

    root.withdraw()
    ventana_login=tk.Tk()
    ventana_login.title("Iniciar Sesión")
    ventana_login.geometry("300x200")
    tk.Label(ventana_login, text="Usuario").grid(row=0, column=0, padx=10, pady=10)
    entry_usuario = tk.Entry(ventana_login)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(ventana_login, text="Contraseña").grid(row=1, column=0, padx=10, pady=10)
    entry_contraseña = tk.Entry(ventana_login, show="*")  # 'show="*"' oculta la contraseña
    entry_contraseña.grid(row=1, column=1, padx=10, pady=10)

    # Botón de login
    boton_login = tk.Button(ventana_login, text="Iniciar sesión", command=validar_login)
    boton_login.grid(row=2, column=0, columnspan=2, pady=10)
    ventana_login.mainloop()