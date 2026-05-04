#veiculo.py
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    def descrever(self):
        return f'+{self.marca} {self.modelo} {self.ano}'

    def __str__(self):
        return self.descrever()

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

    def descrever(self):
        return f'{super().descrever()} com {self.portas} portas'