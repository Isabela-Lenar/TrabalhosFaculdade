v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

if ((v1 > 0) and (v2 > 0) and (v3 > 0) and (v1 + v2 > v3 and v2 + v1 > v3 and v3 + v1 > v2)):
    if v1 != v2 and v2 != v3 and v1 != v3:
      print('Triângulo Escaleno');

    else:
         if (v1 == v2 and v2 == v3):
            print('Triângulo Equilatero');
         else:
             print('Triângulo Isósceles');

else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.');


