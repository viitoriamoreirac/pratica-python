import matriz

def soma_matrizes (A,B):
    num_lin = len(A)
    num_col = len(A[0])
    c = matriz.cria_matriz(num_lin, num_col)

    for lin in range(num_lin):
        for col in range(num_col):
            c[lin][col] = A[lin][col] + B[lin][col]
    return c

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[10,20,30],[40,50,60],[70,80,90]]
    print (soma_matrizes(A,B))
