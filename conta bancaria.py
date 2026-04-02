class Contabancaria:
    def __init__(self,titular,numero,saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def  depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        self.salod -= valor


c1 = Contabancaria('kaique',3252,650)
