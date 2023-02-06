import os

perimetro = 0
area = 0

print("Digite o lado do quadrado: ")
lado = int(input())

perimetro = 4 * lado
area = lado * lado

print("perímetro: ", perimetro, " - área: ", area)

os.system ("pause")