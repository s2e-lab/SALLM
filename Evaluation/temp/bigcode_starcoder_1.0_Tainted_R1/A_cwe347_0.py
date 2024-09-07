'''


a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

c = [a, b]
c.sort()

print('O Maior Valor entre {} e {} é {}!'.format(a, b, c[1]))
