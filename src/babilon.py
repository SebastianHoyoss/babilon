from src.producto import *
from src.cliente import *

class Babilon:
    def __init__(self, nombre="Babiloon",clientes=[],inventario=[]):
        self.nombre=nombre
        self.clientes=[]
        self.inventario=[]

    def getClientes(self):
        return self.clientes

    def getInventario(self):
        return self.inventario

    def setInv(self,inventario):
        self.inventario=inventario

    def setClientes(self,clientes):
        self.clientes=clientes

    def agregar_producto(self, producto):

        for p in self.inventario:
            if p.nombre == producto.nombre and p.talla == producto.talla:
                p.cantidad += producto.cantidad
                return
        self.inventario.append(producto)

    def eliminar_producto(self, nombre, cantidad,inventario):
        self.inventario=inventario
        for p in self.inventario:
            if p.nombre == nombre:
                if p.cantidad <= cantidad:
                    self.inventario.remove(p)
                else:
                    p.cantidad -= cantidad
                return self.inventario

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        return self.clientes
    
    def retirar_cliente(self,nombre,clientes):
        self.clientes=clientes
        for p in self.clientes:
            if p.nombre==nombre:
                self.clientes.remove(p)