n = int(input())
matriz = [input().split() for _ in range(n)]
time1, time2 = 0, 0
time = input()
jogadores = int(input())

for i in range(jogadores):
    letras = input()
    linha = 0
    coluna = 0
    for letra in letras:
        if letra == "L":
            coluna += 1
        if letra == "O":
            coluna -= 1
        if letra == "N":
            linha -= 1
        if letra == "S":
            linha += 1

        if matriz[linha][coluna] == "*":
            if i % 2 == 0:
                time1 += 1
            else:
                time2 += 1
            matriz[linha][coluna] = "."

if time == "vermelho":
    print(f"Tesouros encontrados pelo time azul: {time2}")
    print(f"Tesouros encontrados pelo time vermelho: {time1}")
    if time1 > time2:
        print("Vitoria do time vermelho")
    if time1 == time2:
        print("Empate")
    if time1 < time2:
        print("Vitoria do time azul")
else:
    print(f"Tesouros encontrados pelo time azul: {time1}")
    print(f"Tesouros encontrados pelo time vermelho: {time2}")
    if time2 > time1:
        print("Vitoria do time vermelho")
    if time1 == time2:
        print("Empate")
    if time2 < time1:
        print("Vitoria do time azul")
