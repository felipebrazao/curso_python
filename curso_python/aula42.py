frase = 'O python é uma linguagem de programação' \
    'Multiparadigma. ' \
    'Python foi criado por Guido van Rossum'

indice = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while indice < len (frase): # while = enquanto for maior que o numero de caracteres da frase é bala
    letra_atual = frase[indice]

    if letra_atual == ' ':
        indice += 1

        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    indice += 1

    print('A letra que apareceu mais vezes foi ' 
          f'"{letra_apareceu_mais_vezes}" que apareceu '
          f'{qtd_apareceu_mais_vezes}x'
          )