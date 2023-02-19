def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma

num_inteiros = []
numero_add = 1
while numero_add > 0:
    numero_add = int(input('Digite um número inteiro: '))
    num_inteiros.append(numero_add)
num_inteiros.remove(0)    
num_inteiros.sort()
print("lista formada",num_inteiros)
print("Resultado da soma =", soma_elementos(num_inteiros))