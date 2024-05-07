from poke import pokemon
from sprite import sprite
import time
from generate_pokemon import generate
from generate_pokemon import random_generate

def pelea(select):
    for a in range(10):
        print()
    seleccion = False
    while(not seleccion):
        num = generate()
        print(f'Un {pokemon[num].nombre} salvaje ah aparecido!!')
        print()
        sprite(num)
        print()
        option = input("Atacar o huir? : ")
        if option.lower() == "huir":
            num2 = random_generate()
            if pokemon[select].stats.velocidad > pokemon[num].stats.velocidad:
                if num2 > 0.3:
                    print("Lograste escapar!!")
                else:
                    print("No pudiste escapar, toca peleear!!")
                    seleccion = True
            else:
                if num2 > 0.3:
                    print("Lograste escapar!!")
                else:
                    print("No pudiste escapar, toca peleear!!")
                    seleccion = True
        else:
            seleccion = True
    print()
    print("Que comienza el combate!!")
    print()
    return num

