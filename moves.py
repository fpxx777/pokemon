import json

class Movimiento:
    def __init__(self, nombre, tipo, clase, potencia, precision, prioridad, pp, efecto):
        self.nombre = nombre
        self.tipo = tipo
        self.clase = clase
        self.potencia = potencia
        self.precision = precision
        self.prioridad = prioridad
        self.pp = pp
        self.efecto = efecto

def jsoncreate():
    with open("JSON/moves.json", "r") as file:
        data = json.load(file)
        return data

data = jsoncreate()

movimientos = [Movimiento(**movimiento) for movimiento in data]



