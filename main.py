from calcbit import *


while(1):
	print("Soma de bits: (a)")
	print("Complemento de 1: (b)")
	print("Complemento de 2: (c)")
	print("Subtração: (d)")
	
	opcao = str(input("Digite a Opção\n"))
	
	if(opcao == 'a'):
		bits = int(input("Range da soma\n"))
		num1 = str(input("Número 1\n"))
		num2 = str(input("Número 2\n"))
		
		resultado = somabit(bits,num1,num2)
		
		print("\t", resultado, "\n\n")
	
	elif(opcao == 'b'):
		num1 = str(input("Digite um número\n"))
		
		resultado = complemento1(num1)
		
		print("\t", resultado, "\n\n")
	
	elif(opcao == 'c'):
		num1 = str(input("Digite um número\n"))
		
		resultado = complemento2(num1)
		
		print("\t", resultado, "\n\n")
		
	elif(opcao == 'd'):
		bits = int(input("Range da subtração\n"))
		sinalnum1 = str(input("Sinal Número 1\n"))
		num1 = str(input("Número 1\n"))
		sinalnum2 = str(input("Sinal Número 2\n"))
		num2 = str(input("Número 2\n"))
		
		resultado = subtracao(bits,sinalnum1,num1,sinalnum2,num2)
		
		print("\t", resultado, "\n\n")
			
	if(opcao == 'x'):
		break;
	
