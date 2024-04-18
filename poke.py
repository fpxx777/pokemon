class Pokemon:
    def __init__(self, nombre, tipo, ataques, estadisticas):
        self.nombre = nombre
        self.tipo = tipo
        self.ataques = ataques
        self.estadisticas = estadisticas

venasaur = Pokemon("Venasaur",
                ["Planta",
                "Veneno"],
                ["Rayo Solar",
                "Somnifero",
                "Sintesis",
                "Latigazo"],{
            "HP": 80,
            "Ataque": 82,
            "Defensa": 83,
            "Velocidad": 80,
            "Ataque Especial": 100,
            "Defensa Especial": 100
        })

print(venasaur)