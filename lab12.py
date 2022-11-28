###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Yasmin Kaline de Carvalho Silva
# RA: 241066
###################################################
import numpy as np


def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))


def expansao(matriz, tamanho):
    tamanho_novo = []
    matriz_nova = []

    for elem in tamanho:
        elem_ = 2 * int(elem) - 1
        tamanho_novo.append(int(elem_))

    var_linha = 0
    for i in range(tamanho_novo[1]):
        matriz_nova.append([])
        var = 0
        for j in range(tamanho_novo[0]):
            if j % 2 == 0 and i % 2 == 0:
                matriz_nova[i].append(matriz[i // 2][j // 2])
            else:
                matriz_nova[i].append(".")

    # Passo 2
    var_linha = 0
    for i in range(tamanho_novo[1]):
        var = 0
        for j in range(tamanho_novo[0]):
            if j % 2 != 0 and i % 2 == 0:
                matriz = np.array(matriz)
                submatriz = matriz[0 + var_linha:1 + var_linha, 0 + var:2 + var]
                matriz_nova[i][j] = (submatriz.sum() // submatriz.size)
                var += 1
        if i % 2 == 0:
            var_linha += 1

    # Passo 3
    var_linha = 0
    for i in range(tamanho_novo[1]):
        var = 0
        for j in range(tamanho_novo[0]):
            if j % 2 == 0 and i % 2 != 0:
                matriz = np.array(matriz)
                submatriz = matriz[0 + var_linha:2 + var_linha, 0 + var:1 + var]
                matriz_nova[i][j] = (submatriz.sum() // submatriz.size)
                var += 1
        if i % 2 != 0:
            var_linha += 1

    # Passo 3
    var_linha = 0
    for i in range(tamanho_novo[1]):
        for j in range(tamanho_novo[0]):
            if j % 2 != 0 and i % 2 != 0:
                matriz = np.array(matriz)
                submatriz = [matriz_nova[i + 1][j + 1], matriz_nova[i + 1][j - 1], matriz_nova[i - 1][j + 1],
                             matriz_nova[i - 1][j - 1]]
                matriz_nova[i][j] = (sum(submatriz) // len(submatriz))

    return matriz_nova


def retracao(A, tamanho):
    tamanho_novo = []
    matriz_nova = []

    for elem in tamanho:
        resto = int(elem) % 2
        if resto == 0:
            elem_ = int(elem) / 2
        else:
            elem_ = (int(elem) + 1) / 2

        tamanho_novo.append(int(elem_))

    var_linha = 0
    for i in range(tamanho_novo[1]):
        matriz_nova.append([])
        var = 0
        for j in range(tamanho_novo[0]):
            A = np.array(A)
            submatriz = A[0 + var_linha:2 + var_linha, 0 + var:2 + var]
            matriz_nova[i].append(submatriz.sum() // submatriz.size)
            var += 2
        var_linha += 2

    return matriz_nova


_ = input()

tamanho = input().split()

_ = input()

A = []
for i in range(int(tamanho[1])):
    linha = [int(x) for x in input().split()]
    A.append(linha)

tipo = input()
if tipo == "expansao":
    imagem = expansao(A, tamanho)
else:
    imagem = retracao(A, tamanho)

imprimir_imagem(imagem)
