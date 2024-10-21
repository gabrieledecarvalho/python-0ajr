#coding: utf-8
import math

def equacao2grau(a,b,c): #melhor método
    delta = math.pow(b,2)-4*a*c
    #criando variáveis vazias antes de usá-las, é uma prática boa para não gerar algum erro e causar trabalho 
    x1=None
    x2=None
    if(delta>0):
        #há duas raízes reais distintas
        x1 = (-b-pow(delta,0.5))/(2*a)
        x2 = (-b+pow(delta,0.5))/(2*a)
    elif(delta == 0):
        print("há raíz única, delta = ", delta)
    else:
        print("raízes complexas, delta = ", delta)    
    return x1,x2,delta

def equacao2grauCapivara(a,b,c):
     delta = math.pow(b,2)-4*a*c
    if(delta>0):
        print("há duas raízes reais distintas")
        x1 = (-b-pow(delta,0.5))/(2*a)
        x2 = (-b+pow(delta,0.5))/(2*a)
        return x1,x2
    elif(delta == 0):
        print("há raíz única, delta = ", delta)
        x = -b/(2*a)
        return x, delta
    else:
        print("raízes complexas, delta = ", delta)
        return delta

if __name__=="__main__":
    saida = eq2grau(1,4,4)

    n = len(saida) #retorna o número de termos da variável saída
    for i in range(n):
         print(f"valor {i} de saída: ", saida[1])

    #x1, x2, delta = eq2grau(1,4,3)
    #print(f"as raúzes são {x1} e {x2}, delta = {delta}")