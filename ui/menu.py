def menu_principal(banco):
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
            nome = input('informe o nome da conta: ')
            numero = input('informe o numero do conta: ')

           

            if banco.buscar_contas(numero):
                print('conta duplicada')
            else:
                banco.criar_contas(nome,numero)


        if resposta == 2:
            for conta in banco.listar_contas():
                print(conta)

                
        if resposta == 3:
            pedir_numero = input('informe o numero da conta:')
            conta = banco.buscar_contas(pedir_numero)
            if conta:
                conta.menu()
            else:
                print('conta nao encontrada')

        elif resposta == 4:
            break
            
        
           

