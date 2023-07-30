def main():
    carro1 = carro('FordKa',2016,'branco',80)
    carro2 = carro('Onix',2018,'vinho',95)

    carro1.pare()
    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)
    carro2.pare()


class carro:
    def __init__(self,modelo,ano,cor,vel_max):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.vel = 0
        self.velocidademax = vel_max

    def imprima(self):
        if self.vel == 0:
            print ( "%s %s %d está parado"%(self.modelo, self.cor, self.ano)    )
        elif self.vel < self.velocidademax:
            print ( "%s %s indo a %d Km/h"%(self.modelo,self.cor,self.vel)  )
        else:
            print ( "%s %s indo muito rapidooooo!"%(self.modelo,self.cor)  )

    def acelere(self, velocidade):
        self.vel = velocidade
        if self.vel > self.velocidademax:
            self.vel = self.velocidademax
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

main()
