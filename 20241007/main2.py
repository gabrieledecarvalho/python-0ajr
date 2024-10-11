#coding: utf-8
#código da aula
import math

def Eq2grau(a,b,c): 
	Delta = math.pow(b,2)-4*a*c
	if (Delta>0): 
		#Há duas raizes reais distintas
		x1 = (-b-pow(Delta, 0.5))/(2*a)
		x2 = (-b+pow(Delta, 0.5))/(2*a)
		return x1,x2
	elif (Delta ==0):
		print("Há raiz única, Delta = ", Delta)
		return None
		
if __name__=="__main__": 
	Eq2grau(1,4,4)
	#print(f"As raizes são {x1} e {x2}")
