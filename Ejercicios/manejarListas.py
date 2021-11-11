listaExtremos = [0]
listaMaxMin = [0]
listaNumeros = [0]
cont = 1

numeros = input('Digame de 5 a 10 numeros (separados por un espacio): ')

for num in [int(n) for n in numeros.split(" ")]:
    if cont > 10:
        print("Ha insertado demasiados numeros. Utilizaremos solo 10")
        break
    listaNumeros.append(num)
    if cont == 1:
        minNumL = num
        listaExtremos.append(num)
    if (num < minNumL):
        minNumL = num
    # for verNumMaxMin in
    cont += 1
listaExtremos.append(listaNumeros[len(listaNumeros)-1])
if len(listaNumeros) < 5:
    print("Ha insertado pocos numeros. Vuelva a intentarlo")
    exit()
print(f"primer y ultimo número: {listaExtremos[1]},  {listaExtremos[2]}")
print ("numeros que hemos usado {len(listaNumeros)}")
print(f"el menor numero mio de los insertados: {minNumL}")
print(f"el mayor numero de los insertados: {max(listaNumeros)}")
