nombre_producto = "Fintech"
precio_mesual = 149
unidades = 10
categoria = "Software"
descuento = 0.20
meses = 12

total_inventario = precio_mesual * unidades


print("=== REPORTE DE PRODUCTO ===")
print("Producto: FinX")
print("Categoria: Software financiero")
print(f"Precio:{precio_mesual:.2f}")
print(f"Undades:{unidades}")
print(f"Valor total: ${total_inventario:.2f}")


costo_anual = precio_mesual * meses
descuento = precio_mesual * 0.20
precio_descuento = costo_anual - descuento

print("=== PLAN ANUAL ===")
print(f"Precio:{precio_mesual:.2f}")
print(f"Descuento anual: 20%")
print(f"Total a pagar: {precio_descuento:.2f} pesos")

