#ex1

from ast import Mult
from enum import Enum
import enum
class verpar (Enum):
    par=0
    impar=1
def verificaparimpar(lista, a ):
    
    listimp=[]
    for nu in lista:
        if nu % 2==a:
            listimp.append(nu)            
    return listimp  
def convertor(texto):
    listaA=[]
    lista=texto.split(",")
    for x in lista:
        listaA.append(int(x))
    return tuple(verificaparimpar(listaA,verpar.par.value))


def mtpl(ns,mult ):
    xrr=[]
    for x in ns:
        if x%mult==0:
            xrr.append(x)
    return xrr

print(convertor(input("Insira um tuplo de inteiros positivos: ")))




         
        
    
#ex2

tuplo = (10,15,3,6,99,45,63,30,344,22,4,25,10)


print("a)", len(tuplo))
print("b)", max(tuplo), min(tuplo))
tuplo2=(21, 53, 23, 54,22,2,1,13)
tuplo3= tuplo + tuplo2
print("c)", tuplo3)
print("d)",verificaparimpar (tuplo3,verpar.impar.value))
a=5    
print("e)", mtpl(tuplo3, a ))






    
        