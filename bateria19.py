llista = []
while True:
    valor = input("Introdueix un número enter o 'final' per acabar: ")
    if valor == 'final':
        break
    else:
        llista.append(int(valor))
resultat = 0
for numero in llista:
    resultat = resultat + numero
print("La suma dels elements de la llista és: ", resultat)
