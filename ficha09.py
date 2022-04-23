#ex1


from re import X


class verificaparimapar():
    par = 2
    impar = 1

def verpar(lista):
    lista=[]
    for x in lista:
        if x %2==x:
            lista.append(x)
    return lista

def convertuplos(texto):
    verpar(texto)
    lista=texto.split(",")
    
    return tuple(verificaparimapar(lista,verificaparimapar.par.value))

def var(xy,a):
    xrr=[]
    for y in xy:
        if y%a==0:
            xrr.append(y)
    return xrr
print(convertuplos(input("Insira um tuplo de inteiros positivos:")))


#ex2
tuplo=(10,15,3,6,99,45,63,30,344,22,4,25,10)

print("a)", len(tuplo))
print("b)", max(tuplo), min(tuplo))
tuplo2=(21, 53, 23, 54,22,2,1,13)
tuplo3= tuplo + tuplo2
print("c)", tuplo3)
print("d)",verificaparimapar (tuplo3,verpar.impar.value))
a=5
print("e)", var,(tuplo3, a))






    
        