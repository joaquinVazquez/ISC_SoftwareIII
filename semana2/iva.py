precio = 149


def calcular_con_iva_mensual(precio, iva):
    iva = precio * iva
    precio_total_iva = precio + iva
    return precio_total_iva

def calcular_con_iva_anual(precio, iva):
    iva = (precio * iva)
    precio_total_iva = (precio + iva) * 12
    return precio_total_iva

resultado_mes = calcular_con_iva_mensual(precio, 0.16)
resultado_anio = calcular_con_iva_anual(precio, 0.16)
resultado_mes_8 = calcular_con_iva_mensual(precio, 0.08)
print("======== PRECIO CON IVA =======")
print(f"Plan mensual (IVA 16%): {resultado_mes:.2f} MXN")
print(f"Plan anual (IVA 16%): {resultado_anio:.2f} MXN")
print(f"Plan anual (IVA 8%): {resultado_mes_8:.2f} MXN")
print("===================================================")