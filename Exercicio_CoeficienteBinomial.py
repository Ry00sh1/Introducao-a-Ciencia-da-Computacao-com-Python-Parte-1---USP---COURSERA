def fatorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def coeficiente_binomial(n,k):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))

print("Digite os dois termos do coeficiente binomial: ")
x = int(input())
y = int(input())

print("Coeficiente Binomial = ",coeficiente_binomial(x,y))


