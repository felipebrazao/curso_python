# Exercício - sistema de perguntas e respostas

# perguntas = {
#     'Pergunta': 'Quanto é 2+2?',
#     'Opções': ['1', '3', '4', '5'],
#     'Resposta': '4',

#      'Pergunta2': 'Quanto é 5*5?',
#      'Opções2': ['25', '55', '10', '51'],
#      'Resposta2': '25',

#      'Pergunta3': 'Quanto é 10/2?',
#      'Opções3': ['4', '5', '2', '1'],
#      'Resposta3': '5',    
    

# }

# def jogo_de_pergunta():
#     print(perguntas['Pergunta'])
#     print(perguntas['Opções'])
#     input('Qual a resposta certa?: ')
#     print(f'A respota certa era {perguntas["Resposta"]}!')
#     print(perguntas['Pergunta2'])
#     print(perguntas['Opções2'])
#     input('Qual a resposta certa?: ')
#     print(f'A respota certa era {perguntas["Resposta2"]}!')
#     print(perguntas['Pergunta3'])
#     print(perguntas['Opções3'])
#     input('Qual a resposta certa?: ')
#     print(f'A respota certa era {perguntas["Resposta3"]}!')

# jogo_de_pergunta()    


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
