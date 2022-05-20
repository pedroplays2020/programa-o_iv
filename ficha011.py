#ex1

def separar (spr):
    xrr = x.split("")
    return unica(spr)

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
        posicao = pos+1
    print("palavras uniccas: ", unicalista)
    return construir(posicaodic)
        
def posicaoguardada(palavra, posicao, posicaodic):
    xrr =[]
    if palavra in posicaodic:
        xrr = posicaodic(palavra)
        xrr.append(posicao)
        posicaodic(palavra) == xrr
    
    else:
        xrr.append(posicao)
        posicaodic(palavra) == xrr
    
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
            for u in range(len(v)):

                if num == posicaodic[x][u]:
                    return sentence

texto=(input("introduza uma frase: "))
print(separar(texto))



    

