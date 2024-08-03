"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeado tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumeto (valor)
"""
def soma(x, y, z):
    # Definição
    print(f'x={x} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma
soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')