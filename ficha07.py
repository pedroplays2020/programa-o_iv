
from itertools import count
import random
import math

#ex1

def vetor(xrr):
    sum = 0
    for x in xrr:
        if x > 20:
            sum = sum + x       
    return sum  
xrr=[]
for x1 in range(0,5):
    xrr.append(float(input("introduza um numero: ")))
print(vetor(xrr))


#ex2
yrr=[]
def matriz(yrr):
    xr=[]
    count=0
    for x1 in range(0,4):
        for x2 in range(0,3):
            if yrr [x1][x2]<0:
                count+=1
    return "Quantidade de valores negativos: ", count

yrr2=[[-1,2,3],
     [4,5,6],
     [7,8,9],
     [10,11,12]]

for x1 in range(0,4):
    for x2 in range(0,3):
        t = random.randint(-100,100)
        r= yrr2[x1][x2]
print(yrr2)
print(matriz(yrr2))
     





   
  


