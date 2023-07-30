def éPrimo(n):
    i = n - 1
    while i != 1:
        if n % i != 0:
            i -= 1
        else:
            return False
    return True

def n_primos (n):
    i = 2
    quantidade_de_primos = 0
    while i <= n:
        if éPrimo(i):
            quantidade_de_primos += 1
        i += 1
    return quantidade_de_primos
        
