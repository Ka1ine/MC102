###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Yasmin Kaline de Carvalho Silva
# RA: 241066
###################################################

semana = int(input())
hora = input()
minuto = input()
estudante = input()
pagamento = input()

horas = str(hora) + str(minuto)

df = {'Dia da semana': [1, 2, 3, 4, 5, 6, 7], 'Preço vespertino': [30, 15, 15, 15, 20, 20, 30],
      'Preço noturno': [30, 20, 20, 30, 30, 40, 40], 'Desconto vespertino': [30, 50, 50, 50, 50, 50, 20],
      'Desconto noturno': [30, 50, 50, 50, 50, 30, 20]}

index = semana - 1


def verificar_estudante(horario):
    preco = df[horario][index]
    ingresso = str(preco)
    ingresso = int(ingresso) * 0.5
    print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))


def verificar_pagamento(desconto):
    preco = df[horario][index]
    ingresso = str(preco)
    desconto_final = df[desconto][index]
    ingresso = int(preco) - (int(ingresso) * (int(desconto_final) / 100))
    print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))


def pegar_valor(horario):
    preco = df[horario][index]
    ingresso = int(preco)
    print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))


if int(horas) >= 1830:
    horario = 'Preço noturno'
    desconto = 'Desconto noturno'
    if estudante == "S":
        verificar_estudante(horario)
    else:
        if pagamento == "C":
            verificar_pagamento(desconto)
        else:
            pegar_valor(horario)
else:
    horario = 'Preço vespertino'
    desconto = 'Desconto vespertino'
    if estudante == "S":
        verificar_estudante(horario)
    else:
        if pagamento == "C":
            verificar_pagamento(desconto)
        else:
            pegar_valor(horario)
