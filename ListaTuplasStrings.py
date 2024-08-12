item = [] #ou list()
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: ')) #comando append adiciona a lista
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])  #cópia da lista item para lista mercado
    item.clear()  #clear limpa a lista de itens
print(mercado)


mercado = []
for i in range (3):
    nome = input('Digite o nome do item: ')
    qnt = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome, qnt, valor])
    print(mercado)

soma = 0
print('Lista de Compras: ')
print('-' * 20)
print('ITEM | QUANTIDADE | VALOR UNITÁRIO | TOTAL DO ITEM')
for item in mercado:
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print(f'Total a ser pago: {soma}')

