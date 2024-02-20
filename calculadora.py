while True:
    print("MENÚ PRINCIPAL:")
    print("Benvinguts a pycalc, introduïu una de les següents opcions:")
    print("0. Sortir")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcio = int(input("Introdueix la vostra opció: "))

    if opcio == 0:
        print("Adéu!")
        break
    elif opcio in [1, 2, 3, 4]:
        num1 = float(input("Introdueix el primer número: "))
        num2 = float(input("Introdueix el segon número: "))

        if opcio == 1:
            suma = num1 + num2
            print("La suma de", num1, "+", num2, "és:", suma)
        elif opcio == 2:
            resta = num1 - num2
            print("La resta de", num1, "-", num2, "és:", resta)
        elif opcio == 3:
            multiplicacion = num1 * num2
            print("La multiplicació de", num1, "*", num2, "és:", multiplicacion)
        elif opcio == 4:
            if num2 != 0:
                division = num1 / num2
                print("La divisió de", num1, "/", num2, "és:", division)
            else:
                print("La divisio de 0 entre 0 es: Infinit")
    else:
        print("Opció no vàlida. Si us plau, introduïu una opció vàlida.")
