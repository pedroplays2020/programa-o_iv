import math

#ex1
nota=int(input('introduza a nota:'))
if nota>=0 and nota<=20:
    print('a nota é valida')
else:
    print('a nota está errada, pois deve estar entre 0 e 20')
    print(nota)


#ex2

def temp (c):
        return c* 1.8+32
for  c  in range (10, 20):
        print(temp(c))




#ex3 
n=int(input('Digite um numero: '))

if n<=0:
    print("valor errado, termina o programa"),n

elif n>= 0:
    print(n) 
    for k in range(n,0,-1):
        print(k)


#ex4

def pm(x):
    return 2* math.pi * x
print(pm(int(input('introduza um perimetro '))))

 







    







    













