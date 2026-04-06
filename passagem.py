
# Declarando uma dataclasse para o exemplo
from dataclasses import dataclass

@dataclass
class RedEmbarque:
    NumPassage: int
    NumPoltrona: int
    Idade: int
    Nome: str
    Data: str
    Origem: str
    Destino: str
    Horario: str

# Criando uma instância da dataclasse

passagem = RedEmbarque(
    NumPassage= 12345,
    NumPoltrona= 12,
    Idade= 22,
    Nome= "Matheus Cabral Brandão Liebana",
    Data= "2024-06-15",
    Origem= "São Paulo",
    Destino= "Gramado",
    Horario= "14:30"
)

# Imprimindo os detalhes da passagem

print(f'''
        Detalhes da Passagem:
      
Número da Passagem: {passagem.NumPassage}  Data: {passagem.Data}
De: {passagem.Origem} Para: {passagem.Destino}
Horário: {passagem.Horario}  Poltrona: {passagem.NumPoltrona}  Idade: {passagem.Idade}
Passageiro: {passagem.Nome}
''')