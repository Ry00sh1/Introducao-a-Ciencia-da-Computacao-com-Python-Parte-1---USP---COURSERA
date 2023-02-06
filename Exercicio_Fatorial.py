def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

num = int(input("Digite o valor de n: "))
print(fatorial(num))
