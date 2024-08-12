def valida_int (pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x


def fatorial (num):
    """
    Funções que retorna fatorial de num
    :param num: o número escolhido para ser calculado a fatorial
    :return: retorna o resultado da fatorial
    """

    fat = 1
    if num == 0:
        return fat
    # esta parte só executa caso num > 0
    for i in range(1, num + 1, 1):
        fat *= i
    return fat


x = valida_int('Digite um valor para calcular a fatorial: ', 0, 9999)
print(f'{x}! = {fatorial(x)}')

