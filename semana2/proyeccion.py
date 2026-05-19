precio = 149
usuarios_anio1 = 200
usuarios_anio2 = usuarios_anio1 * 1.5
usuarios_anio3 = usuarios_anio2 * 1.5


print("=== PROYECCIÓN DE INGRESOS ===")
print(f"Precio mensual por usuario {precio:.2f} MXN")
print("--------------------------------------------------------------------")
ingreso_anual1 = usuarios_anio1 * precio * 12
print(f"Año 1 | {usuarios_anio1} usuarios | ${ingreso_anual1:.2f}")
ingreso_anual2 = usuarios_anio2 * precio * 12
print(f"Año 2 | {usuarios_anio2} usuarios | ${ingreso_anual2:.2f}")
ingreso_anual3 = usuarios_anio3 * precio * 12
print(f"Año 2 | {usuarios_anio3} usuarios | ${ingreso_anual3:.2f}")
print("--------------------------------------------------------------------")
ingreso_total = ingreso_anual1 + ingreso_anual2 + ingreso_anual3
print(f"Ingreso acumulado 3 años: ${ingreso_total:.2f} MXN")