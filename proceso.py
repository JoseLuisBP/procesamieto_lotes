import random

class Proceso:
    def __init__(self, id = 0, nombre = "", operacion = "", resultado = "", tme = 5):
        self.id = id
        self.nombre = nombre
        self.operacion = operacion
        self.resultado = resultado
        self.tme = tme

    def generarOperacion(self):
        operador = random.choice(['+', '-', '*', '/','%','^'])
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        
        self.operacion = f"{num1} {operador} {num2}"

    def generarResultado(self):
        eval(self.operacion)

    def generarNombre(self):
        nombres = [
            "Alba", "Rene", "Andrea", "Nancy", "Midory",
            "Juan", "Alex", "Carlos", "Daniel", "Emilio",
            "Sofia", "Alejandra", "Paola", "Ana", "Irina",
            "Luis", "Noe", "Mateo", "Jose", "Teo"
        ]
        self.nombre = random.choice(nombres)
    
