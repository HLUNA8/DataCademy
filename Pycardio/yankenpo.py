import random

def descifrar(numero_descifrar):
	descifrar = ''
	if numero_descifrar == 1 :
		descifrar = 'piedra'
	elif numero_descifrar == 2 :
		descifrar = 'papel'
	else :
		descifrar = 'tijeras'

	return descifrar

def ganador_partida(jugador1, jugador2):
	ganador = 0
	if jugador1 == jugador2 :
		ganador = 3

	elif (jugador1 == 1 and jugador2 == 3) or (jugador1 == 2 and jugador2 == 1) or (jugador1 == 3 and jugador2 == 2):
		ganador = 1

 
	else :
		ganador = 2

	return ganador

def eleccion(jugador):
	print(f"{jugador} es tu turno elige:")
	print("		1. piedra")
	print("		2. papel")
	print("		3. tijeras")

	eleccion = int (input())

	return eleccion

def run():
	print("Hola!, juguemos unas partidas de piedra papel ")
	print("		1. jugar con la computadora")
	print("		2. jugar con un amigo")

	modo_juego = int(input())
	numero_partidas = int(input("cuantas partidas deseas jugar :"))

	if modo_juego == 1:
		num_juegos = 0
		juegos_ganados = 0
		juegos_perdidos = 0

		while num_juegos < numero_partidas:
			jugador = eleccion(jugador = 'jugador')
			compu = random.randint(1,3)
			ganador = ganador_partida(jugador, compu)
			eleccion_jugador = descifrar(jugador)
			eleccion_compu = descifrar(compu)


			if ganador == 1:
				juegos_ganados += 1
				num_juegos += 1 
				print (f"{eleccion_jugador} vs {eleccion_compu} tu ganas!")

			elif ganador == 2:
				juegos_perdidos += 1
				num_juegos +=1
				print(f"{eleccion_jugador} vs {eleccion_compu} perdiste :(")

			else :
				print(f"{eleccion_jugador} vs {eleccion_compu} es un empate!!")

		if juegos_ganados > juegos_perdidos :
			print("Ganaste!!")

		elif juegos_ganados == juegos_perdidos :
			print("Oooo !! Empatamos, fue una buena ronda de juegos  :)")

		else:
			print(f"Perdiste {juegos_perdidos} a {juegos_ganados} :(  suerte la proxima!!")



	if modo_juego == 2 :
                num_juegos = 0
                juegos_ganados = 0
                juegos_perdidos = 0

                while num_juegos < numero_partidas:

                        jugador1 = eleccion(jugador = 'jugador1')
                        jugador2 = eleccion(jugador = 'jugador2')
                        ganador = ganador_partida(jugador1, jugador2)
                        eleccion_jugador1 = descifrar(jugador1)
                        eleccion_jugador2 = descifrar(jugador2)


                        if ganador == 1:
                                juegos_ganados += 1
                                num_juegos += 1
                                print (f"{eleccion_jugador1} vs {eleccion_jugador2}, jugador1 tu ganaste!!")

                        elif ganador == 2:
                                juegos_perdidos += 1
                                num_juegos +=1
                                print(f"{eleccion_jugador1} vs {eleccion_jugador2}, jugador2 tu ganaste")

                        else :
                                print(f"{eleccion_jugador} vs {eleccion_compu} es un empate!!")

                if juegos_ganados > juegos_perdidos :
                        print("Ganaste jugador1!!")

                elif juegos_ganados == juegos_perdidos :
                        print("Oooo !! Empataron {juegos_ganados} a {juegos_perdidos}, fue una buena ronda de juegos  :)")

                else:
                        print(f"Ganaste jugador2!!")
		


if __name__ == "__main__":
	run()
