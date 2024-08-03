"""
Iterável -> str, range,  etc
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o próximo valor
iter -> me entregue o seu iterador
metodo = açao para manipular objetos (geralmente usando . alguma coisa)
"""
# for letra in texto
texto = 'Luiz'
# iteratador = iter(texto)

# while True:
#     try:
#         print(next(iteratador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
