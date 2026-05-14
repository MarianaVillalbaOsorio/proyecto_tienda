class Venta:

    def __init__(self, cliente, producto, cantidad):
        
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
    
    def calcular_total(self):
        return self.producto.precio * self.cantidad
    
    def realizar_venta(self):

        if self.producto.actualizar_stock(self.cantidad):

            return f"Venta realizada. Total: ${self.calcular_total()}"
        
        return "No hay suficiente stock."