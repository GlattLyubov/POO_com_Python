
class Onibus:
    def __init__(self, nome_empresa="Comandos Carr", modelo="Mercedes-Benz O-500RS", placa="ABC-1234", motorista="Wagner Swartz"):
        self.NomeEmpresa = nome_empresa
        self.Modelo = modelo
        self.Placa = placa
        self.Motorista = motorista

    def mostrar_informacoes(self):
        print(f"""
        ==================================================
                    INFORMAÇÕES DO VEÍCULO
        ==================================================
        Empresa:   {self.NomeEmpresa}
        Modelo:    {self.Modelo}
        Placa:     {self.Placa}
        Motorista: {self.Motorista}
        ==================================================
        """)

