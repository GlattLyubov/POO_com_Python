# Declarando uma dataclasse para o exemplo
from dataclasses import dataclass
from random import randint
from datetime import datetime  



@dataclass
class Onibus:
    NomeEmpresa: str
    Modelo: str
    Acento: list[int]
    Placa: str
    Motorista: str

Companhia = Onibus(
    NomeEmpresa= "Comandos Carr",
    Modelo = "Merdedes-Benz O-500RS",
    Acento = [i for i in range(1, 45)],
    Placa = "ABC-1234",
    Motorista = "Wagner Swartz"
)

@dataclass
class Distancia:
    MatDistancia: list[int]

Matriz = Distancia(
    MatDistancia = [[0, 524, 521, 882],
                    [524, 0, 434, 586],
                    [521, 434, 0, 429],
                    [882, 586, 429, 0]]
)

@dataclass
class Cidade:
    Nome: list[str]
    origem: int
    destino: int

cidades = ["Vitória", "Belo Horizonte", "Rio de Janeiro", "São Paulo"]

while True:
    
    print('''\nBem-vindo ao sistema de passagens de ônibus da Comandos Carr! Escolha a cidade de origem e destino para calcular a distância entre elas:
          
    0 - Vitória
    1 - Belo Horizonte
    2 - Rio de Janeiro
    3 - São Paulo\n''')

    origem = int(input("Digite o número da cidade de origem: "))
    destino = int(input("Digite o número da cidade de destino: "))

    VetorCidade = Cidade(
        Nome = cidades,
        origem = origem,
        destino = destino
    )

    print(f"\nDistância entre {VetorCidade.Nome[VetorCidade.origem]} e {VetorCidade.Nome[VetorCidade.destino]}: {Matriz.MatDistancia[VetorCidade.origem][VetorCidade.destino]} km\n")
    break

@dataclass
class RedEmbarque:
    NumPassagem: int
    NumPoltrona: int
    Idade: int
    Nome: str
    Data: str
    Origem: str
    Destino: str
    Horario: str

# Criando uma instância da dataclasse
passagem = RedEmbarque(
    NumPassagem = randint(0, 99999),
    NumPoltrona = Companhia.Acento[randint(0, len(Companhia.Acento)-1)],
    Nome = input("Digite o nome do passageiro: "),
    Idade = int(input("Digite a idade do passageiro: ")),
    Data = datetime.now().strftime("%d/%m/%Y"),
    Origem = VetorCidade.Nome[VetorCidade.origem],
    Destino = VetorCidade.Nome[VetorCidade.destino],
    Horario = datetime.now().strftime("%H:%M")
)

# Imprimindo os detalhes da passagem
print(f'''
        Detalhes da Passagem:

Motorista: {Companhia.Motorista} Ônibus: {Companhia.NomeEmpresa} 
Modelo: {Companhia.Modelo} Placa: {Companhia.Placa}        
Número da Passagem: {passagem.NumPassagem}  Data: {passagem.Data}
De: {passagem.Origem} Para: {passagem.Destino}
Horário: {passagem.Horario}  Poltrona: {passagem.NumPoltrona}  Idade: {passagem.Idade}
Passageiro: {passagem.Nome}
''')