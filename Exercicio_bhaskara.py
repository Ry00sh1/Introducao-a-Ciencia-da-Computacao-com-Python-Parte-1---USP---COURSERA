import math
print("Digite os valores de A, B e C, respectivamente")
a = float(input())
b = float(input())
c = float(input())

delta = ((b**2)-4*a*c)


if delta > 0:
	x1 = (-b + math.sqrt(delta))/(2*a)
	x2 = (-b - math.sqrt(delta))/(2*a)
	print("Primeira raíz = ", x1)
	print("Segunda raíz = ", x2)
else:
	print("Sem raízes reais")
