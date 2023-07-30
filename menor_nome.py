''' escrever uma função menor_nome(nomes) que recebe uma lista de strings
    contendo nomes de pessoas como parâmetro e devolve o nome mais curto.
    a funçao deve ignorar espaços antes e depois do nome e deve devolver ele
    capitalizado '''

def menor_nome(nomes):
    elements = len(nomes) - 1
    size = len(nomes[elements].strip())
    MenorNome = nomes[elements].strip()
    elements -= 1
    while elements >= 0:
        size2 = len(nomes[elements].strip())
        if size2 <= size:
            MenorNome = nomes[elements].strip()
        size = len(nomes[elements].strip())
        elements -= 1
    return MenorNome.capitalize()
