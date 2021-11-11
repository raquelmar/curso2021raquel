# -*- coding: utf-8 -*-
# Creando la clase empleado
class ClaseEmpleado:
    def __init__(self, nombre, puesto, anyosAntiguedad):
        self.nombre = nombre
        self.puesto = puesto
        self.anyosAntiguedad = anyosAntiguedad

    def categoria_profesional(self):
        self.categoriaPorAntiguedad = self.anyosAntiguedad
        if self.categoriaPorAntiguedad < 2:
            print('El empleado es junior')

# Creando las instancias de la clase Coche
objeto_empleado = ClaseEmpleado('Maria','Analista', 15)
# Acceder a los atributos de ese objeto
print(objeto_empleado.nombre)
print(objeto_empleado.puesto)
print(objeto_empleado.anyosAntiguedad)

class Aptitudes(ClaseEmpleado):
    # El método __init__() para crear una clase hija
    def __init__(self, nombre, puesto, anyosAntiguedad, lenguajes, sitemas_operativos,idiomas):
        super().__init__(nombre, puesto, anyosAntiguedad)
        self.lenguajes = lenguajes
        self.sitemas_operativos = sitemas_operativos
        self.idiomas = idiomas

objetoAptitudesEmp = Aptitudes("maria", "analista", 15, "python","windows","inglés")
print(objetoAptitudesEmp.sitemas_operativos)
print(objetoAptitudesEmp.puesto)
print(objetoAptitudesEmp.anyosAntiguedad)
