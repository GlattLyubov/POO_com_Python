import cidade

class Distancia:
    def __init__(self):
        self.MatDistancia = [[0, 524, 521, 882],
                            [524, 0, 434, 586],
                            [521, 434, 0, 429],
                            [882, 586, 429, 0]]

    def mostrar_distancias(self):
        VetorCidade = cidade.Cidade()
        print("\nCidades disponíveis:\n")
        VetorCidade.mostrar_cidades()

        origem = int(input("\nDigite o número da cidade de origem: "))
        destino = int(input("Digite o número da cidade de destino: "))

        print(f"\nDistância entre {VetorCidade.cidades[origem]} e {VetorCidade.cidades[destino]}: {self.MatDistancia[origem][destino]} km")