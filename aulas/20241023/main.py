#coding: utf-8

# função que apresenta nomes aprovados com compreensão de listas -> mais compacto
def script01():
    nomes1 = ["Larissa", "Rafael", "Marcos", "Joao"]
    nomesAprovados = [(nome+" Aprovou") for nome in nomes1]
    print(nomesAprovados)

# função que é igual a de cima, mas mais extenso:
def script02():
    nomes1 = ["Larissa", "Rafael", "Marcos", "Joao"]
    strAprovados = " Aprovou"
    nomesAprovados = []
    for nome in nomes1:
        saida = nome+strAprovados
        nomesAprovados.append(saida)
    print(nomesAprovados)

#funçao que apresenta nomes reprovados com compreensão de listas:
def script03():
    nomes2 = ["Ana", "Carla", "Rotundo", "Henrique"]
    strReprovados = " Reprovou"
    nomesReprovados = [(nome+strReprovados) for nome in nomes2]
    print(nomesReprovados)

# função dentro de função:
def script04():
    nomes1 = ["Larissa", "Rafael", "Marcos", "Joao"]
    nomes2 = ["Ana", "Carla", "Rotundo", "Henrique"]

    #essas duas próximas funções NÃO podem ser utilizadas fora da função script04 -> usado para quando NÃO quero utilizar ela fora
    def aprovarPessoa(nomeApr):
        strg = " Aprovado"
        return nomeApr+strg
    def reprovarPessoa(nomeRepr):
        strg = " Reprovado"
        return nomeRepr+strg
    
    nomesAprovados = [aprovarPessoa(nome) for nome in nomes1]
    nomesReprovados = [reprovarPessoa(nome) for nome in nomes2]
    
    print(nomesAprovados)
    print(nomesReprovados)

# função que testa se número é par de uma forma obscura
def ehPar(num):
    if num%2: #zero no python significa False
        return False
    else:
        return True

#função que testa se número é par de forma mais clara:
def ehPar2(num):
    if (num%2 == 0):
        return True
    else:
        return False

def script05():
    num = [i for i in range(20) if ehPar(i)]
    print(num2)
    num2 = [i for i in range(20) if ehPar2(i)]

if __name__ == "__main__":
    script01()
    script02()
    script03()
    script04()
    script05()