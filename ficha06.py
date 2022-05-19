#ex1 
import math

soma = 0
i= 20 
for x in range(i, 0, -2):
    soma +=x
print('Soma =', soma)


#ex2

lista1 = ["Iva", 25, "Rui", 19, "Rato", "abc", 33]
print("a)",lista1)
print("b)", lista1[2:5])
print("c)", lista1[:3])
print("d)", lista1[3:])

lista2 = ["Diogo", 45, "Miguel", 19, "Lixo", "agua", 63]
lista2.append(lista1)
print("e)", lista2)

#ex3

def volume_esfera(r):
    return (4*math.pi*math.pow(r,3))/3
print(volume_esfera(5))

#ex4
u=int(input("introduza um numero: "))

for x in range(1,i+1):
    print("*"*u)



