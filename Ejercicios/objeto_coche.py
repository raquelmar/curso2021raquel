# Importando solamente un módulo de la clase

from clase_coche import ClaseCoche
from clase_coche import CocheElectrico

# Creando las instancias de la clase Coche
coche = ClaseCoche('SEAT','Ateca', '1.0')
# Acceder a los atributos de ese objeto
print(coche.marca)
print(coche.modelo)
print(coche.tipo)

coche_electrico = CocheElectrico('Tesla', 'Modelo 3', 'Berlina')





