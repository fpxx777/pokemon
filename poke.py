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


class Pokemon:
    def __init__(self, nombre, tipo, ataques, estadisticas):
        self.nombre = nombre
        self.tipo = tipo
        self.ataques = ataques
        self.stats = Stats(estadisticas)

venasaur = Pokemon("Venasaur",
                ["Planta",
                "Veneno"],
                ["Rayo Solar",
                "Somnifero",
                "Sintesis",
                "Latigazo"],[80, 82, 83, 100, 100, 80
        ])

charizard = Pokemon("Charizard",
                ["Fuego",
                "Volador"],
                ["Lanzallamas",
                "Infierno",
                "Garra Dragon",
                "Envite Igneo"],[78, 84, 78, 100, 109, 85
        ])

blastoise = Pokemon("Blastoise",
                ["Agua"],
                ["Hidrobomba",
                "Defensa Ferrea",
                "Danza Lluvia",
                "Envite Acuatico"],[79, 83, 100, 78, 85, 78
        ])
pokemon = [venasaur, charizard, blastoise]