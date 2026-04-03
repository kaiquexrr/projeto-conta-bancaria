from rich import print
class Contabancaria:
    def __init__(self,titular,numero,saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        print(f'conta {self.numero} criada com sucesso. saldo atual de [green]R${self.saldo:,.2f}[/]')

    def menu(self):
        while True:
            print('[1] depositar')
            print('[2] sacar')
            print('[3] ver saldo')
            print('[4] sair ')

            try:
                resposta = int(input())
            except ValueError:
                print('voce digitou texto ao inves de numero')
                continue

            if resposta == 1:
                try:
                    depositar = int(input('informe o valor do deposito: '))
                except ValueError:
                    print('voce digitou texto ao inves de numero')
                    continue
                if depositar <= 0:
                    print(f'valor [red]negativo[/] nao pode ser depositado')
                else:
                    self.depositar(depositar)

            elif resposta == 2:
                try:
                    saque = int(input('saque: '))
                except ValueError:
                    print('voce digitou texto ao inves de numero')
                    continue
                if saque <= 0:
                    print(f'valor [red]negativo[/] nao pode ser sacado')
                else:
                    self.sacar(saque)
            elif resposta == 3:
                    print(f'saldo: R${self.saldo:,.2f}')
            elif resposta == 4:
                break
            else:
                print('opcão invalida')
                continue


    def __str__(self):
        return f'conta {self.numero} de {self.titular} tem  R${self.saldo:,.2f} de saldo'

    def  depositar(self,valor):
        self.saldo += valor
        print(f'deposito de [green]R${valor:,.2f} Autorizado na conta {self.numero}[/]')

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'saca [green]R${valor:,.2f} de saldo')
        else:
            print(f'Saque negado de [red]R${self.saldo:,.2f} na conta {self.numero}. SALDO INSUFICIENTE[/]')




c1 = Contabancaria('kaique',3252,)
c1.menu()

