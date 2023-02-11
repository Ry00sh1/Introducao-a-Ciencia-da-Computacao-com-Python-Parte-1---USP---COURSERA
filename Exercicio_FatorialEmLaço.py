def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

n = 0

while n == 0:
    num = int(input("Digite um número inteiro positivo: "))
    while num>0:
        print("Fatorial de",num," :",fatorial(num))
        num = num - 1
    n = n-1
