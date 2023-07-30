def soma_elementos(n):
    
    elemento = len(n) - 1
    soma = 0
    while elemento >= 0:
        soma = soma + n[elemento]
        elemento -= 1
    return soma
