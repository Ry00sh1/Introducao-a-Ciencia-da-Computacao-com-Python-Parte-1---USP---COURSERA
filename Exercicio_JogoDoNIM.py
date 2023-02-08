print("Bem-vindo ao jogo do NIM! Escolha:")

def inicio():
    print("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n")

    x = int(input())
    
    if (x!=1) or (x!=2):
        if x == 1:
            print("Voce escolheu uma partida isolada!\n")
            return 1
        elif x == 2:
            print("Voce escolheu um campeonato!\n")
            return 2
        else:
            print("Digite uma opção válida\n")
            x = 0
            return inicio()

def computador_escolhe_jogada(n,m):

def usuario_escolhe_jogada(n,m):

def partida(n,m):
    
   
    if n%(m+1) == 0:
        print("Você começa!")
        while n!= 0:
            print(usuario_escolhe_jogada())
    else:
        print("Computador começa!")
        while n!= 0:
            print(computador_escolhe_jogada())

def partida_Isolada(): 
    print("Voce escolheu uma partida isolada!")
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    print(partida())

def campeonato():
    print("Voce escolheu um campeonato!")

    for x in range(4):
        n = int(input("Quantas peças?"))
        m = int(input("Limite de peças por jogada?"))
        print("**** Rodada %d ****"%x)
        print(partida())
    
if inicio()==1:
    print(partida_Isolada())
else:
    print(campeonato())