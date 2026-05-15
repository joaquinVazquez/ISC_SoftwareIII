nombre_producto = "CrossUp"
precio = 90
version_gratuita = True

def aplicar_descuento(precio):
    precio_descuento = precio * 0.9
    print(f"El precio con descuento es de {precio_descuento}")

aplicar_descuento(precio)