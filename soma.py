quant = int(input("Quantos números você quer somar?"))

soma = 0
total = 0

while total < quant:
    valor = int(input("Digite o valor a ser somado: "))
    soma = soma + valor
    total = total +1

print ("A soma dos valores é:", soma)
