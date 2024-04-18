import json

def pokecarga() :
    with open("json/pokemon.json", "r") as file:
        pokemon = json.load(file)
        return pokemon
pokemon = pokecarga()