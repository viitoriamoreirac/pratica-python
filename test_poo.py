def main():

    nome = input("Seu nome: ")
    acai_ou_creme = input("Açaí ou creme de cupuaçu? ")
    tamanho = input("Tamanho P, M ou G? ")
    print ("Os acompanhamentos são: Banana, Morango, Kiwi, Ovomaltine, Granola, Paçoca, Confete, Leite em pó, Oreo e Farinha Lactea. (Você pode escolher 3)")
    acomp1 = input("Escolha o primeiro acompanhamento: ")
    acomp2 = input("Escolha o segundo acompanhamento: ")
    acomp3 = input("Escolha o terceiro acompanhamento: ")
    cobertura = input ("Cobertura de leite condensado, morango ou chocolate? ")

    pedido = pedidos(nome, acai_ou_creme, tamanho, acomp1, acomp2, acomp3, cobertura)

    pedido.imprime_pedido()

class pedidos:
    def __init__(self, nome, acai_ou_creme, tamanho, acomp1, acomp2, acomp3, cobertura):
        self.nome = nome
        self.acai_ou_creme = acai_ou_creme
        self.tamanho = tamanho
        self.acomp1 = acomp1
        self.acomp2 = acomp2
        self.acomp3 = acomp3
        self.cobertura = cobertura

    def imprime_pedido(self):
        print ("Pedido de %s: %s %s com %s, %s, %s e cobertura de %s"%(self.nome,self.acai_ou_creme,self.tamanho,self.acomp1,self.acomp2,self.acomp3,self.cobertura))

main()
