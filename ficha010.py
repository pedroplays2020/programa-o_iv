#ex1

def  animal(nome, raca, dic):
    if nome !="fim" or raca !="fim":
        dic.update({nome:raca})
        return dic
    else:
        return dic

dic={"Ziggy: canario, Pluto: cao, Kitty: gato, Nemo: peixe, Mickey: rato"}
nome=2
raca=2
while(nome !="fim" or raca !="fim"):
    print("introduza novos dados de animais, para terminar digite fim")
    nome=input("aninal: ") 
    print("para terminar digite fim")
    if nome == "fim":
        break
    print(nome)
    raca=input("raça do animal: ")
    print("para terminar digite fim")
    print(raca)
    print(animal(nome, raca,dic))
print("terminado")
searc=input("procura: ")
for nome, raca in dic.items():
    if nome==searc or raca == searc:
       print(nome, raca)


