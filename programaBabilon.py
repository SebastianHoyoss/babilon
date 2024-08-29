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

class InfoApp:
    def __init__(self,frame):
        self.row_height=500
        self.col_width=400
        self.frame=frame
        self.frameApp=Frame(self.frame,bg="#c3c3c3",width=550,height=400)
        self.frameApp.grid(row=0,column=0,sticky="nsew")
        Label(self.frameApp,text="Bienvenido a la aplicación de gestión administrativa de Babiloon Shoes", font=("Bold",12)).place(x=10,y=30)
        descripcion="Mediante esta aplicación podrás gestionar activamente\n las ventas, clientes e inventario del almacén"
        Label(self.frameApp,text=descripcion,font=("Bond",10)).place(x=10,y=150)

def abrir_func1():
    func1Top=Toplevel(root)
    func1Top.title("Funcionalidad 1")
    func1Top.geometry("500x500")
    func1Top.configure(bg="azure")

def abrir_func2():
    func2Top=Toplevel(root)
    func2Top.title("Funcionalidad 2")
    func2Top.geometry("500x500")
    func2Top.configure(bg="azure")

def abrir_func3():
    func3Top=Toplevel(root)
    func3Top.title("Funcionalidad 3")
    func3Top.geometry("500x500")
    func3Top.configure(bg="azure")

def abrir_func4():
    func4Top=Toplevel(root)
    func4Top.title("Funcionalidad 4")
    func4Top.geometry("500x500")
    func4Top.configure(bg="azure")

def abrir_func5():
    func5Top=Toplevel(root)
    func5Top.title("Funcionalidad 5")
    func5Top.geometry("500x500")
    func5Top.configure(bg="azure")

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

    boton_func1=tk.Button(frame1,text="Func1",command=abrir_func1)
    boton_func2=tk.Button(frame1,text="Func2",command=abrir_func2)
    boton_func3=tk.Button(frame1,text="Func3",command=abrir_func3)
    boton_func4=tk.Button(frame1,text="Func4",command=abrir_func4)
    boton_func5=tk.Button(frame1,text="Func5",command=abrir_func5)

    etiqueta.grid(row=0,column=0,padx=0,pady=10,sticky="nsew")
    boton_func1.grid(row=1,column=0,padx=0,pady=10,sticky="nsew")
    boton_func2.grid(row=2,column=0,padx=0,pady=10,sticky="nsew")
    boton_func3.grid(row=3,column=0,padx=0,pady=10,sticky="nsew")
    boton_func4.grid(row=4,column=0,padx=0,pady=10,sticky="nsew")
    boton_func5.grid(row=5,column=0,padx=0,pady=10,sticky="nsew")

    frame1.configure(width=200,height=500,bg="azure",bd=5)
    frame2.configure(width=670,height=500,bg="light blue",bd=5)
    root.mainloop()