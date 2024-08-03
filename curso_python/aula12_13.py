nome = 'Felipe'
altura = 1.78
peso = 70
imc = peso / (altura * altura) # IMC = peso / (altura x altura)

linha_1 = f'{nome} tem {altura:,.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc)


# Luiz Otávio tem 1.80 de altura, pesa 95 quilos e seu IMC é 29.32432432432
