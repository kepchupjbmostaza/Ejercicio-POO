class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
    def calcular_precio_final(self, cantidad):
        return self._precio

    def reducir_stock(self, cantidad):
        if self._stock >= cantidad:
            self._stock -= cantidad
        else:
            print(f"No queda stock suficiente de {self._nombre}.")

    @staticmethod
    def validar_precio(precio):
        if precio > 0:
            return True
        else:
            return False

class Electronico(Producto):
    def __init__(self, nombre, precio, meses_garantia):
        super().__init__(nombre, precio)
        self._meses_garantia = meses_garantia
        self._precio = precio * 1.19

class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla
    def calcular_precio_final(self, cantidad):
        if cantidad > 10:
            return self._precio * 0.9
        else:
            return self._precio

class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)
        print(f"Se ha agregado {producto._nombre} al carrito.")

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.calcular_precio_final(1)
        return total

compu = Electronico("Laptop", 1000, 24)
polera = Ropa("Polera", 20, "M")
carrito = Carrito()
carrito.agregar_producto(compu)
carrito.agregar_producto(polera)
print(f"Total del carrito: ${carrito.calcular_total()}")




