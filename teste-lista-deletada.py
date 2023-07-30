lista = [2, 4, 3, 4, 6]

print (len(lista))
quantidade = len(lista) - 1

while quantidade >= 0:
    if lista[quantidade] == 4:
        del lista[quantidade]
        print (lista)
    quantidade -= 1
print (lista)
