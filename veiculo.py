#veiculo.py
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    def descrever(self):
        return f'{self.__marca} {self.__modelo} {self.__ano}'

    def __str__(self):
        return self.descrever()

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.__num_portas = num_portas

    @property
    def num_portas(self):
        return self.__num_portas
    
    def descrever(self):
        base = super().descrever()
        return f'{base} | {self.__num_portas} | portas'
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.__cilindradas = cilindradas

    @property
    def cilindradas(self):
        return self.__cilindradas
    
    def descrever(self):
        base = super().descrever()
        return f'{base} | {self.__cilindradas} cc'
    
c = Carro('Toyota', 'Corolla', 2023, 4)
m = Moto('Ronda', 'CG 160', 2022, 160)

print(c)
print(m)
print(c.marca)
print(isinstance(c, Veiculo))
print(isinstance(m, Carro))