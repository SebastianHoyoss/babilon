from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
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

def salir():
    serializar(babilon)
    exit()

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

def hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    root.after(1000,hora)

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
    boton_salir=tk.Button(frame1,text="Salir",command=salir)

    etiqueta.grid(row=0,column=0,padx=0,pady=10,sticky="nsew")
    boton_func1.grid(row=1,column=0,padx=0,pady=10,sticky="nsew")
    boton_func2.grid(row=2,column=0,padx=0,pady=10,sticky="nsew")
    boton_func3.grid(row=3,column=0,padx=0,pady=10,sticky="nsew")
    boton_func4.grid(row=4,column=0,padx=0,pady=10,sticky="nsew")
    boton_func5.grid(row=5,column=0,padx=0,pady=10,sticky="nsew")
    boton_func6.grid(row=6,column=0,padx=0,pady=10,sticky="nsew")
    boton_salir.grid(row=7,column=0,padx=0,pady=10,sticky="nsew")

    frame1.configure(width=200,height=500,bg="azure",bd=5)
    frame2.configure(width=670,height=500,bg="light blue",bd=5)
    root.mainloop()