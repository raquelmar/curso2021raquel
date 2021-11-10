
x = 100
y = 500
if y > x:
    print(y, '(y) es mayor que', x, ('x'))
elif x == y:
    print(x, '(x) e (y)', y, 'tienen el mismo valor')
else:
    print(x, '(x) es mayor que', y, ('y'))

frutas = ['banana', 'manzana','pera', 'naranja']
for f in frutas:
    print("La palabra", f, "tiene", len(f), "letras")

for i in range(0, 10, 3):
    print("Imprime de 0 a 9, de tres en tres unidades", i)