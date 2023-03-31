num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
operador = input("Ingrese un operador de la lista: \n+ (suma) \n- (resta) \nx (multiplicacion) \n/ (division) \n** (potenciacion) \n")

if operador == "+":
	suma = num1+num2
	print(f"la suma es: {suma}")
elif operador == "-":
	resta = num1-num2
	print(f"la resta es: {resta}")
elif operador == "x":
	multi = num1*num2
	print(f"la multiplicacion es {multi}")
elif operador == "/":
	if num2 == 0:
		print("no es posible dividir por cero")
	else:
		div = num1/num2
		print(f"la division es {div}")
elif operador == "**":
	if num1==0 and num2==0:
		print("no se puede elevear cero a la cero")
	else:
		pote = num1**num2
		print(f"la potencia es: {pote}")
else:
	print("operador desconocido")
