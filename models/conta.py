from rich import print

class ContaBancaria():
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.__saldo = saldo
        print(f'conta {self.numero} criada com sucesso. saldo atual de [green]R${self.__saldo:,.2f}[/]')

    @property
    def saldo(self):
        return self.__saldo

    def __str__(self):
        return f'conta {self.numero} de {self.titular} tem  R${self.__saldo:,.2f} de saldo'

    def depositar(self, valor):
        self.__saldo += valor
        print(f'deposito de [green]R${valor:,.2f} Autorizado na conta {self.numero}[/]')

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de [green]R${valor:,.2f}[/] realizado com sucesso')
        else:
            print(f'Saque negado de [red]R${valor:,.2f} na conta {self.numero}. SALDO INSUFICIENTE[/]')

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
                    depositar = float(input('informe o valor do deposito: '))
                except ValueError:
                    print('voce digitou texto ao inves de numero')
                    continue
                if depositar <= 0:
                    print(f'valor [red]invalido[/] nao pode ser depositado')
                else:
                    self.depositar(depositar)
            elif resposta == 2:
                try:
                    saque = float(input('saque: '))
                except ValueError:
                    print('voce digitou texto ao inves de numero')
                    continue
                if saque <= 0:
                    print(f'valor [red]invalido[/] nao pode ser sacado')
                else:
                    self.sacar(saque)
            elif resposta == 3:
                print(f'saldo: R${self.saldo:.2f}')
            elif resposta == 4:
                break
            else:
                print('opção inválida')
                continue


    