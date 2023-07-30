def primeiro_lex(lista):
    i = len(lista) - 1
    first = lista[0]
    while i >= 0:
        if first >= lista[i]:
            first = lista[i]
        i -= 1
    return first
        
