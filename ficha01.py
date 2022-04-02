#ex1
print('Viva Turma')

#ex2

def soma(a,b):
    return a+b

a= int(input('introduza um valor'))
b= int(input('introduza um valor'))
print(soma(a,b))


#ex3
n1=int(input('introduza um numero'))
n2=int(input('introduza o numero 2: '))
if n1 == n2:
     print('o numero é igual')
else:
    print('o numero é diferente')

#ex4

x=10
if x>=10:
    print('o numero inserido é maior ou igual a 10')
elif x<10:
    print('o numero inserido é menor que 10')


#ex5
def media(n1,n2):
    return (n1+n2)/2
n1=int(input('introduza um valor1:'))
n2=int(input('introduza um valor2:'))
print(media(n1,n2))


def ex6(a,b):
    return (a*b)/2

a=int(input("digite um numero: "))
b=int(input("digite um numero: "))
print(ex6(a,b))




#ex6
# def area(a,b):
#     return (a*b)/2
# a=int(input('introduza a altura'))
# b=int(input('introduza a base'))
# x=area(a,b)
# print(x)

#ex7

a=float(input('introduza a temperatura celsius'))
f=a*1.8+32
print('o valor da temperatura é'(f))






