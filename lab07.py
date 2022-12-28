###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: Yasmin Kaline de Carvalho Silva
# RA: 241066
###################################################

tropas_de_defesa = int(input())
defesa = []
for i in range(tropas_de_defesa):
    defesa.append(input())

tropas_de_ataque = int(input())
ataque = []
for j in range(tropas_de_ataque):
    ataque.append(input())

for p in range(len(defesa)):
    venceu = 0
    perdeu = 0
    empate = 0
    for k in range(len(ataque)):
        index = k + p
        if index <= (len(defesa) - len(ataque) + 1):
            if int(ataque[k]) > int(defesa[index]):
                venceu += 1
            else:
                perdeu += 1
            if int(ataque[k]) == int(defesa[index]):
                empate += 1

    if venceu + empate > perdeu:
        print(f"Vitória posicionando as tropas a partir da posição {p+1}")
        exit()


print("Derrota")
