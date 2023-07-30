def remove_repetidos(lista):
    quantidade = len(lista) - 1
    elemento = 0
    lista2 = []
    i = 0
    
    while quantidade >= 0:
        while elemento < quantidade:
            if lista[quantidade] == lista[elemento]:
                i += 1
            elemento += 1
        if i == 0:
            lista2.append(lista[quantidade])
        quantidade -= 1
        elemento = 0
        i = 0
        
    return sorted(lista2)
