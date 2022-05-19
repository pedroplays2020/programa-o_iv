
import math

#ex1

def temp (c):
    return c*1.8+32
print(temp(float(input("introduza o seu valor em Celsius:  "))))

#ex2
def intem(arr):
    i= sorted(arr)
    return "o valor intermédio: ",i[1]

arr=[]
n1 = int(input("introduza num: "))
n2 = int(input("introduza num: "))
n3 = int(input("introduza num: "))

arr.append(n1)
arr.append(n2)
arr.append(n3)

print(intem(arr))


#ex3

def numprimo(x):
    if x % 1 ==0 and x % x == 0:
        return "1"
    else:
        return "0"
x=int(input("introduza um numero: "))
print(numprimo(x))

#ex4

num=[1,5,3,6,22,45,63,30,344,22,12,25,10]
print("a)", len(num))
print("b) maximo: ",max(num), "minimo: ", min(num))

num2=[21,53,23,54,22,2,1,13]

for x in num2:
    num.append(x)
print("c)", num)

num.sort()
print("d)", num)

before = 0 
y= num[0]
for x1 in num:
   now = num.count(x1)
   if now > before:
       before = now
       y = x1
print("e) ", y)


print("f)")
for x2 in num:
    print( x2, "-", end="")

for x3 in num:
    if x3 % 2 !=0:
        print("g), x3 impar: ", x3)
    if x3 % 5 == 0:
        print("h), multiplo de 5: ", x3)









