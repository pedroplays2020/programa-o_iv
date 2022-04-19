#ex1

from array import array


i=0
coun= 0
sum=0
n1=0
n2=0
while i < 7:
    x= int(input('introduza um valor'))
    print(x)
    i +=1
    if x >=18 and x<=28:
        coun= coun+1
        sum=(x+sum)
    n1=(n1+x)
    n2=n2+1
if coun>0:
    sum=sum/coun
    print(sum)
if n2>0:
    n1=n1/n2

    print(n1)


#ex2
nh_ex=0
sb=0
def ordenadoliquido(sb):
    if sb > 1000:
        sal= sb-sb*0.20
    elif sb >=600 and sb <1000:
        sal= sb-sb*0.15
    else:
        sal= sb-sb*0.10
    return " o  salario vencido", sb
    
n1=int(input('numero do empregado'))
nh= int(input('numero de horas trabalhadas '))
vh=int(input('valor de hora'))

if nh<35:
    sb = nh* vh
else:

    nh_ex = sb*vh

print(sb)


#ex3 
def intem (arr):
    i = sorted(arr)
    return "o valor intermédio: ", i[1]
arr=[]

n1=int(input("introduza um numero: "));
n2=int(input("introduza um numero: "));
n3=int(input("introduza um numero: "));
arr.append(n1)
arr.append(n2)
arr.append(n3)
print(intem(arr))








 
 










    

