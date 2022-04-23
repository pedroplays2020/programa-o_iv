#ex1

from re import sub


num = [1,5,3,6,22,45,63,30,344,22,12,25,10]
num.reverse()
print("a)", num)
num.sort()
print("b)", num)
num[-3:]
print("c)", num[-3:])


#ex2 

xtr=input("digite  uma frase: ")
subs= input("digite uma substring a ser substituída: ")
new=input("digite uma substring de substituição:")

if xtr.find(subs)==1:
    print("string não encontrada: ", subs)

xtr=xtr.replace(subs,new)
print(xtr)
