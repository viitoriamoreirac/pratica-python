def maior_primo(n):
    while n >= 2:
        if éPrimo(n):
            return n
        else:
            n -=1
             
    
def éPrimo(k):
    i = k - 1
    while i != 1:
        if k % i != 0:
            i -= 1
        else:
            return False
    return True
        
