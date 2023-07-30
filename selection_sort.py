def ordena(lista):
    fim = len(lista)

    for i in range(fim-1):
        menor = i
        for j in range(i+1,fim):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista
