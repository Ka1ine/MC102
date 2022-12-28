if __name__ == '__main__':

    def rodar_90(peca):
        nova_peca = []
        transposta = list(map(list, zip(*peca)))

        for linha in transposta:
            nova_peca.append(list(reversed(linha)))
        return nova_peca

    def mudar_peca(peca):
        for i in range(len(peca)):
            for j in range(len(peca[0])):
                if peca[i][j] == "X":
                    peca[i][j] = "."
                else:
                    peca[i][j] = "X"
        return peca

    def verificar_tabuleiro(A, C):
        continuar = True
        total = 0
        for i in range(len(C) - len(A) + 1):
            for j in range(len(C[0]) - len(A[0]) + 1):
                posicao = []
                for k in range(len(A)):
                    for m in range(len(A[0])):
                        lista = []
                        if C[i + k][j + m] != A[k][m]:
                            if A[k][m] != "X":
                                posicao = []
                                continuar = False
                            else:
                                lista.append(i + k)
                                lista.append(j + m)
                                posicao.append(lista)
                        else:
                            lista.append(i + k)
                            lista.append(j + m)
                            posicao.append(lista)
                    if not continuar:
                        posicao = []
                        continuar = True
                        break
                if posicao:
                    total += 1
        return total

    # Tabueliro
    T = int(input())
    tabuleiro = []
    for _ in range(T):
        tabuleiro.append(input().split())

    # Peça
    P = int(input())
    peca = []
    for _ in range(P):
        peca.append(input().split())

    peca = mudar_peca(peca)

    final = []
    for i in range(4):
        if i != 0:
            peca = rodar_90(peca)

        final.append(str(verificar_tabuleiro(peca, tabuleiro)))

    print(",".join(final))
