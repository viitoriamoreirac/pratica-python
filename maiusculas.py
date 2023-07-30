''' função que recebe uma frase (string) e devolve uma outra string com as
    letras maiusculas desas string //  usar .ord para verificar a numeração
    da string e assim ir adicionando a outra'''


def maiusculas(frase):
    ''' percorrer cada string dessa frase e testar a numeração, se estiver
    dentro dos numeros de maiuscula, adicionar dentro da nova string que
    sera devolvida depois'''
    pos = 0
    new_string = ""
    while pos < len(frase):
        numeracao = ord(frase[pos])
        if numeracao > 64 and numeracao < 91:
            new_string += frase[pos]
        pos += 1
    return new_string
