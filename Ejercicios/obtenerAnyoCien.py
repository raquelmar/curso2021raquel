import datetime

nombre = input("Digame su nombre: ")
edadActual = input("Digame su edad: ")

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

anyoActual = date.year
print(anyoActual)
anyosQuedan = 100 - int(edadActual)
anyosCien = int(anyoActual) + int(anyosQuedan)
print(f"{nombre}, cumplirás 100 años aproximadamente en el año: {anyosCien}")