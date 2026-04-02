from rich import print
class Contabancaria:
    def __init__(self,titular,numero,saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        print(f'conta {self.numero} criada com sucesso. saldo atual de [green]R${self.saldo:,.2f}[/]')

    def __str__(self):
       return f'conta {self.numero} de {self.titular} tem  R${self.saldo:,.2f} de saldo'

    def  depositar(self,valor):
        self.saldo += valor
        print(f'deposito de [green]R${self.saldo:,.2f} Autorizado na conta {self.numero}[/]')

    def sacar(self,valor):
        if valor < self.saldo:
            print(f'Saque negado de [red]R${self.saldo:,.2f} na conta {self.numero}. SALDO INSUFICIENTE[/]')
        else:
            print(f'Saque de [green]R$ {valor:,.2f} autorizado na conta {self.numero}[/] ')
        self.saldo -= valor


c1 = Contabancaria('kaique',3252,650)
c1.depositar(100)
c1.sacar(500)
print(c1)
