largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

largur = 1
altur = 1

while altur <= altura:
    while largur <= largura:
        if altur == 1 or altur == altura or largur == 1 or largur == largura:
            print ("#", end="")
        if altur !=1 and altur != altura and largur != 1 and largur != largura:
            print (" ", end="")
        largur += 1
    print ()
    altur += 1
    largur = 1
