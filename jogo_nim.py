def usuario_escolhe_jogada(n,m):
    peças_usuario = int(input("Quantas peças você vai tirar?"))
                        
    while peças_usuario > m or peças_usuario < 1 or peças_usuario > n:
        print ("Oops! Jogada inválida! Tente de novo.")
        peças_usuario = int(input("Quantas peças você vai tirar?"))
    if peças_usuario == 1:
        print ("Você tirou uma peça.")
        return 1
    else:
        print("Você tirou",peças_usuario,"peças.")
        return peças_usuario


def computador_escolhe_jogada(n,m):
    if n % (m+1) == 0:
        if m == 1:
            print ("O Computador tirou uma peça.")
            return 1
        else:
            print ("O computador tirou",m,"peças.")
            return m
    else:
        peças_computador = n % (m+1)
        if peças_computador == 1:
            print ("O Computador tirou uma peça.")
            return 1
        else:
            print ("O computador tirou",peças_computador,"peças.")
            return peças_computador

        

def partida():
    pontos_computador = 0
    pontos_usuario = 0
    
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    if n % (m+1) == 0:
        print ("Você começa!")
        
        while n > 0:
            jogada = usuario_escolhe_jogada(n,m)
            n -= jogada
            if n == 1:
                print ("Agora resta apenas uma peça no tabuleiro")
            if n == 0:
                print ("Agora restam",n,"peças no tabuleiro")
                pontos_usuario = pontos_usuario + 1
                print ("Você ganhou!")
            else:
                print ("Agora restam",n,"peças no tabuleiro")
                

            if n > 0:
                jogada_computador = computador_escolhe_jogada(n,m)
                n -= jogada_computador
                if n == 1:
                    print ("Agora resta apenas uma peça no tabuleiro")
                if n == 0:
                    print ("Agora restam",n,"peças no tabuleiro")
                    pontos_computador += 1
                    print ("O Computador ganhou!")
                else:
                    print ("Agora restam",n,"peças no tabuleiro")
                
    else:
        print ("Computador começa!")
        
        while n > 0:
            jogada_computador = computador_escolhe_jogada(n,m)
            n -= jogada_computador
            if n == 1:
                print ("Agora resta apenas uma peça no tabuleiro")
            if n == 0:
                print ("Agora restam",n,"peças no tabuleiro")
                pontos_computador += 1
                print ("O computador ganhou!")
            else:
                print ("Agora restam",n,"peças no tabuleiro")
                
            if n > 0:
                jogada = usuario_escolhe_jogada(n,m)
                n -= jogada
                if n == 1:
                    print ("Agora resta apenas uma peça no tabuleiro")
                if n == 0:
                    print ("Agora restam",n,"peças no tabuleiro")
                    pontos_usuario = pontos_usuario + 1
                    print ("Você ganhou!")
                else:
                    print ("Agora restam",n,"peças no tabuleiro")
    if pontos_usuario > pontos_computador:
        return 0
    else:
        return 1


def campeonato():
    print ("**** Rodada 1 ****")
    rodada = partida()
    print ("**** Rodada 2 ****")
    rodada_2 = partida()
    print ("**** Rodada 3 ****")
    rodada_3 = partida()
    soma = rodada + rodada_2 + rodada_3
    print ("**** Final do campeonato! ****")

    if soma == 0:
        print ("Placar: Você 3 x 0 Computador")
    if soma == 1:
        print ("Placar: Você 2 x 1 Computador")
    if soma == 2:
        print ("Placar: Você 1 x 2 Computador")
    if soma == 3:
        print ("Placar: Você 0 x 3 Computador")




print ("Bem-vindo ao jogo do NIM! Escolha:")
print ("1 - para jogar uma partida isolada")
print ("2 - para jogar um campeonato 2")

partida_ou_campeonato = int(input())

while partida_ou_campeonato != 1 and partida_ou_campeonato != 2:
    print("Escolha 1 ou 2")
    partida_ou_campeonato = int(input())
                                
if partida_ou_campeonato == 1:
    print ("Você escolheu uma partida isolada!")
    partida()
else:
    if partida_ou_campeonato == 2:
        print ("Você escolheu campeonato!")
        campeonato()
