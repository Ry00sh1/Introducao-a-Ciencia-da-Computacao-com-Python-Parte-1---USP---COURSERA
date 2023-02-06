n = int(input("Digite um número inteiro: "))
lista = list(str(n))
i = len(str(n)) 
soma = 0

while i!=0:
    soma = soma + int(lista[i-1])
    i = i-1
print(soma)