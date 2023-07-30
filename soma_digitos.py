numero = int(input("Digite um número inteiro:"))

soma = 0

while numero != 0:
    resto_numero = numero % 10
    numero = numero // 10
    soma = soma + resto_numero

print (soma)
