from calcbit import *
from conversoes import *

while(1):
	print(30*"-")
	print("Conversão de bases (a)")
	print("Operações com bits(b)")
	print("Sair (x)")
	print(30*"-")

	opcao = str(input("Digite a opção\n"))

	if opcao == 'a':
		print(30*"-")
		print("Conversão de bases")
		print(30*"-")
		inibase = int(input("Digite a base inicial\n"))
		finbase = int(input("Digite a base para conversão\n"))
		print("Digite o número na base ", inibase)
		num1 = str(input())
		
		if inibase == 10:
			resultado = intlista(decbase(int(num1),finbase))
		elif inibase == 16:
			resultado = hexabase(num1,finbase)
		elif inibase == 8:
			resultado = octabase(num1,finbase)
		elif inibase == 2:
			resultado = binbase(num1,finbase)

		print(15*"-")
		print("Resultado: ",resultado)
		print(15*"-")

	if opcao == 'b':
		while(1):
			print(30*"-")
			print("Soma de bits: (a)")
			print("Complemento de 1: (b)")
			print("Complemento de 2: (c)")
			print("Subtração: (d)")
			print("Voltar (x)")
			print(30*"-")
			
			opcaobit = str(input("Digite a opção\n"))
			
			if(opcaobit == 'a'):
				while(1):
					#bits = int(input("Range da soma\n"))
					num1 = str(input("Número 1\n"))
					num2 = str(input("Número 2\n"))
					if len(num1) == len(num2):
						break
					else:
						print(30*"-")
						print("Digite os números com um mesmo range")
						print(30*"-")
				
				resultado = intlista(somabit(num1,num2))
				
				print(15*"-")
				print("Resultado: ",resultado)
				print(15*"-")
			
			elif(opcaobit == 'b'):
				num1 = str(input("Digite um número\n"))
				
				resultado = intlista(complemento1(num1))
				
				print(15*"-")
				print("Resultado: ",resultado)
				print(15*"-")
			
			elif(opcaobit == 'c'):
				num1 = str(input("Digite um número\n"))
				
				resultado = intlista(complemento2(num1))
				
				print(15*"-")
				print("Resultado: ",resultado)
				print(15*"-")
				
			elif(opcaobit == 'd'):
				print(30*"-")
				print("Digite apenas a representação positiva em binário")
				print("A conversão será feita em complemento de 2\n")
				print(30*"-")
				bits = int(input("Bits de representação\n"))
				print(30*"-")
				print("Representação de ", -2**(bits-1), " a ", 2**(bits-1)-1)
				print(30*"-")		
							
				sinalnum1 = str(input("Sinal Número 1\n"))
				num1 = str(input("Número 1\n"))
				sinalnum2 = str(input("Sinal Número 2\n"))
				num2 = str(input("Número 2\n"))
				
				resultado = intlista(subtracao(bits,sinalnum1,num1,sinalnum2,num2))
				
				print(15*"-")
				print("Resultado: ",resultado)
				print(15*"-")
					
			elif(opcaobit == 'x'):
				break
	elif(opcao == 'x'):
				break
