"""
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#       01234
#      -54321
string = 'ABCDE'    # 5 caracteres (len)
# print(bool(lista)) #falsy
# print(lista, type(lista))


#         0     1          2        3     4
#        -5    -4         -3       -2    -1
lista = [123, True, 'luiz otavio', 1.2, []] # ''
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))