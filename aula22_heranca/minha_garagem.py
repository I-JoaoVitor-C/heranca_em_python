from veiculo import Veiculo, Carro, Moto

v1 = Carro('Volkswagen', 'Fusca', 1978, 2)
v2 = Carro('Audi', 'R8', 2024, 2)
v3 = Moto('Porsche', 'Harley-Davidson V-Rod', 2017, 1250)

garagem = [v1, v2, v3]

for v in garagem:
    print (v)

carros = [v for v in garagem if isinstance(v, Carro)]
motos = [v for v in garagem if isinstance(v, Moto)]
print(f'Carros: {len(carros)} | Motos: {len(motos)}')