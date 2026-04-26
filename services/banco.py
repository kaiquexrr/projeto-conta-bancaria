from models.conta import ContaBancaria
class Banco:
    def __init__(self):
        self.__contas = []

    def criar_contas(self,titular,numero):
        conta = ContaBancaria(titular,numero)
        self.__contas.append(conta)
        
       
    def buscar_contas(self,numero):
        for conta in self.__contas:
            if conta.numero == numero:
                return conta    
        return None



    def listar_contas(self):
        return self.__contas
