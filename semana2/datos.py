nombre_fundador = "Joaquín Vázquez"
inversion_inicial = float(120000)
num_socios = int(3)
tiene_app_movil = bool(True)
ciudad_lanzamiento = str("Teopsica, Chiapas")

print(f"El tipo de dato del nombre del fundador es {type(nombre_fundador)}")
print(f"El tipo de dato de inversión inicial es {type(inversion_inicial)}")
print(f"El tipo de dato del número de socio es  {type(num_socios)}")
print(f"El tipo de dato para saber si tiene app movil es  {type(tiene_app_movil)}")
print(f"El tipo de dato de la ciudad de lanzamiento es  {type(ciudad_lanzamiento)}")

suma_datos = num_socios + inversion_inicial
print(f"Este es un ejemplo de la suma de un float e int, resultado {suma_datos}")