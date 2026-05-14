from models.producto import Producto
from models.cliente import Cliente
from models.venta import Venta
from models.producto_alimenticio import ProductoAlimenticio

producto1 = Producto("Leche", 3500, 10)
producto2 = ProductoAlimenticio("Yugurt", 4500, 5, "20/06/2026")

cliente1= Cliente("Mariana", "123456789")

venta1 = Venta(cliente1, producto1, 2)

print(producto1.mostrar_info())
print(cliente1.mostrar_info())
print(venta1.realizar_venta())
print(producto1.mostrar_info())
print(producto2.mostrar_info())