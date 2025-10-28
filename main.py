class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducirStock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print(f"No hay suficiente stock de {self.nombre} (disponible: {self.stock})")

    def aumentarStock(self, cantidad):
        self.stock += cantidad


class Carrito:
    def __init__(self):
        self.productos = []  # [[Producto, cantidad], ...]
        self.total = 0

    def agregarProducto(self, producto, cantidad):
        if producto.stock >= cantidad:
            producto.reducirStock(cantidad)

            # Buscar si ya está en el carrito
            for item in self.productos:
                if item[0].nombre == producto.nombre:
                    item[1] += cantidad
                    break
            else:
                self.productos.append([producto, cantidad])

            self.total += producto.precio * cantidad
            return True
        else:
            return False  # stock insuficiente

    def eliminarProducto(self, producto):
        for item in self.productos:
            if item[0].nombre == producto.nombre:
                prod, cantidad = item
                prod.aumentarStock(cantidad)
                self.total -= prod.precio * cantidad
                self.productos.remove(item)
                return True
        return False

    def vaciarCarrito(self):
        for prod, cantidad in self.productos:
            prod.aumentarStock(cantidad)
        self.productos.clear()
        self.total = 0

    def mostrarProducto(self, posicion):
        if 0 <= posicion < len(self.productos):
            prod, cantidad = self.productos[posicion]
            subtotal = cantidad * prod.precio
            return [prod.nombre, prod.precio, cantidad, subtotal]
        else:
            return "Producto no existente"


def buscar(nombre, deposito):
    for producto in deposito:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return False


# ----- Productos de ejemplo -----
deposito = [
    Producto("Manzana", 200, 10),
    Producto("Banana", 150, 5),
    Producto("Naranja", 180, 8),
    Producto("Pera", 220, 6),
    Producto("Zapatilla",1000,2)
]

carrito = Carrito()
