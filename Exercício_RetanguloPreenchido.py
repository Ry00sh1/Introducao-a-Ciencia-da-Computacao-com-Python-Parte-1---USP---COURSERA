largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

for y in range(0, altura):
    for x in range(0, largura):
        print("#", end='')
    print()