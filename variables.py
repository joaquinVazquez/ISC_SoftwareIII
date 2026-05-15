producto = "Pan integral";
costo = 250;
cantidad = 3;

monto_credito = 5000;
tasa_mensual = 0.015;
plazo_meses = 12;

interes_total = monto_credito * tasa_mensual * plazo_meses;

print("--- RESUMEN DEL CREDITO ---")
print(f"El interes total es de {interes_total:.2f}")
print(f"Monto base: {monto_credito:.2f}")
print(f"Reporte: El {producto} tiene un valor de {costo} pesos")
print(f"Total: {costo * cantidad}")
