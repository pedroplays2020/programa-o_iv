#ex1
from time import time

conta = 0
vogais = 0
tpalavras = 0
palavra_x = []
linhas = []
try:
    with open('ficha012teste.txt') as x:
        linhas = x.readlines()
    x.close()
except:
    print('erro ao abrir o ficheiro')
print(linhas)

for texto in linhas:
    xtr = texto

    vogais += xtr.count("a")+xtr.count("e") + \
        xtr.count("i")+xtr.count("o")+xtr.count("u")

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

#ex2

palavras_y = []
unica=[]
try:
    with open('ficha12teste.txt') as x:
        linhas = x.readlines()
    x.close()
except:
    print('problema ao abrir o ficheiro')

for texto in linhas:
    xtr= texto
    palavras_y.append(xtr.split(None))

for linha in range(len(palavras_y)):
    for palavra in range(len(palavras_y[linha])):
        if palavras_y[linha][palavra] != " " and palavras_y[linha][palavra] not in unica:
            unica.append(palavras_y[linha][palavra])
        else:
            continue
try:
    x = open('ficha12novoteste.txt', 'a')
    print("criando o ficheiro....")
    time.sleep(5)
    x.close()
except:
    print('falha na criação do ficheiro ou ficheiro já existe')

with open('ficha12novoteste.txt', 'r+') as c:
    for palavra in range (len(unica)):
        c.write(unica[palavra])
        c.write("\n")



 




