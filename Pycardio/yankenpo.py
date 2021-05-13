import time
import random

def ganador(jugador_eleccion, compu_eleccion):
	if jugador_eleccion 

def elegir():
	
	posibilidades = ['piedra', 'papel', 'tijera']
	eleccion = random.choice(posibilidades)
	return eleccion

def run():

	print("Hola!, jueguemos piedra, papel o tijeras")

	
	jugadas_ganadas = 0

	for _ in range (3):
		print("elige uno:")
        	print("         1. piedra")
        	print("         2. papel")
       		print("         3. tijera")
		
		jugador_eleccion = int(input())

		compu_eleccion = elegir()
		gandor_jugador = ganador(jugador_eleccion, compu_eleccion)
		if ganador_jugador == true :
			jugadas_ganadas += 1
	

if __name__ == "__main__":
	run()
