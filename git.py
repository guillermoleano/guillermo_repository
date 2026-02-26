bienvenida = input("desea ingresar al sistema de validacion de cedula? (si/no): ")
if bienvenida.lower() == "si":
    cedula = input("Ingrese su numero de cedula: ")
    if len(cedula) != 10:
        print("numero de cedula no valido")
    elif cedula.isdigit():
        print("numero de cedula valido\n")
    else:
        print("numero de cedula no valido, debe contener solo numeros")
elif bienvenida.lower() == "no":
    print("gracias por usar el sistema de validacion de cedula")
else:    print("opcion no valida, por favor ingrese 'si' o 'no'")
=======
print("hola como estas xxxxsdf") 

