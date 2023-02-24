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
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    sep_sentencas = (separa_sentencas(texto))

    sep_frases = []
    for frase in sep_sentencas:
        sep_frases.append((separa_frases(frase)))

    sep_palavras = [];
    for palavras in sep_frases:
        for palavra in palavras:
            sep_palavras.append((separa_palavras(palavra)))
   
    junta_palavras = []
    for sublista in sep_palavras:
        junta_palavras.extend(sublista)

    numero_palavras = len(junta_palavras)
    
    numero_caracteres = 0
    for caractere in junta_palavras:
        numero_caracteres += len(caractere)

    palavras_unicas = n_palavras_unicas(junta_palavras)
    palavras_diferentes = n_palavras_diferentes(junta_palavras)
    tam_senteca = 0
    for sentença in sep_sentencas: 
        tam_senteca += len(sentença)

    num_frases = sum((len(sep_sentencas)) for sentenca in sep_sentencas)

    wal = numero_caracteres/numero_palavras
    hlr = palavras_unicas / numero_palavras
    ttr = palavras_diferentes / numero_palavras
    sal = tam_senteca/len(sep_sentencas)
    sac = len(sep_frases) / num_frases
    pal = numero_caracteres / len(sep_frases)

    return [wal, ttr, hlr, sal, sac, pal]

def compara_assinatura(as_a, as_b): 
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
textos = le_textos()

assinaturas = []
cont=1
for texto in textos:
    print("Assinatura do texto",cont,calcula_assinatura(texto))
    assinaturas.append(calcula_assinatura(texto))
    cont+=1


#avalia = avalia_textos(textos, assinatura)




'''
texto1 = texto[0]
sep_sentencas = (separa_sentencas(texto1))

print("Sentenças separadas: \n",sep_sentencas)


sep_frases = []
for frase in sep_sentencas:
    sep_frases.append((separa_frases(frase)))
    
print("Frases separadas: \n",sep_frases)
    

sep_palavras = []
for palavras in sep_frases:
    for palavra in palavras:
        sep_palavras.append((separa_palavras(palavra)))
print("Palavras separadas: \n",sep_palavras)

junta_palavras = []
for sublista in sep_palavras:
    junta_palavras.extend(sublista)

palavras_unicas = 0
for palavras_uni in sep_palavras:
    palavras_unicas = n_palavras_unicas(junta_palavras)

palavras_diferentes = 0
for palavras_dif in sep_palavras:
    palavras_diferentes = n_palavras_diferentes(junta_palavras)

print("Número de palavras únicas: ", palavras_unicas)
print("Número de palavras diferentes: ", palavras_diferentes)
'''