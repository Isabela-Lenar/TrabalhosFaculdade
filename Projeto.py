def escolha_servico(pergunta):
    serv = pergunta
    valor = 0
    while True:
        if serv == 'DIG':
            valor = 1.10
            print(valor)
            break

        elif serv == 'ICO':
             valor = 1.00
             print(valor)
             break

        elif serv == 'IPB':
             valor = 0.40
             print(valor)
             break

        elif serv == 'FOT':
             valor = 0.20
             print(valor)
             break

        elif serv != 
            print('Escolha inválida.Entre com um tipo de serviço valido.')
            input(' ')

        else:
            break











print('Bem vindo a Copiadora da Isabela!')
print('DIG - Digitalização')
print('ICO - Impressão Colorida')
print('IPB - Impressão Preto e Branco')
print('FOT - Fotocópia')
escolha_servico(input('Digite serviço desejado: '))