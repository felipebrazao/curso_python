# Exercícios
# Crie funções que duplicam, triplicam e quadriplicam
# O número recebido como parametro
# def multiplicador_de_numero(numero):
#         print(numero * 2)
#         print(numero * 3)
#         print(numero * 4)


# multiplicador_de_numero(4)




# def duplicador(numero):
#     return numero * 2
# def triplicador(numero):
#     return numero * 3
# def quadriplicador(numero):
#     return numero * 4

# print(duplicador(2))
# print(triplicador(2))
# print(quadriplicador(2))



def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))



