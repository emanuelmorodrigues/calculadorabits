def somabit(bits,a,b):	
	num1 = []
	num2 = []
	vai1 = []
	resultado = []

	num1 = [int(i) for i in a]
	num2 = [int(i) for i in b]
	
	# Define lista Vai1
	# Primeiro adicionam-se zeros para as verificações não darem "fora de range"
	# Se a soma das parcelas mais vai1 for maior ou igual a dois, então
	# significa que "vai um" na soma de bits no índice antes do atual.
	# Define lista Vai1
	# Primeiro adicionam-se zeros para as verificações não darem "fora de range"
	# Se a soma das parcelas mais vai1 for maior ou igual a dois, então
	# significa que "vai um" na soma de bits no índice antes do atual.

	for i in range(bits):
		vai1.append(0)

	for i in range(-1,(-1)*bits,-1):
		if (num1[i] + num2[i] + vai1[i] >= 2):
			vai1[i-1] = 1

	# Soma bit
	# Se a soma das parcelas mais vai1 for igual a zero ou igual a dois, então
	# o resultado da soma será zero. 
	# Ex: 0+0 "zero e vai 0" ou 1+1 "zero e vai 1"
	# Senão se a soma das parcelas mais vai1 for igual a um ou igual a 3, então
	# a soma será um. 
	# Ex: 0+1 (um e vai 0) ou 1+1 mais vai 1 (um e vai 1)

	for i in range(-1,(-1)*bits-1,-1):
		if (num1[i] + num2[i] + vai1[i] == 0) or (num1[i] + num2[i] + vai1[i] == 2):
			resultado.append(0)
		elif (num1[i] + num2[i] + vai1[i] == 1) or (num1[i] + num2[i] + vai1[i] == 3):
			resultado.append(1)
	# Adiciona bits quanto o resultado é uma representação maior que o range
	# Se o i foi a ultima iteração e a soma das parcelas mais vai1 for 
	# maior ou igual a dois, então adicione um bit 1 a mais
		if i == (-1)*bits and vai1[i] + num1[i] + num2[i] >= 2:
			resultado.append(1)
	
	resultado.reverse()		
	return resultado
	
def complemento1(a):
	num1 = [int(i) for i in a]
	compnum1 = []
		
	for i in num1:
		compnum1.append(int(not bool(i)))
		
	return compnum1

def complemento2(a):
		um = []
		comp = complemento1(a)
		for i in range(0,len(comp)-1):
			um.append(0)
		um.append(1)
			
		resultado = somabit(len(comp),comp,um)
		return resultado
		
def subtracao(bits,asinal,a,bsinal,b):
	if(asinal == '+' and bsinal == '+'):
		print("Use a soma de bits")
		return ''
	
	if(asinal == '-'):
		num1 = complemento2(a)
	else:
		num1 = [int(i) for i in a]
	if(bsinal == '-'):
		num2 = complemento2(b)
	else:
		num2 = [int(i) for i in b]
	
	resultado = somabit(bits,num1,num2)
	
	if(len(resultado) > bits):
		del(resultado[0])
		
	return resultado
