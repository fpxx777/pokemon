import random
from random import randint

#Realiza el calculo para quitar vida al oponente

def ataque(pokemon,atak, oponent, ):
    bonus = 1
    variabilidad = random.randint(85, 100)
    potencia = atak.potencia
    efectividad = 0.5
    nivel = 100
    if atak.clase == "Ataque Especial":
        ataque = pokemon.stats.ataqueEspecial
        defensa = oponent.stats.defensaEspecial
    else:
        ataque = pokemon.stats.ataque
        defensa = oponent.stats.defensa
    total = (0.01 * bonus) * efectividad * variabilidad * (((((0.2 * nivel) + 1) * ataque * potencia) / (25 * defensa)) + 2)
    print(round(total))