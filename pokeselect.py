import random
from poke import pokemon
from sprite import sprite
import time


def pokeselect():
    print('Selecciona a tu Pokemon!')
    for num in range(len(pokemon)):
        time.sleep(1)
        print('------------------------------')
        print(pokemon[num].nombre.upper())
        time.sleep(0.5)
        sprite(num)
        if len(pokemon[num].tipo) == 2:
            print(f'Tipo: {pokemon[num].tipo[0]} y {pokemon[num].tipo[1]}')
        else:
            print(f'TIPO: {pokemon[num].tipo[0]}')
        print("MOVIMIENTOS:")
        for move in pokemon[num].ataques:
                time.sleep(0.6)
                print(f' {move.nombre},')
        time.sleep(1)
        print(f'{pokemon[num].stats}')
    select = input("Y tu eleccion es?:")
    if select.lower() == "venasaur":
        select = 0
    elif select.lower() == "charizard":
        select = 1
    elif select.lower() == "blastoise":
        select = 2
    else:
        print('Ese Pokemon aun no esta en el juego D:')
        return
    print(f"Has seleccionado a {pokemon[select].nombre}!!")
    return select


