#coding:utf-8
import prog3 as eq2 #importando um arquivo como se fosse uma biblioteca

print("Valor do name:", __name__) #protocolo de segurança para trabalhar com vários arquivos
if __name__=="__main__":
	resultado=eq2.Equacao2grau(1,4,3)
	print("x1 = ",resultado[0],"x2 = ", resultado[1],"Delta = ", resultado[2]) #vetores
	saida="x1 = {0:.2f}, x2 = {1:.2f} e Delta = {2:.2f}".format(resultado[0], resultado[1], resultado[2])
	print("Nova saída")
	print(saida)
