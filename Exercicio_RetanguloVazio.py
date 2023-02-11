l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))


for x in range(a):
    if x == 0 or x == a-1:
        for y in range(l):
            print("#", end='')
    else:
        for y in range(l):
            if y == 0 or y == l-1:
                print("#", end='')
            else:
                print(" ", end='')
    print()