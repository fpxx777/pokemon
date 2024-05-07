from poke import pokemon
from sprite import sprite
import time
from generate_pokemon import random_generate
from battle_start import pelea

def combate(select):
    print("MOVIMIENTOS:")
    for move in pokemon[select].ataques:
        time.sleep(0.6)
        print(f' {move.posicion_json}. {move.nombre}')
    seleccion = False
    while(not seleccion):
        response = input("Que movimiento quieres usar?: ")
        for move in pokemon[select].ataques:
            if response == str(move.posicion_json) or response.lower() == move.nombre.lower():
                seleccion = True
                response = move.posicion_json
                break
        if seleccion == False:
            print("Ese movimiento no existe!")
    print(response)
if __name__ == "__main__":
    combate(2)