precio_venta = 805
precio_costo = 520
costo_actual= 12000
usuarios_anterior = 80
usuarios_nuevos = 124

ganancia = precio_venta - precio_costo
margen = ganancia / precio_venta * 100
ahorro = costo_actual * 0.08
crecimiento = ((usuarios_nuevos - usuarios_anterior) / usuarios_anterior * 100)

print(f"La ganancia es de {ganancia}")
print(f"El margen de ganancia de es {margen}")
print(f"El ahorro es de {ahorro}")
print(f"El crecimiento porcentual es de:{crecimiento}")
