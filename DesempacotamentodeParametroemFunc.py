def soma(*num): #a função recebe uma variável num, e o * indica que será uma tupla de tamanho  qualquer
    acumulador = 0
    print(f'Tupla: {num}')
    for i in num:
        acumulador += i
    return acumulador

#Programa Principal
print(f'Resulta: {soma(1, 2)}\n')
print(f'Resulta: {soma(1, 2, 3, 4, 5, 6, 7, 8, 9)}\n')
