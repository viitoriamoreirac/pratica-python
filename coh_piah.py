import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    i = 0
    similaridade = []
    while i < 6:
        a = as_a[i]
        b = as_b[i]
        traço = abs(a - b)
        similaridade.append(traço)
        i += 1
    i = 0
    soma = 0
    while i < 6:
        soma = soma + similaridade[i]
        i += 1
    Sab = soma / 6
    return Sab
        

def calcula_assinatura(texto):
    
    #tamanho médio das palavras   LEMBRAR DE REMOVER OS PRINTS!!!!!
    lista_palavras = []
    lista_frases = []
    lista_sent = separa_sentencas(texto)
    for sentenca in lista_sent:
        novas_frases = separa_frases(sentenca)
        lista_frases.extend(novas_frases)
    for frase in lista_frases:
        novas_palavras = separa_palavras(frase)
        lista_palavras.extend(novas_palavras)
    quantidade = len(lista_palavras) - 1
    i = 0
    soma = 0
    while i <= quantidade:
        palavra = lista_palavras[i]
        soma = soma + len(palavra)
        i += 1
    média_de_caracteres = soma / len(lista_palavras)

    #relação Type_token
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    type_token = palavras_diferentes / len(lista_palavras)

    #Razão Hapax Legomana
    palavras_unicas = n_palavras_unicas(lista_palavras)
    hapax_legomana = palavras_unicas / len(lista_palavras)

    #média de caracteres por sentença
    quantidade1 = len(lista_sent) - 1
    i = 0
    soma1 = 0
    while i <= quantidade1:
        sentença = lista_sent[i]
        soma1 = soma1 + len(sentença)
        i += 1
    media_de_caracteres_sent = soma1 / len(lista_sent)

    #Complexidade da sentença
    complexidade = len(lista_frases) / len(lista_sent)

    #Tamanho das frases
    quantidade2 = len(lista_frases) - 1
    i = 0
    soma2 = 0
    while i <= quantidade2:
        frase = lista_frases[i]
        soma2 = soma2 + len(frase)
        i += 1
    media_de_caracteres_pal = soma2 / len(lista_frases)
    
    return [média_de_caracteres, type_token, hapax_legomana, media_de_caracteres_sent, complexidade, media_de_caracteres_pal]

def avalia_textos(textos, ass_cp):
    quantidade = len(textos) - 1
    i = 0
    assinaturas = []
    while i <= quantidade:
        assinatura = calcula_assinatura(textos[i])
        assinaturas.append(assinatura)
        i += 1
        
    quantidade = len(assinaturas) - 1
    i = 0
    assinaturas_comparadas = []

    ass_cohpiah = ass_cp
    while i <= quantidade:
        ass_sp = assinaturas[i]
        assinaturas2 =  compara_assinatura(ass_sp,ass_cohpiah)
        i += 1
        assinaturas_comparadas.append (assinaturas2)
    cohpiah = min(assinaturas_comparadas)
    resultado = assinaturas_comparadas.index(cohpiah)
    
    return resultado + 1
        
    


ass_cp = le_assinatura()
textos = le_textos()

resultado = avalia_textos(textos,ass_cp)

print ("O autor do texto",resultado,"está infectado com COHPIAH")

















    
