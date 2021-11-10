#calcular media de tres valores
def calcular_media(*args):
    total = 0
    for i in args:
        total += i
    result_media = total / len(args)
    return result_media

a, b, c = 5, 42, 23
media = calcular_media(a, b, c)

print(f"La media de {a},{b}, y {c} es {media}")
