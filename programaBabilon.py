from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from enum import Enum
import time

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

def info():
    pass
def func1():
    pass
def func2():
    pass
def func3():
    pass
def func4():
    pass
def func5():
    pass

def hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    root.after(1000,hora)

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("babilon.ico.ico")
    root.title("Babiloon Shoes")
    root.geometry("730x400")
    root.resizable(False,False)
    frame1=tk.Frame(root,padx=10,pady=20,bd=1,relief="solid")
    frame2=tk.Frame(root,padx=10,pady=20,bd=1,relief="solid")
    frameI=tk.Frame(frame2)

    frame1.grid(row=1, column=0, sticky="nsew")
    frame1.pack_propagate(False)
    frame2.grid(row=1,column=1,sticky="nsew")
    frame2.pack_propagate(False)

    etiqueta=tk.Label(root,text="Hora")
    hora()
    etiqueta.grid(row=1,column=2,sticky="n")
    boton_info=tk.Button(frame1,text="Info",command=info)
    boton_func1=tk.Button(frame1,text="Func1",command=func1)
    boton_func2=tk.Button(frame1,text="Func2",command=func2)
    boton_func3=tk.Button(frame1,text="Func3",command=func3)
    boton_func4=tk.Button(frame1,text="Func4",command=func4)
    boton_func5=tk.Button(frame1,text="Func5",command=func5)

    boton_info.grid(row=0,column=0,sticky="nsew")
    boton_func1.grid(row=1,column=0,sticky="nsew")
    boton_func2.grid(row=2,column=0,sticky="nsew")
    boton_func3.grid(row=3,column=0,sticky="nsew")
    boton_func4.grid(row=4,column=0,sticky="nsew")
    boton_func5.grid(row=5,column=0,sticky="nsew")

    frame1.configure(width=100,height=500,bg="azure",bd=5)
    frame2.configure(width=600,height=400,bg="light blue",bd=5)
    root.mainloop()