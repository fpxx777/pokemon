import random
from poke import pokemon
from sprite import sprite

def pokeselect():
    print('Selecciona a tu Pokemon!')
    for num in range(len(pokemon)):
        print('------------------------------')
        print(pokemon[num]["nombre"].upper())
        sprite(num)
        if len(pokemon[num]["tipo"]) == 2:
            print(f'Tipo: {pokemon[num]["tipo"][0]} y {pokemon[num]["tipo"][1]}')
        else:
            print(f'Tipo: {pokemon[num]["tipo"][0]}')
        print("Movimientos:")
        for move in pokemon[num]["ataques"]:
                print(f'{move},')
pokeselect()