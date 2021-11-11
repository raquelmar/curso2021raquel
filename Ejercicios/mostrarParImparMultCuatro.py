numeroInsertado = input("Escriba un número: ")
if int(numeroInsertado) % 2 == 0:
    print(f"El numero insertado {int(numeroInsertado)} es par")
    if int(numeroInsertado) % 4 == 0:
        print(f'Enhorabuena! El numero insertado {int(numeroInsertado)} también es múltiplo de cuatro.')
else:
    print(f"El numero insertado {int(numeroInsertado)} es impar")