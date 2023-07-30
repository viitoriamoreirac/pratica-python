def main ():
    rp = 0 #reprovados
    rc = 0 #recuperação
    ap = 0 #aprovados
    dm = 0 #desempenho muito bom
    t = 0 #total de alunos
    
    total = int(input("Qual o total de alunos?"))
    
    while t < total:
        nota = float(input("Digite a nota: "))
        if nota >= 3 and nota < 5: #recuperação
            rc = rc + 1
        if nota < 3: #reprovados
            rp = rp + 1
        if nota > 8: #desempenho muito bom
            dm = dm + 1
        if nota >= 5 and nota <= 8: #aprovados
            ap = ap + 1
        t = t + 1

    print ("Total de alunos:",total)
    print ("Número de alunos reprovados =",rp)
    print ("Número de alunos de recuperação =",rc)
    print ("Número de alunos aprovados =",ap)
    print ("Número de alunos com desempenho muito bom =",dm)

main ()
