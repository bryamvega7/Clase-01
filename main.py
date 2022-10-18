#Realizar Calculadora Basica

#Bryam Antony Vega Chafloque
#Alvaro Jose Chancafe Araujo
#Andre Sebastian Arquinigo
#Antonio Manuel Barrantes Rupaylla
#Cristian Diaz

def suma(num1,num2):
  resultado = num1+num2
  return resultado

def resta(num1,num2):
  resultado = num1-num2
  return resultado

def multiplicacion(num1,num2):
  resultado = num1*num2
  return resultado

def division(num1,num2):
  resultado = num1/num2
  return resultado

def potencia(num1,num2):
  resultado = num1*num2
  return resultado

print("\nBienvenido a la Calculadora Basica!")

print("\nTener en cuenta los signos de cada operacion:\n1. Suma [+]\n2. Resta [-]\n3. Multiplicacion [*]\n4. Division [/]\n5. Potencia [**]")

num1 = int(input("Ingrese el Primer numero: "))
num2 = int(input("Ingrese el Segundo numero: "))
op = input("Ingrese el signo de la operacion desea realizar: ")

if op == "+":
  print(suma(num1,num2))
elif op == "-":
  print(resta(num1,num2))
elif op == "*":
  print(multiplicacion(num1,num2))
elif op == "/":
  print(division(num1,num2))
elif op == "**":
  print(potencia(num1,num2))
else:
  print("El operador no es valido")