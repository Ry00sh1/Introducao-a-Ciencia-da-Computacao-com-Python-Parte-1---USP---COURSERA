def remove_repetidos(lista):
    sem_repetidos = []
    for i in lista:
       if i not in sem_repetidos:
            sem_repetidos.append(i)
    return sem_repetidos 

num_inteiros = []
numero_add = 1
while numero_add > 0:
    numero_add = int(input('Digite um número inteiro: '))
    num_inteiros.append(numero_add)
num_inteiros.remove(0)    
num_inteiros.sort()
print(num_inteiros)
print("Lista excluindo os números repetidos: ", remove_repetidos(num_inteiros))

