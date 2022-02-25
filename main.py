import string


def soma():
    numero1 = int(input('Digite o primeiro Numero: '))
    numero2 = int(input('Digite o Segudo Numero: '))

    resultado = numero1 + numero2

    print(f'Resultado: {resultado}')


def subtracao():
    numero1 = int(input('Digite o primeiro Numero: '))
    numero2 = int(input('Digite o Segudo Numero: '))

    resultado = numero1 - numero2

    print(f'Resultado: {resultado}')


def multiplicacao():
    numero1 = int(input('Digite o primeiro Numero: '))
    numero2 = int(input('Digite o Segudo Numero: '))

    resultado = numero1 * numero2

    print(f'Resultado: {resultado}')


def divisao():
    numero1 = int(input('Digite o primeiro Numero: '))
    numero2 = int(input('Digite o Segudo Numero: '))

    resultado = numero1 / numero2

    print(f'Resultado: {resultado}')


def princpipal():
    while True:
        print('==================')
        print('🅲🅰🅻🅲🆄🅻🅰🅳🅾🆁🅰')
        print('==================')
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair')
        opcao = int(input('>>> '))

        if opcao == 1:
            soma()
        elif opcao == 2:
            subtracao()
        elif opcao == 3:
            multiplicacao()
        elif opcao == 4:
            divisao()
        elif opcao == 5:
            print('Saindo...')
            break
        else:
            print('Opção inválida, digite um valor de 1 a 5')


princpipal()
