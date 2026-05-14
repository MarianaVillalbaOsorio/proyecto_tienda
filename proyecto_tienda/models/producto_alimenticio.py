from models.producto import Producto

class ProductoAlimenticio(Producto):

    def __init__(self, nombre, precio, stock, fecha_vencimiento):

        super().__init__(nombre, precio, stock)
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_info(self):
        return f"Producto alimenticio: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock} | Vence: {self.fecha_vencimiento}"