def minmax (temperaturas):
    print ("A maior temperatura do mês foi:",máxima(temperaturas),"°C")
    print ("A menor temperatura do mês foi:",mínima(temperaturas),"°C")


def mínima(temp):
    quantidade = len(temp) - 1
    menor = temp[quantidade]
    i = 0
    while i <= quantidade:
        if temp[i] < menor:
            menor = temp[i]
        i += 1
    return menor


def máxima(temp):
    quantidade = len(temp) - 1
    maior = temp[quantidade]
    i = 0
    while i <= quantidade:
        if temp[i] > maior:
            maior = temp[i]
        i += 1
    return maior


def teste_pontual(temp, valor_esperado):
    valor_calculado = mínima(temp)
    if valor_calculado != valor_esperado:
        print ("Valor errado para array",temp,". Valor esperado:",valor_esperado)
        print ("O valor calculado foi:",valor_calculado)
        print()

        
def testa_mínima():
    print ("Iniciando os testes")
    teste_pontual([0],0)
    teste_pontual([2,3,4,5],2)
    teste_pontual([3,6,7,9,2],2)
    teste_pontual([3,6,7,9,2,-2,-15,8,7],-15)
    print ("Finalizando os testes")

    

def teste_pontual(temp, valor_esperado):
    valor_calculado = máxima(temp)
    if valor_calculado != valor_esperado:
        print ("Valor errado para array",temp,". Valor esperado:",valor_esperado)
        print ("O valor calculado foi:",valor_calculado)
        print()

        
def testa_máxima():
    print ("Iniciando os testes")
    teste_pontual([0],0)
    teste_pontual([2,3,4,5],5)
    teste_pontual([3,6,7,9,2],9)
    teste_pontual([3,6,7,9,2,-2,-15,8,7],9)
    print ("Finalizando os testes")
