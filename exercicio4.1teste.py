def main ():
    q = 1 #quantidade de alunos
    total = 0
    nota = 0
    
    qt = int(input("Qual a quantidade de alunos?"))

    while q <= qt:
        q = q + 1
        nota = float(input("Digite uma nota: "))
        total = total + nota

    media = total / qt
    print ("A nota média da turma é:",media)
    
main()
