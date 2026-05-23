precio = 149
inversion = 85000
tasa = 0.12
meses = 18

print("=== SIN FORMATO ===")
print(f"{precio}")
print(f"{inversion}")
print(f"{tasa}")
print(f"{meses}")

print("=== CON FORMATO ===")
print(f"{precio:.2f}")
print(f"{inversion:,.2f}")
print(f"{tasa}%")
print(f"{meses} meses")