
class Producto:
    def __init__(self, nombre,categoria,descripcion, disponible):
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.disponible = disponible

radio = Producto("Radio","Audio","dispositivo para escuchar musica", True)
lavadora = Producto("Lavadora","electrodomestico","dispositivo para lavar la ropa", True)
celular = Producto("Celular","telefono","dispositivo para llamar", True)

#por que el atributo disponible marca si hay o no stock del producto en la tienda
if radio.disponible == True:
    ### if radio.categoria ==electrodomestico
    ### mensaje si es electrodomestico y la descripcion
    ### if radio.categoria == telefono
    ### if radio.categoria == computadora
    ### if radio.categoria == accesorio
    ### else: 
    ### no se encontro categoria para el producto
    print("aqui escribir su codigo")
else:
    print(f"el producto {radio.nombre} se encuentra agotado")