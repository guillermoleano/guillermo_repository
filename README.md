x = int(input("ingrese un digito"))
y = int(input("ingrese otro digito"))

opcion = input("Ingrese la opción de calculo deseado: "
      "Opciones de cálculo disponibles:\n"
      "1: Suma\n"
      "2: Resta\n"
      "3: Multiplicación\n"
      "4: División\n"
      "5: Potencia\n"
      "6: Raíz cuadrada\n"
      "7: Porcentaje\n"
      "8: Módulo (%)\n"
      "9: Promedio de dos números\n")

if opcion == "1":
    resultado = x + y
    print("El resultado de la suma es:", resultado)
elif opcion == "2":
    resultado = x - y
    print("El resultado de la resta es:", resultado)
elif opcion == "3":
    resultado = x * y
    print("El resultado de la multiplicación es:", resultado)         
elif opcion == "4":
    if y != 0:
        resultado = x / y
        print("El resultado de la división es:", resultado)
    else:
        print("Error: No se puede dividir por cero.")
elif opcion == "5":
    resultado = x ** y
    print("El resultado de la potencia es:", resultado)
elif opcion == "6":
    if x >= 0:
        resultado = x ** 0.5
        print("El resultado de la raíz cuadrada es:", resultado)
    else:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
elif opcion == "7":
    resultado = (x / y) * 100
    print("El resultado del porcentaje es:", resultado, "%")
elif opcion == "8":
        if y != 0:
            resultado = x % y
            print("El resultado del módulo es:", resultado)
        else:
            print("Error: No se puede calcular el módulo con divisor cero.")
elif opcion == "9":
    resultado = (x + y) / 2
    print("El resultado del promedio es:", resultado)
else:    print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")    