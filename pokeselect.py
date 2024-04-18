import random
from poke import pokemon
from sprite import sprite
import time


def pokeselect():
    print('Selecciona a tu Pokemon!')
    for num in range(len(pokemon)):
        time.sleep(1)
        print('------------------------------')
        print(pokemon[num]["nombre"].upper())
        time.sleep(0.5)
        sprite(num)
        if len(pokemon[num]["tipo"]) == 2:
            print(f'Tipo: {pokemon[num]["tipo"][0]} y {pokemon[num]["tipo"][1]}')
        else:
            print(f'TIPO: {pokemon[num]["tipo"][0]}')
        print("MOVIMIENTOS:")
        for move in pokemon[num]["ataques"]:
                print(f'{move},')
        time.sleep(1)
        for stats in pokemon[num]["estadisticas"]:
            print(stats, ':', pokemon[num]["estadisticas"][stats])
