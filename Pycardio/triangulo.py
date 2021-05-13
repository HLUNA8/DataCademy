import math 

def Area(Base,Altura):
	return (Base*Altura)/2

def run():
	print("Hola, quieres calcular el area de tu triangulo? ingresa su base y su altura")

	Base = float(input("base: "))
	Altura = float(input("Altura: "))

	Area_triangulo = Area(Base,Altura)

	print (f'El area de tu triangulo es {Area_triangulo} unidades cuadradas')

if __name__ == "__main__" :
	run()
