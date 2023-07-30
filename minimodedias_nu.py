'''def acharMinimoDeDias(n):
    i = 0
    duracoes = []
    while i < n:
        elemento = float(input())
        if 1.01 <= elemento <= 3.0:
            duracoes.append(elemento)
            i += 1
    print (duracoes)
    
    dia = 0
    i = len(duracoes) - 1
    k = 0
    
    while i > 0:
        while k < i:
            while duracoes[k] + duracoes[i] <= 3.00:
                del duracoes[i]
                del duracoes[k]
                dia += 1
                i = len(duracoes) - 1
                print (duracoes)
                print (i)
                print (dia)
                k += 1
            del duracoes[i]
            dia += 1
            i -= 1
            print(dia)


 desisti.'''

def acharMinimoDeDias(n):
    i = 0
    duracoes = []
    while i < n:
        elemento = float(input())
        if 1.01 <= elemento <= 3.0:
            duracoes.append(elemento)
            i += 1
        return duracoes
