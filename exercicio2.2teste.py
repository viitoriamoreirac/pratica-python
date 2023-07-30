soma = int(input("Digite aqui uma sequência de números a ser somada e termine com zero. "))

valor = 0
while soma != 0:
  valor = valor + soma
  soma = int(input ("Mais um número:"))

print ("A soma é", valor)
