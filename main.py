class producto:
    def __init__(self,nombre:str,precio:float,stock:int):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
    def reducirstock(self,cant):
        if self.stock>=0:
            self.stock-=cant
            return self.stock
        else:
            return "No hay suficiente stock"
    def aumentarstock(self,cant):
        if self.stock>=0:
            self.stock+=cant
            return self.stock
        else:
            return "Ingrese un valor coherente"
class carrito(producto):
    def __init__(self,productos= []):
        self.productos=productos
    def agregarproducto(self,productito):
        self.productos.append(productito).lower()
    
        

    