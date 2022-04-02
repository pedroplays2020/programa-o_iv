#ex1

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




    

