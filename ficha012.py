#ex1
conta = 0
vogais = 0
tpalavras = 0
palavra_x = []
#linhas = []
try:
    with open('ficha012teste.txt') as x:
        linhas = x.readlines()
    x.close()
except:
    print('erro ao abrir o ficheiro')
print(linhas)

for texto in linhas:
    xtr = texto

    vogais += xtr.conta("a")+xtr.conta("e") + \
        xtr.conta("i")+xtr.conta("o")+xtr.conta("u")

    palavra_x.append(xtr.split(" "))

    for y in range(len(xtr)):
        if xtr[y].isalpha():
            conta+=1
for linha in range (len(palavra_x)):
    for palavra  in range(len(palavra_x[linha])):
        if palavra_x[linha][palavra] !=  "\n":
            tpalavras += 1
        else:
            continue

print("vogais: ", vogais)
print("consoantes: ",conta-vogais)
print("palavras: ", len(linhas))




