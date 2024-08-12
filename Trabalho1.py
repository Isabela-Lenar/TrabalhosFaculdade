print('Bem vindo a Loja da Isabela Souza') #print para mostrar a mensagem de boas vindas na tela.

preco = float(input('Entre com o valor do produto: ')) #float para identificar o input como número.
quant = float(input('Entre com a quantidade do produto: '))
res = preco * quant #resultado da multiplicação do valor com a quantidade do produto.
desc = (f'O valor SEM DESCONTO: ')

print(f'O valor SEM DESCONTO: {res}') #

if (res < 2500):
    print(f'O valor SEM DESCONTO: {res}')
#Se o resultado for menos que 2500 não há desconto.

elif (res >= 2500 and res < 6000):
    print(f'O valor COM DESCONTO: {res - (res * 4/100) }');
#Se o resultado por maior ou igual 2500 e menos que 6000 terá desconto de 4%.
#Entre colchetes a expressão que calcula o desconto.

elif (res >= 6000 and res < 10000):
   print(f'O valor COM DESCONTO: {res - (res * 7/100) }');
#Se o resultado for maior ou igual a 6000 e menos que 10000 terá desconto 7%.
#Entre colchetes a expressão que calcula o desconto.

else:
   print(f'O valor COM DESCONTO: { res - (res * 11/100) }');
#Se o resultado for maior ou igual a 10000 terá desconto de 11%.