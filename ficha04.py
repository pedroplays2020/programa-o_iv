#ex1

from resource import prlimit
from tracemalloc import start


a =0 
e=0
i=0
o =0
u =0


for vogal in str:
    if vogal == "a":
        a+=1

    elif vogal =="e":
        e+=1
    elif vogal =="i":
        i+=1

    elif vogal =="o":
        o+=1


    elif vogal =="u":
        u+1
print("Ocorrência da vogal a: ",str.count(a))
print("Ocorrência da vogal e: ",str.count(e))
print("Ocorrência da vogal i: ",str.count(i))
print("Ocorrência da vogal o: ",str.count(o))
print("Ocorrência da vogal u: ",str.count(u))


#ex2

start= str.index("b")
i=str.index("a")
print("a)",str[start:len(str)])
print ("b )",str[0:start])
print("c)",i) 
print("d)", str.count("a"))
print("e", len(str))
print("f)", str.replace("", "#"))
print("g) a posição da palavra tejo: ", str.find("tejo"))




