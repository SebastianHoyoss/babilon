from src.producto import *
from src.cliente import *
from src.venta import *

class Babilon:
    def __init__(self, nombre="Babiloon",clientes=[],inventario=[],ventasL=[],ventasN=[],ventasT=[]):
        self.nombre=nombre
        self.clientes=clientes
        self.inventario=inventario
        self.ventasT=ventasT
        self.ventasL=ventasL
        self.ventasN=ventasN
    def getClientes(self):
        return self.clientes

    def getInventario(self):
        return self.inventario

    def setInv(self,inventario):
        self.inventario=inventario

    def setVentasT(self,ventasT):
        self.ventasT=ventasT
    def getVentasT(self):
        return self.ventasT

    def setVentasL(self,ventasL):
        self.ventasL=ventasL
    def getVentasL(self):
        return self.ventasL
    def setVentasN(self,ventasN):
        self.ventasN=ventasN
    def getVentasN(self):
        return self.ventasN
    def setClientes(self,clientes):
        self.clientes=clientes

    def eliminar_cantidad(self, producto, cantidad):
        for p in self.inventario:
            if p == producto:
                p.cantidad -= cantidad
    def crear_venta_loc(self, numero, cliente, fecha, producto, valor, cantidad,localidad):
        venta=Venta(numero, cliente, fecha, producto, valor,localidad)
        self.ventasL.append(venta)
        self.ventasT.append(venta)
        self.eliminar_cantidad(producto,cantidad)

    def crear_venta_nal(self, numero, cliente, fecha, producto, valor, cantidad,localidad):
        venta=Venta(numero, cliente, fecha, producto, valor,localidad)
        self.ventasN.append(venta)
        self.ventasT.append(venta)
        self.eliminar_cantidad(producto,cantidad)

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

    def agregar_venta(self,venta):
        self.ventas.append(venta)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        return self.clientes
    
    def retirar_cliente(self,nombre,clientes):
        self.clientes=clientes
        for p in self.clientes:
            if p.nombre==nombre:
                self.clientes.remove(p)