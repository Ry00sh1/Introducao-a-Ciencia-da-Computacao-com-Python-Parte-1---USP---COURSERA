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

def calcula_assinatura(texto): 
    '''Primeira variavel a ser resolvida'''
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #texto = str(input(le_textos())) 
    '''print(le_assinatura(texto))'''
   
    
 
    
    pass

def compara_assinatura(as_a, as_b): 
    '''Segunda variavel a ser resolvida'''
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.''' 
    S_ab = 0 #grau de similaridade extre os textos A e B
    F_ia = 0 #valor de cada traço linguístico i no texto A
    F_ib = 0 #valor de cada traço linguístico i no texto B
     
    pass

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero 
    (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    pass

#assinatura = le_assinatura()
texto = le_textos()

texto1 = texto[0]
sep_sentencas = (separa_sentencas(texto1))

sep_frases = []
for frase in sep_sentencas:
    sep_frases.append((separa_frases(frase)))

sep_palavras = []
for palavras in sep_frases:
    for palavra in palavras:
        sep_palavras.append((separa_palavras(palavra)))
print(sep_palavras)
'''
for palavras in sep_palavras:
    palavras_unicas = n_palavras_unicas(sep_palavras[palavras])

palavras_unicas = n_palavras_unicas(sep_palavras[0])
palavras_diferentes = n_palavras_diferentes(sep_palavras)
print("Palavras que aparecem uma única vez:",palavras_unicas)
print("Palavras diferentes utilizadas:",palavras_diferentes)

'''