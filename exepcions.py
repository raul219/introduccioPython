try:
    num1 = int(input("Posa un numero: "))
    num2 = int(input("Posa un numero: "))
    resultado = num1 / num2
    print(resultado)
except:
    print("Error no se puede dividir por cero.")

try:
    numero = int(input("Introdueix un número: "))
    print("El número introduït és:", numero)
except ValueError:
    print("Error si us plau, introdueix nomes numeros.")

try:
    valor1 = float(input("Introdueix el primer valor: "))
    valor2 = float(input("Introdueix el segon valor: "))
    resultat = valor1 + valor2
    print(resultat)
except ValueError:
    print("Error")

llista = [1,3,5,6]
try:
    num = int(input("Fica el numero de la llista"))
    print(llista[num])
except:
    print("ERROR")
    
