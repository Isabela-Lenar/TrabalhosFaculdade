print('Bem vindo a Copiadora da Isabela!')

def escolha_servico():
    while True:
        print('Entre com o serviço desejado: ')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input(' ')
        if servico == 'DIG':
           return 1.10

        elif servico == 'ICO':
            return 1.00

        elif servico == 'IPB':
            return 0.40

        elif servico == 'FOT':
            return 0.20
        else:
            print('Escolha inválida. Entre com um tipo de serviço válido.')

def num_paginas(valortotal):
    while True:
        try:
            paginas = int(input('Entre com o número de páginas: '))
            if paginas <= 0:
                print('O número de páginas deve ser maior que zero.')
                continue
            if paginas <= 20:
                return valortotal * paginas
            elif paginas <= 200:
                return valortotal * paginas * 0.15
            elif paginas <= 2000:
                return valortotal * paginas * 0.20
            elif paginas <= 20000:
                return valortotal * paginas * 0.25
            else:
                print('Não aceitamos tantas páginas de uma vez. Por favor entre com o número novamente.')
        except ValueError:
            print('Por favor, entre com um número inteiro para o número de páginas.')

def servico_extra():
    while True:
            print('Deseja adicionar serviço extra? ')
            print('1-Encadernamento Simples - 15.00')
            print('2-Encadernamento Capa Dura - 40.00')
            print('0-Não desejo nada')
            extra = input(' ')
            if extra == '1':

                return  15.00

            elif extra == '2':

                return 40.00

            elif extra == '0':

                return 0

    print(f'Total: {(escolha_servico() * num_paginas()) + extra}')







valor_servico = escolha_servico()
desconto = num_paginas(valor_servico)
servico_extra()
print('Valor total: R$', desconto)