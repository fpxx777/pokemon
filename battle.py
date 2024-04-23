import random
from poke import pokemon
from sprite import sprite
import time
from generate_pokemon import generate

def pelea(select):
    for a in range(10):
        print()
    num = generate()
    print(f'Un {pokemon[num].nombre} salvaje ah aparecido!!')
    print()
    sprite(num)
    print()
    elec = input("Atacar o huir? : ")
    if elec.lower() == "huir":
        num2 = random.random()
        if num2 > 0.5:
            print("Lograste escapar!!")
            return
        else:
            print("No pudiste escapar, toca peleear!!")
    print()
    print("Que comienza el combate!!")
    print()
    print()
    print("MOVIMIENTOS:")
    for move in pokemon[select].ataques:
            print(f'{move.posicion_json}. {move.nombre},')
    print()
    move_select = input('Que ataque quieres usar?: ')
pelea(2)