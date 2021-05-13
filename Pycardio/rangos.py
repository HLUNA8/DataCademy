def verificar(lim_inferior, lim_superior, numero):
	resultado = 0
	if numero >= lim_inferior and numero <= lim_superior:
		resultado = 1
	return resultado

def run():
	print("Hey, ingresa tres valores, un limite inferior, un limite superior y un valor intermedio")
	
	lim_inferior = int(input("limite inferior: "))
	lim_superior = int(input("limite superior: "))
	
	resultado = 0	

	numero = int(input("numero: "))

	resultado  = verificar(lim_inferior, lim_superior, numero)

	if resultado == 1:
		print(f"el numero {numero} esta dentro del limete entre {lim_inferior} y {lim_superior} ")

	else :
		while resultado == 0 :
			print(f"el numero {numero} no se encuentra entre los limites {lim_inferior} y {lim_superior}")
			numero = int (input("ingresa otro numero :"))
			resultado = verificar(lim_inferior, lim_superior, numero)
		print(f"el numero {numero} es correcto esta entre los limites {lim_inferior} y {lim_superior}")

if __name__ == "__main__":
	run()
