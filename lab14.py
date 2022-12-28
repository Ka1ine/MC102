def caminho(tabuleiro, posicao_atual, posicao_final, cor):
    counter = 0
    if posicao_atual[0] == posicao_final[0] and posicao_atual[1] == posicao_final[1]:
        return True
    elif posicao_atual in paes:
        return False
    else:
        verificacao = [posicao_atual[0] + 1 < len(tabuleiro),
                       posicao_atual[0] - 1 > 0,
                       posicao_atual[1] + 1 < len(tabuleiro[0]),
                       posicao_atual[1] - 1 > 0]
        sinal = [posicao_atual[0] + 1, posicao_atual[0] - 1, posicao_atual[0], ]
        for i in range(4):
            if verificacao:
                nova_cor = tabuleiro[posicao_atual[0] + 1][posicao_atual[1]]
                if nova_cor != cor:
                    if posicao_atual not in paes:
                        paes.append(list(posicao_atual))
                    nova_posicao = list(posicao_atual)
                    nova_posicao[0] = posicao_atual[0] + 1
                    result = caminho(tabuleiro, nova_posicao, posicao_final, nova_cor)
                    if result:
                        return True
                else:
                    counter += 1
            if posicao_atual[0] - 1 > 0:
                nova_cor = tabuleiro[posicao_atual[0] - 1][posicao_atual[1]]
                if nova_cor != cor:
                    if posicao_atual not in paes:
                        paes.append(list(posicao_atual))
                    nova_posicao = list(posicao_atual)
                    nova_posicao[0] = posicao_atual[0] - 1
                    result = caminho(tabuleiro, nova_posicao, posicao_final, nova_cor)
                    if result:
                        return True
                else:
                    counter += 1
            if posicao_atual[1] + 1 < len(tabuleiro[0]):
                nova_cor = tabuleiro[posicao_atual[0]][posicao_atual[1] + 1]
                if nova_cor != cor:
                    if posicao_atual not in paes:
                        paes.append(list(posicao_atual))
                    nova_posicao = list(posicao_atual)
                    nova_posicao[1] = posicao_atual[1] + 1
                    result = caminho(tabuleiro, nova_posicao, posicao_final, nova_cor)
                    if result:
                        return True
                else:
                    counter += 1
            if posicao_atual[1] - 1 > 0:
                nova_cor = tabuleiro[posicao_atual[0]][posicao_atual[1] - 1]
                if nova_cor != cor:
                    if posicao_atual not in paes:
                        paes.append(list(posicao_atual))
                    nova_posicao = list(posicao_atual)
                    nova_posicao[1] = posicao_atual[1] - 1
                    result = caminho(tabuleiro, nova_posicao, posicao_final, nova_cor)
                    if result:
                        return True
                else:
                    counter += 1
        if counter == 4:
            return False


L = int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = [int(i) for i in input().split()]

posicao_inicial = [l1, c1]
posicao_final = [l2, c2]
paes = []
resultado = caminho(tabuleiro, posicao_inicial, posicao_final, tabuleiro[l1][c1])
if resultado:
    print("caminho encontrado")
else:
    print("caminho nao encontrado")
