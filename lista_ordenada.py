def ordenada(lista):
    fim = len(lista)
    for i in range(fim - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
