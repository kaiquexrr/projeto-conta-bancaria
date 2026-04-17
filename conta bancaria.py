from rich import print
contas = []
def menu_principal():
    while True:
        print('[1] Criar conta')
        print('[2] Listar conta')
        print('[3] Acessar conta')
        print('[4] Sair ')
        try:
            resposta = int(input())
        except ValueError:
            print('voce digitou texto ao inves de numero')
            continue
        if resposta == 1:
            nome = input('informe o nome do conta: ')
            numero = input('informe o numero do conta: ')

            duplicada = False

            for cnt in contas:
                if numero == cnt.numero:
                    duplicada = True
                    break
            if duplicada:
                print('conta duplicada')
            else:
                conta = Contabancaria(nome,numero)
                contas.append(conta)


        elif resposta == 2:
            if not contas:
                print('Nao existe conta cadastrada')
            else:
                for conta in contas:
                    print(conta)
        elif resposta == 3:
            pedir_numero = input('informe o numero do conta: ')
            encontrou = False
            for conta in contas:
                if pedir_numero == conta.numero:
                    encontrou = True
                    conta.menu()
                    break
            if not encontrou:
                print('Conta nao encontrada')
        elif resposta == 4:
            break



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
                    print(f'saldo: R${self.saldo:,.2f}')
            elif resposta == 4:
                break
            else:
                print('opção inválida')
                continue


    def __str__(self):
        return f'conta {self.numero} de {self.titular} tem  R${self.saldo:,.2f} de saldo'

    def  depositar(self,valor):
        self.saldo += valor
        print(f'deposito de [green]R${valor:,.2f} Autorizado na conta {self.numero}[/]')

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de [green]R${valor:,.2f}[/] realizado com sucesso')
        else:
            print(f'Saque negado de [red]R${valor:,.2f} na conta {self.numero}. SALDO INSUFICIENTE[/]')


menu_principal()
