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
    
    sep_frases = [frase for sentenca in sep_sentencas for frase in separa_frases(sentenca)] #aplicado o list comprehension para pegar todas as frases
    
    
    sep_palavras = []
    for palavras in sep_frases:
        sep_palavras.extend(separa_palavras(palavras))
    
    #sep_palavras = [separa_palavras(palavra) for palavras in sep_frases for palavra in palavras] #aplicado o list comprehension para pegar todas as palavras        
    numero_palavras = len(sep_palavras)
    
    numero_caracteres = 0
    for caractere in sep_palavras:
        numero_caracteres += len(caractere)
    
    caractere_por_frase = 0
    for caractere in sep_frases:
        caractere_por_frase += len(caractere)

    palavras_unicas = n_palavras_unicas(sep_palavras)
    palavras_diferentes = n_palavras_diferentes(sep_palavras)
    tam_senteca = 0
    for sentença in sep_sentencas: 
        tam_senteca += len(sentença)

    num_frases = sum((len(sep_sentencas)) for sentenca in sep_sentencas)

    wal = numero_caracteres/numero_palavras
    hlr = palavras_unicas / numero_palavras
    ttr = palavras_diferentes / numero_palavras
    sal = tam_senteca/len(sep_sentencas)
    sac = len(sep_frases) / len(sep_sentencas)
    pal = caractere_por_frase / len(sep_frases)

    return [wal, ttr, hlr, sal, sac, pal]

def compara_assinatura(as_a, as_b): 
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.''' 
    s_ab = 0 #grau de similaridade extre os textos A e B
    cont = 0;sub = 0; traco = []
    while cont < 6:
        sub = as_a[cont] - as_b[cont]
        traco.append(abs(sub))
        cont += 1

    s_ab = sum(traco)/6
     
    return s_ab

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero 
    (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinatura = []; compara = 0; comparacoes = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        compara = compara_assinatura(assinatura, ass_cp)
        comparacoes.append(compara)

    menor = min(comparacoes)
    indice = comparacoes.index(menor) + 1

    return indice

assinatura = le_assinatura()
textos = le_textos()

num_texto = avalia_textos(textos, assinatura)
print("O autor do texto",num_texto, "está infectado com COH-PIAH")

