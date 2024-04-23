import random
from random import randint

def ataque(atacante,atak, oponent):
    bonus = 0
    variabilidad = random.randint(85, 100)
    if atak.clase == "Ataque Especial":
        ataque = atacante.stats.ataqueEspecial
        defensa = oponent.stats.defensaEspecial
    elif atak.clase == "Ataque":
        ataque = atacante.stats.ataque
        defensa = oponent.stats.defensa
    potencia = atak.potencia
    total = bonus * variabilidad * (ataque * potencia / (25 * defensa))
    print(total)+