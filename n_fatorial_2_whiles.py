#receber uma sequencia de numeros do usuario
#imprimir o fatorial de cada numero
#while mais externo que vai ler o numero
#while mais interno que vai calcular o fatorial

n = 1
while n >= 0:
    n = int(input("Digite um número inteiro positivo:"))
    n_fatorial = 1
    nn = n
    while n > 1:
        n_fatorial = n_fatorial * n
        n = n - 1
    print ("O fatorial de",nn,"é:" ,n_fatorial)
    
