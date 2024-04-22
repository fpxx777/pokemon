import random
from random import randint

def ataque(pokemon,atak, oponent, ):
    bonus = 0
    variabilidad = random.randint(85, 100)
    ataque = pokemon.stats.atak["clase"]
    potencia = atak["potencia"]
    defensa = oponent.stats.atak["clase"]
    total = bonus * variabilidad * (ataque * potencia / (25 * defensa))