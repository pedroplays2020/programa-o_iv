#ex1

a =0 
e=0
i=0
o =0
u =0


def frase(xtr):
    print("Ocorrência da vogal a: ",xtr.count("a"))
    print("Ocorrência da vogal e: ",xtr.count("e"))
    print("Ocorrência da vogal i: ",xtr.count("i"))
    print("Ocorrência da vogal o: ",xtr.count("o"))
    print("Ocorrência da vogal u: ",xtr.count("u"))
frase(xtr=input("introduza uma frase: "))




#ex2
def string(str):

    start= str.index("b")
    i=str.index("a")
    print("a)",str[start:len(str)])
    print ("b )",str[0:start])
    print("c)",i) 
    print("d)", str.count("a"))
    print("e", len(str))
    print("f)", str.replace("", "#"))
    print("g) a posição da palavra tejo: ", str.find("tejo"))
str="a amada lisboa e o rio tejo belo encantam toda a gente"
string(str.lower())

