print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressiona qualquer outra tecla para sair.')


op = input('Qual operação deseja realizar? ')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite segundo valor: '))

if (op == '+'):
    res =  x + y
    print(f'Resultado: {x} + {y} = {res}');


elif(op == '-'):
        res = x - y
        print(f'Resultado: {x} - {y} = {res}');

elif(op == '*'):
        res = x * y
        print(f'Resultado: {x} * {y} = {res}');

elif(op == '/'):
        res = x / y
        print(f'Resultado: {x} / {y} = {res}');

else:
    print('Encerrando o programa...')