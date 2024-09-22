class Pedido:
    def __init__(self, numero, hora_salida, hora_entrega, productos, estado):
        self.numero = numero
        self.hora_salida = hora_salida
        self.hora_entrega = hora_entrega
        self.productos = productos
        self.estado = estado