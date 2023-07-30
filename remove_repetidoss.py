def remove_repetidos(lista):
    quantidade = len(lista) - 1
    elemento = 0
    
    while quantidade >= 0:
        while elemento < quantidade and lista[quantidade] != lista[elemento]:
            
            if lista[quantidade] == lista[elemento]:
                del lista[quantidade]
            elemento += 1
        quantidade -= 1
        elemento = 0
        
    print (lista)
                
