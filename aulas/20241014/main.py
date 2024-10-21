#coding: utf-8
from array import array
import math as m

def scr0(): #criando alguns vetores e observando como eles se apresentam: 
    vA = [] #vetor vazio e de tamanho 0, criando como lista e não como tupla
    vB = [ None ] * 5 #vetor vazio e de tamanho 5
    vC = [1 , 3.4 , "A" , " IFSC ", 3.4] #vetor de tamanho 4 e com tipos diferentes
    print(vA) # imprime o vetor vA
    print(vB) # imprime o vetor vB
    print(vC) # imprime o vetor vC
    print("Numero de vezes que aparece 3.4: ", vC.count(3.4))
    print("Posição do primeiro 3.4 no vetor: ", vC.index(3.4)) #lembrando que posição se inicia no 0

def scr1(): # criando tuplas e observando como elas se apresentam e diferença em relação à lista
    tA = () #tupla vazia, inútil porque não pode sofrer alteração
    tB = (1 , 3.4 , "A", "IFSC" ) #tupla de tamanho 4 e com tipos diferentes
    lista1 = ["Rampa", "Descida", 11.34] # lista com vários tipos diferentes
    print("Tupla A", tA) # imprime a tupla tA
    print("Tupla B: ", tB) # imprime a tupla tB
    print("Lista 1: ", lista1)
    lista1[1] = "Subida"
    print("Lista 1 modificada: ", lista1)
    #tA[1] = "Modificado"
    #print("Tentativa de modificar a tupla A", tA)
    # ERRO : 'tuple' object does not support item assignment

def SaidaFuncao():
    a = 2.4
    b = 3.5
    return a,b
    #return [a,b] #forçando saída desprotegida, em lista, não em tupla

def testandoArray():
    ArrayFloat = array('f', [])
    for i in range(21):
        ArrayFloat.append(m.sqrt(i)) # append = colocar no final do vetor
    print(ArrayFloat)

def Comando_in(): # verificando se algo está dentro de algo
    frutas = ['maçã', 'abacate', 'açaí', 'pêra']
    print('maçã' in frutas) # maçã está em frutas ? true
    print(not 'cajá' in frutas) #cajá não está em frutas ? true
    print('bananta' not in frutas) # banana não está em frutas ? true
    print('cajá' in frutas) #cajá está em frutas? false
    teste = 'laranja' not in frutas
    if (teste):
        frutas.append('laranja')
        print(frutas)
    if ('banana' not in frutas):
        frutas.append('banana')
        print(frutas)
    fruta_teste = 'laranja'
    if(fruta_teste not in frutas):
        frutas.append(fruta_teste)
        print(f"{fruta_teste} adicionado ao vetor")
    else:
        print(f"{fruta_teste} já está no vetor")
    print(frutas)

def Comando_in_percorrimento(): # criando uma variável i que pode assumir qualquer tipo, o for percorre o vetor em seu comprimento inteiro
    vC = [1, 3.4, 'A', 'IFSC']
    for i in vC:
        print(i)
        print(type(i))
    # método mais eficiente porque não fica mudando toda hora qual o tipo do i:
    for i in range(len(vC)): # len(vC) = 4; range cria uma lista
        print( vC [i])
        print(type(i))

def comandoEnumerate():
    moedas = ['BRL', 'USD', 'EUR']
    for moeda in moedas: # mostrando os itens dentro de moedas
        print(moeda)
    for i, moeda in enumerate(moedas): #o enumerate gera uma tupla mas estou mostrando só as variáveis seapradas no print, por isso não é protegida
        print(i, moeda)
    for saida in enumerate(moedas): # escolhe mostrar como uma tupla, o enumerate gera uma tupla tal qual a saída de função
        print(saida)

def modificaVetor():
    vC = [1, 3.4, 'A', 'IFSC']
    vC[2] = 555 #mudando o tipo e o conteúdo
    vC[0] = 'Python'
    vC[1] = 3>2 #retorna booleano
    for i in vC:
        print(i)

if __name__=="__main__":
    #scr0()
    
    #scr1()

    #saida = SaidaFuncao() # saída protegida
    #print(saida) #o retorno dessa função vai sair em tupla, pra justamente proteger esses dados    #a,b = SaidaFuncao() #saída desprotegida
    #print(a,b)

    #testandoArray()
    
    #Comando_in()

    #Comando_in_percorrimento()

    #comandoEnumerate()

    modificaVetor()