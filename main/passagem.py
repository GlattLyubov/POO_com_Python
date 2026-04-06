from datetime import datetime

class Passagem:
    def __init__(self, usuario, onibus, origem_nome, destino_nome, valor):
        self.usuario = usuario    
        self.onibus = onibus      
        self.origem = origem_nome
        self.destino = destino_nome
        self.valor = valor
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.num_passagem = "BR-" + datetime.now().strftime("%H%M%S")

    def gerar_bilhete(self):
        print(f'''
        ========================================================
                      DETALHES DA PASSAGEM
        ========================================================
        Motorista: {self.onibus.Motorista}   Empresa: {self.onibus.NomeEmpresa}
        Modelo: {self.onibus.Modelo}      Placa: {self.onibus.Placa}
        --------------------------------------------------------
        Número da Passagem: {self.num_passagem}  Data: {self.data}
        De: {self.origem}  Para: {self.destino}
        --------------------------------------------------------
        Passageiro: {self.usuario.Nome}  CPF: {self.usuario.CPF}
        VALOR PAGO: R$ {self.valor:.2f}
        ========================================================
        ''')
