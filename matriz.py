def cria_matriz (num_linhas, num_colunas):
    ''' (int,int)  -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas colunas
    em que cada elemento é digitado pelo usuário.
    '''

    matriz = []
    for i in range(num_linhas):
        linha = []
        for o in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(o) + "]:"))
            linha.append(valor)

        matriz.append(linha)
    return matriz

def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin,col)
