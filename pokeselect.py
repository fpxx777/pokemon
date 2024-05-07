import random
from poke import pokemon
from sprite import sprite
import time

#Realiza la seleccion de los pokemon

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
    seleccion = False
    while (not seleccion):
        select = input("Y tu eleccion es?:")
        if select.lower() == "venasaur" or select == "1":
            select = 0
            seleccion = True
        elif select.lower() == "charizard" or select == "2":
            select = 1
            seleccion = True
        elif select.lower() == "blastoise" or select == "3":
            select = 2
            seleccion = True
        else:
            print('Ese Pokemon aun no esta en el juego D:')
    print(f"Has seleccionado a {pokemon[select].nombre}!!")
    return select

if __name__ == "__main__":
    pokeselect()

