def conta_letras(frase,contar="vogais"):
    vogais = 0
    consoantes = 0
    i = len(frase) - 1
    list_vogais = ["A","E","I","O","U","a","e","i","o","u"]
    while i >= 0:
        if frase[i] in list_vogais:
            vogais += 1
        elif frase[i] != " ":
            consoantes += 1
        i -= 1
    if contar == "vogais":
        return vogais
    else:
        return consoantes
        
