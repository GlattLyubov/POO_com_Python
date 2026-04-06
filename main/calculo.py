from distancia import Distancia 
from usuario import Usuario
from cidade import Cidade
from onibus import Onibus
from passagem import Passagem

def calcular_valor_passagem(origem, destino):
    distancias = Distancia()
    distancia_km = distancias.MatDistancia[origem][destino]
    valor_passagem = distancia_km * 0.5
    return valor_passagem

def processar_compra():
    print("\n=== Comprar Passagem ===\n")
    nome = input("Digite somente o primeiro nome: ")
    idade = input("Digite sua idade: ")
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu email: ")

    user = Usuario(nome=nome, idade=idade, cpf=cpf, email=email)
    
    print("\nInformações do usuário:\n")
    user.mostrar_informacoes()

    confirmar = input("\nDeseja comprar uma passagem? (S/N): ").upper()
    if confirmar == 'S':
        cidades_obj = Cidade()
        print("\nCidades disponíveis:\n")
        cidades_obj.mostrar_cidades()
        
        origem = int(input("\nDigite o número da cidade de origem: "))
        destino = int(input("Digite o número da cidade de destino: "))
        
        valor = calcular_valor_passagem(origem, destino)
        
        nome_origem = cidades_obj.cidades[origem]
        nome_destino = cidades_obj.cidades[destino]
        onibus_info = Onibus()

        bilhete = Passagem(user, onibus_info, nome_origem, nome_destino, valor)
        bilhete.gerar_bilhete()
        
        return True
    
    print("\nCompra cancelada.")
    return False

def consultar_valor():
    distancia_info = Distancia()
    distancia_info.mostrar_distancias()
    
    cidades_obj = Cidade()
    cidades_obj.mostrar_cidades()
    
    try:
        origem = int(input("\nDigite o número da cidade de origem para consulta: "))
        destino = int(input("Digite o número da cidade de destino para consulta: "))
        
        valor = calcular_valor_passagem(origem, destino)
        
        print(f"\nDistância entre {cidades_obj.cidades[origem]} e {cidades_obj.cidades[destino]}")
        print(f"Valor estimado da passagem: R${valor:.2f}")
        
    except (ValueError, IndexError):
        print("\nErro: Seleção de cidades inválida.")


