

class Cidade:
    def __init__ (self, nome=None):
        self.Nome = nome
        self.cidades = ["Vitória", "Belo Horizonte", "Rio de Janeiro", "São Paulo"]

    def mostrar_cidades(self):
        for i, cidade in enumerate(self.cidades):
            print(f"{i} - {cidade}")

