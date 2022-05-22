#ex1

def separar (spr):
    xrr = spr.split(" ")
    return unica(xrr)

def unica(xrr):
    posicao = 0
    unicalista = []
    posicaodic = {}
    posicaounicadic = {}

    for palavra in xrr:
        if palavra not in unicalista:
            unicalista.append(palavra)
            posicaounicadic[palavra] = posicao
        posicaoguardada(palavra, posicao, posicaodic)
        posicao = posicao+1
    print("palavras unicas: ", unicalista)
    return construir(posicaodic)
        
def posicaoguardada(palavra, posicao, posicaodic):
    xrr =[]
    if palavra in posicaodic:
        xrr = posicaodic[palavra]
        xrr.append(posicao)
        posicaodic[palavra] == xrr
    
    else:
        xrr.append(posicao)
        posicaodic[palavra] = xrr
    
    return posicaodic

def construir(posicaodic):
    sorted = []
    sentence = []

    for x, y  in posicaodic.items():
        for u in y:
            sorted.append(u)
        
        sorted.sort()
    
    for num in sorted:
        for x, y in posicaodic.items():
            for u in range(len(y)):

                if num == posicaodic[x][u]:
                     sentence.append(x)
    return sentence

texto=(input("introduza uma frase: "))
print(separar(texto))



    

