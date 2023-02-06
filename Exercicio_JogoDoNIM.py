print("Bem-vindo ao jogo do NIM")

def principal():
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
            return principal()

def pecas_Iniciais(n):
    n = int(input("Digite a quantidade de peças iniciais: "))
    return

def max_Rodada(m):
    m = int(input("Máximo de peças que é possível retirar nessa rodada: "))
    return

def partida_Isolada(): 
    x = 1; n = 0; m = 0
    print("**** Rodada %d ****"%(x))
    pecas_Iniciais(n);print(pecas_Iniciais(n))    
    max_Rodada(m);print(max_Rodada(m))

def campeonato():
    x = 1
    print("**** Rodada %d ****"%(x))
    
if principal()==1:
    print(partida_Isolada())
else:
    print(campeonato())