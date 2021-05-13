import math 

def Clase_triangulo(Base, Lado1, Lado2):
	Tipo_Triangulo = ''
	
	if Base == Lado1 and Base == Lado2 :
		Tipo_Triangulo = 'Equilatero y todos los lados del triangulo son iguales'
	elif Base != Lado1 and Base != Lado2 and Lado1 != Lado2 :
		Tipo_Triangulo = 'Escaleno y todos los lados del triangulo son distintos'
	else :
		Tipo_Triangulo = 'Isoceles y dos de los lados de tu triangulo son iguales'

	return Tipo_Triangulo

def Area(Base,Altura):
	return (Base*Altura)/2

def run():
	print("Hola, quieres calcular el area de tu triangulo? ingresa su base y su altura")

	Base = float(input("base: "))
	Altura = float(input("Altura: "))

	Area_triangulo = Area(Base,Altura)

	print (f'El area de tu triangulo es {Area_triangulo} unidades cuadradas')

	print ("Quires saber de que tipo es tu triangulo? Ingresa los dos lados restantes de tu triangulo!")

	Lado1 = float(input("Ingresa uno de los lados faltantes: "))
	Lado2 = float(input("Ingresa el otro lado faltante: "))

	Tipo_triangulo = Clase_triangulo(Base, Lado1, Lado2)

	print(f'Tu triangulo es un {Tipo_triangulo}  :)')
if __name__ == "__main__" :
	run()
