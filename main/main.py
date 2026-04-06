# DESENVOLVEDOR: Matheus Cabral
# PROJETO: Sistema de Passagens de Ônibus - Carr

# DESCRIÇÃO: Este prjeto foi a ideia de melhoria de outro projeto que fiz do qual está 
# nominado nos arquivos como "passagem.py" e "passagem2.py"onde eu apliquei os 
# conhecimentos que adquiri com o livro "Lógica de programação: A construção 
# de algoritmos e estruturas de dados com aplicações em Python", do autor André Luiz Villar Forbellone,
# comecei a também a estudar POO com Java, criando familiaridade com os conceitos de classes,
# objetos, herança e encapsulamento. 

# Este projeto foi feito com o intuito de aplicar os 
# conhecimentos adquiridos, além de ser um projeto 
# prático e divertido para consolidar o aprendizado.

from onibus import Onibus
from cidade import Cidade 
from distancia import Distancia
import calculo


def menu():

    while True:
        print("\n=========================================================")
        print("    BEM-VINDO AO CARR - SISTEMA DE PASSAGENS DE ÔNIBUS")
        print("=========================================================\n")
        print("-----------------------------------------------------------")
        print("Selecione uma opção:\n")
        print("0 - Sair do sistema")
        print("1 - Informações do ônibus")
        print("2 - Cidades disponíveis")
        print("3 - Distâncias entre as cidades")
        print("4 - Comprar passagem")
        print("-----------------------------------------------------------\n")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '0':
            if input("\nTem certeza que deseja sair? (S/N): ").upper() == 'S':
                print("\nSaindo do sistema. Obrigado por usar o Carr!")
                break
            else:
                print("\nOperação cancelada. Retornando ao menu.")
                continue
            
        elif escolha == '1':
            onibus_info = Onibus()
            print("\nInformações do ônibus:\n")
            onibus_info.mostrar_informacoes()
            pass

        elif escolha == '2':
            cidades_disponiveis = Cidade()
            print("\nCidades disponíveis:\n")
            cidades_disponiveis.mostrar_cidades()
            pass

        elif escolha == '3':
            distancia_info = Distancia()
            distancia_info.mostrar_distancias()
            pass

        elif escolha == '4':
            calculo.processar_compra()
            break

menu()