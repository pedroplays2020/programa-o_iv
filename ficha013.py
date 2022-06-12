#ex1

from cmath import sin, sqrt
import math as X


class empregado(object):
    def __init__(self, numero=0, nome='', salb=0):
        self.numero = numero
        self.nome = nome 
        self.salb = salb
        self.taxa = self.calctaxa()
        self.taxaIRS = self.calclIrs()
        self.SS = self.calcss()
        self.saliquido = self.calcsalliquido()

    def calctaxa(self):
        if self.salb >= 2000.00:
            taxa = 0.25
        if self.salb >= 1000.00 and self.salb < 2000.00:
            taxa = 0.20
        if self.salb < 1000.00:
            taxa = 0.75
        return taxa 
    
    def calclIrs(self):
        return (self.salb*self.taxa)

    def calcss(self):
        return (self.salb-self.taxaIRS)*0.11
    
    def calcsalliquido(self):
        return (self.salb-self.taxaIRS)-self.SS

nome =input("introduza um nome:  ")
numero = input("introduza um numero: ")
salbruto = float(input("introduza o seu salário:  "))
empr = empregado(numero,nome, salbruto)
print ("salário bruto", empr.salb)
print ("ss", empr.SS)
print ("irs", empr.taxaIRS)
print ("taxa", empr.taxa)
print ("salário liquido", empr.saliquido)


#ex2

class professor (empregado):
    def __init__(self, areaensino=[], numero=0 , nome='', salb=0):
        empregado.__init__(self, numero, nome, salb)
        self.areaensino = areaensino

ae = input("introduza as areas de ensino seraparadas por virguula:  ")
cadeira = ae.split(",") 
tea= professor(cadeira, numero, nome, salbruto)
print(" o salario bruto: ", tea.salb)
print("ss: ", tea.SS)
print("irs ", tea.taxaIRS)
print("taxa: ", tea.taxa)
print(" o salario liquido:  ",tea.saliquido)
print("area de ensino:",tea.areaensino)


#ex3 

class calculadora():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        if (self.a == 0 or self.b ==0):
            return "nao deve existir valores 0 na divisão"
        else:
            return self.a/self.b
    
    def soma(self):
        return self.a + self.b
    
    def subtrair(self):
        return self.a - self.b
    
    def quadrada(self):
        print("quadrado do 1º numero", X.sqrt(self.a),
        "\quadro do 2º numero: ", X.sqrt(self.b))

    def log (self):
        print("log do 1º numero: ", X.log10(self.a), 
        "\log do 2º numero: ", X.log10(self.b))
    
    def sin(self):
        print("sin do 1º numero:", X.sin(self.a),
        "\sin do 2º numero:", X.sin(self.b))

x1= int(input("introduza um numero: "))
x2= int(input("introduza um numero: "))

num= calculadora(x1, x2)
print("divisão: ",num.dividir())
print("multiplicação: ",num.multiplicar())
print("soma: ",num.soma())
print("subtração ",num.subtrair())

num.quadrada()
num.log()
num. sin()

       

    
        



















    
        