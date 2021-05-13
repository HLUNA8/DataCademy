def millas_kilometros (millas):
	return round ((millas * 1609344),2)

def kilometros_millas (kilometros):
	return round((kilometros/1609344),2)

def run():
	print("Hola!, que deseas hacer?")
	print ("1. millas -> kilometros")
	print ("2. kilometros -> millas")

	eleccion = int(input())

	if eleccion == 1 :
		millas = int(input("cunatas millas deseas compartir: "))
		resultado = millas_kilometros(millas)
		print (f"{millas} millas son {resultado} kilometros")
	elif eleccion == 2 :
		kilometros = int(input("cuantos kilometros deseas convertir: "))
		resultado = kilometros_millas(kilometros)
		print (f"{kilometros} kilometros son {resultado} millas")

if __name__ == "__main__":
	run()
