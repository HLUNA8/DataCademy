import numpy as np

def volumen_cilindro(radio, altura):
	return (np.pi * (radio**2) * altura)

def volumen_cubo(base):
	return base**3

def volumen_paralelogramo(altura, base, profundidad):
	return altura * base * profundidad

def volumen_esfera(radio):
	return (3/4) * np.pi * (radio**3)

def run():
	print("Hey ! que volumen deseas encontrar:")
	print("		1. Cilindro")
	print("		2. Cubo")
	print("		3. Paralelogramo")
	print("		4. esfera")
	
	figura = int (input())

	if figura == 1:
		print("ingresa el radio y la latura")
		radio = float(input("radio: "))
		altura = float(input("altura: "))
		vol = volumen_cilindro(radio,altura)
		print(f"el volumen de tu cilindro es {vol}")

	elif figura == 2:
		print("ingresa la base del cubo")
		base = float(input("base: "))
		vol = volumen_cubo(base)
		print(f"el volumen de tu cubo es {vol}")

	elif figura == 3:
		print("ingresa la altura, base, profundidad de tu paralelogramo")
		altura = float(input("altura: "))
		base = float(input("base: "))
		profundidad = float(input("profundidad: "))
		vol = volumen_paralelogramo(altura, base, profundidad)
		print(f"el volumen de tu paralelogramo es {vol}")

	elif figura == 4:
		print("ingresa el radio de tu esfera")
		radio = float(input("radio: "))
		vol = volumen_esfera(radio)
		print(f"el volumen de tu esfera es {vol}")

if __name__ == "__main__":
	run()
