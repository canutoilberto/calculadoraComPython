def calculadora():
    try:
        operacao = int(
            input(
                'Escolha uma operação\n 1 - Soma(+)\n 2 - Subtração(-)\n 3 - Multiplicação(*)\n 4 - Divisão(/)\n'
                ' 5 - Divisão Inteira(%)\n 6 - Potenciação(**)\n'
            ))

        if operacao >= 7:
            print('ERRO! Digite uma operação válida')
            calculadora()
        else:
            n1 = float(input('Primeiro valor: '))
            n2 = float(input('Segundo Valor: '))


            def soma():
                resultado = n1 + n2
                print(f'{n1} + {n2} = {resultado}')
                nova_operacao()


            def subtracao():
                resultado = n1 - n2
                print(f'{n1} - {n2} = {resultado}')
                nova_operacao()


            def multiplicacao():
                resultado = n1 * n2
                print(f'{n1} * {n2} = {resultado}')
                nova_operacao()


            def divisao():
                try:
                    resultado = n1 / n2
                    print(f'{n1} / {n2} = {resultado}')
                    nova_operacao()
                except ZeroDivisionError:
                    print('Não é possível divisão por Zero')
                    nova_operacao()


            def divisao_inteira():
                try:
                    resultado = n1 % n2
                    print(
                        f'O resto da divisão entre {n1} e {n2} é igual a: {resultado}'
                    )
                    nova_operacao()
                except ZeroDivisionError:
                    print('Não é possível divisão por Zero')
                    nova_operacao()


            def potenciacao():
                resultado = n1**n2
                print(f'{n1} elevado a {n2} é igual a: {resultado}')
                nova_operacao()

            if operacao == 1:
                soma()
            elif operacao == 2:
                subtracao()
            elif operacao == 3:
                multiplicacao()
            elif operacao == 4:
                divisao()
            elif operacao == 5:
                divisao_inteira()
            elif operacao == 6:
                potenciacao()
    except ValueError:
        print('Digite apenas números.')
    nova_operacao()


def nova_operacao():
    while True:
        opcao = int(input('Deseja continuar?\n 1 - Sim\n 2 - Não\n'))
        if opcao == 1:
            calculadora()
        if opcao == 2:
            print('Até mais!')
            break
        else:
            print('Digite uma opção válida.')
            nova_operacao()
