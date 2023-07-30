largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

largur = 1
altur = 1

while altur <= altura:
    while largur <= largura:
        print ("#", end="")
        largur += 1
    print ()
    altur += 1
    largur = 1
