from html.entities import name2codepoint


class nombredelaclase:
    def nombredelmetodo(self):
        self.nombredelavariable = "Algoritmo"

class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3

s = Matematica()
s.suma()
print(s.n1 + s.n2)

class Ropa:
    def __init__(self):
        self.marca = "willow"
        self.talla = "M"
        self.color = "rojo"

camisa = Ropa()
print(camisa.talla)

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(10, 5)
print(operacion.suma)