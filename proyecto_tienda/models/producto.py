class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock}"

    def actualizar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False
