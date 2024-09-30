#coding utf-8

nome = 'gab' # string, palavra/texto etc
altura = 1.67 #float, ponto flutuante, número com vírgula
numeroSapato = 37 #int: inteiro

nome2 = 'bag'
altura2 = 76.1
numeroSapato2 = 73

#todas as entradas de teclado ele entende como uma string, então tenho que converter para o type
print("Entre com o nome: ", end='') 
nome3 = input() # isso vai ser lido string
print("Entre com a altura: ", end='')
altura3 = float(input())
numeroSapato3= int(input("Entre com o número do seu sapato: "))

print(type(nome))
print(type(altura))
print(type(numeroSapato))

print(nome+nome2+nome3)
print(altura+altura2+altura3)
print(numeroSapato+numeroSapato2+numeroSapato3)



