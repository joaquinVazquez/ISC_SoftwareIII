plan_usuario =  "Otro"

if plan_usuario == "Gratuito":
    print("Acceso limitado - 3 Proyectos máximo")
elif plan_usuario == "Básico":
    print("Acceso estandar - 10 proyectos")
elif plan_usuario == "Profesional":
    print("Acceso completo - Proyectos ilimitados")
elif plan_usuario == "Empresarial":
    print("Acceso total + Soporte prioritario")
else:
    print("Opción no valida")