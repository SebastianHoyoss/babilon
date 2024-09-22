class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)
        print(f"Pedido agregado para {self.nombre}: {pedido}")