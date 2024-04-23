class Stats:
    def __init__(self, stats):
        self.hp = stats[0]
        self.ataque = stats[1]
        self.defensa = stats[2]
        self.ataqueEspecial = stats[3]
        self.defensaEspecial = stats[4]
        self.velocidad = stats[5]

    def __str__(self) -> str:
        return f"HP: {self.hp}\nAtque: {self.ataque}\nDefensa: {self.defensa}\nAtaque Especial: {self.ataqueEspecial}\nDefensa Especial: {self.defensaEspecial}\nVelocidad: {self.velocidad}"


class Ataques:
        def __init__(self, nombre, posicion):
                self.nombre = nombre
                self.posicion_json = posicion
        def __repr__(self):
                return f"Nombre: {str(self.nombre)}, Posicion en JSON: {str(self.posicion_json)}"

class Pokemon:
    def __init__(self, nombre, tipo, ataques, estadisticas):
        self.nombre = nombre
        self.tipo = tipo
        self.ataques = ataques
        self.stats = Stats(estadisticas)


venasaur = Pokemon(
    "Venasaur",
    ["Planta", "Veneno"],
    [
        Ataques("Rayo Solar", 0),
        Ataques("Somnifero", 1),
        Ataques("Sintesis", 2),
        Ataques("Latigazo", 3),
    ],
    [80, 82, 83, 100, 100, 80],
)

charizard = Pokemon(
    "Charizard",
    ["Fuego", "Volador"],
    [
        Ataques("Lanzallamas", 4),
        Ataques("Infierno", 5),
        Ataques("Garra Dragon", 6),
        Ataques("Envite Igneo", 7),
    ],
    [78, 84, 78, 100, 109, 85],
)

blastoise = Pokemon(
    "Blastoise",
    ["Agua"],
    [
        Ataques("Hidrobomba", 8),
        Ataques("Defensa Ferrea", 9),
        Ataques("Danza Lluvia", 10),
        Ataques("Envite Acuatico", 11),
    ],
    [79, 83, 100, 78, 85, 78],
)
pokemon = [venasaur, charizard, blastoise]

