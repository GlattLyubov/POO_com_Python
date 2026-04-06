
class Usuario:
    def __init__(self, nome=None, idade=None, cpf=None, email=None):
        self.Nome = nome
        self.Idade = idade
        self.CPF = cpf
        self.Email = email

    def mostrar_informacoes(self):
        print(f"Nome: {self.Nome}")
        print(f"Idade: {self.Idade}")
        print(f"CPF: {self.CPF}")
        print(f"Email: {self.Email}")