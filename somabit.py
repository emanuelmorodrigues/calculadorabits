num1 = []
num2 = []
vai1 = []
resultado = []

bits = int(input("Range\n"))

for i in range(bits):
	valor = int(input("Valor1\n"))
	num1.append(valor)
	
for i in range(bits):
	valor = int(input("Valor2\n"))
	num2.append(valor)

for i in range(bits):
	vai1.append(0)

# ORGANIZA O VAI1
for i in range(-1,(-1)*bits,-1):
	#if num1[i] + num2[i] + vai1[i] == 0:
	#	lista.append(0)	
	if (num1[i] + num2[i] + vai1[i] >= 2):
		vai1[i-1] = 1
	#elif (num1[i] + num2[i] + vai1[i] == 3):
	#	vai1[i-1] = 1

#Soma bit
for i in range(-1,(-1)*bits-1,-1):
	if (num1[i] + num2[i] + vai1[i] == 0) or (num1[i] + num2[i] + vai1[i] == 2):
		resultado.append(0)
	elif (num1[i] + num2[i] + vai1[i] == 1) or (num1[i] + num2[i] + vai1[i] == 3):
		resultado.append(1)
	#elif (num1[i] + num2[i] + vai1[i] == 2):
	#	lista.append(0)
	#elif (num1[i] + num2[i] + vai1[i] == 3):
	#	lista.append(1)
#Adiciona bits quanto o resultado é uma representação maior que o range
	if i == (-1)*bits and vai1[i] + num1[i] + num2[i] >= 2:
		resultado.append(1)
	#elif i == (-1)*bits and vai1[i] + num1[i] + num2[i] == 0:
	#	lista.append(0)

resultado.reverse()

print(vai1, " Vai1 ")
print(num1, " Parcela 1")
print(num2, " Parcela 2\n ")
print("Resultado\n")

for i in resultado:
	print(i, end='')
	
print("\n")
