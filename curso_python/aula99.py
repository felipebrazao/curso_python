# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import aula99_package.modulo
# from aula99_package import modulo
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)

# from aula99_package.modulo import fala_oi, soma_do_modulo


# print(__name__)
# fala_oi()

from aula99_package import soma_do_modulo
from aula99_package import fala_oi

print(soma_do_modulo(3,5))
print(fala_oi())