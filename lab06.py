##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Yasmin Kaline de Carvalho Silva
# RA: 241066
##################################################


torre = [int(panqueca) for panqueca in input().split()]
loc = int(input())

while loc != 0:
    lista_num = []
    newList = []
    # Pega os numero e inverte eles
    for i in range(loc):
        lista_num.append(torre[i])
        newList = [num for num in reversed(lista_num)]

    # Todos os numeros finais
    lista_final = torre[loc:]

    # adiciona os numeros finais na lista
    for j in range(len(lista_final)):
        newList.append(lista_final[j])

    torre = newList
    loc = int(input())

torre_ordenada = sorted(torre)

if torre_ordenada == torre:
    print("Torre estavel")
else:
    print("Torre instavel")






