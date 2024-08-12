print('Escolha uma fruta: ')
print('1-Maça')
print('2-Laranja')
print('3-Banana')
produto = int(input('Qual sua escolha? '))
qnt = int(input('Quantas unidades? '))


if(produto == 1):
    pagar =  qnt * 2.3
    print(f'Você comprou {qnt} de maças. Total a pagar: {pagar}');


elif(produto == 2):
    pagar =  qnt * 3.6
    print(f'Você comprou {qnt} de laranjas. Total a pagar: {pagar}');

elif(produto == 3):
    pagar = qnt * 1.85
    print(f'Você comprou {qnt} de bananas. Total a pagar: {pagar}');

else:
     print('Prod  uto inexistente.');