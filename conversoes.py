dichexa = {
	0 : 0, 1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8,
	9 : 9, 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F',
	'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, 
	'7' : 7, '8' : 8, '9' : 9, 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13,	
	'E' : 14, 'F' : 15
}


def intlista(a):
	#Transforma a lista em um número inteiro
	resultado = ''
	for i in a:
		resultado += str(i)
	return int(resultado)
	
def hexalista(a):
	resultado = ''
	for i in a:
		resultado += str(i)
	return resultado

def lehexa(a):
	#Substitui letras do hexa para número inteiro (para conversões)
	num = [dichexa[i] for i in a]
	return num

def basedec(n,b):
	#Converte de "qualquer base" para decimal
	result = 0
	num = lehexa(n)
	num.reverse()
	for i in range(0,len(num)):
		result += num[i]*b**i
	
	return result
	
def decbase(n,b):
	#Converte Na Base10 para "qualquer base"
	bit = []
	resultado = []

	while (1):
		result = n%b
		n = n//b
		bit.append(result)
		result = n
	
		if n == 0 or n == 1:
			if n == 1:
				bit.append(n)
			bit.reverse()
			break
			
	for i in bit:
		resultado.append(dichexa[i])
	
	return resultado

def hexabase(n,b):
	#Converte hexa para "qualquer base"
	if b == 10:
		return basedec(n,16)
	elif b == 2:
		num = lehexa(n)
		resultado = []
		for i in num:
			resultado.append(intlista(decbase(i,2)))
		return intlista(resultado)
	elif b == 8:
		hexa = basedec(n,16)
		resultado = decbase(hexa,8)
		return intlista(resultado)
		
def octabase(n,b):
	if b == 10:
		return basedec(n,8)
	elif b == 2:
		num = (basedec(n,8))
		resultado = decbase(num,2)
		return intlista(resultado)
	elif b == 16:
		num = (basedec(n,8))
		resultado = decbase(num,16)
		return hexalista(resultado)
		
def binbase(n,b):
	if b == 10:
		return basedec(n,2)
	elif b == 8:
		num = (basedec(n,2))
		resultado = decbase(num,8)
		return intlista(resultado)
	elif b == 16:
		num = (basedec(n,2))
		resultado = decbase(num,16)
		return hexalista(resultado)

