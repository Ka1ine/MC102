i = 0
dic = {}
lista = []
lista_final = []
lista_quase = []
listaa = []
while i == 0:
    entrada = input()

    if entrada not in dic:
        dic[entrada] = 0

    if entrada == "0":
        i = 1
    else:
        dic[entrada] += 1

for i in sorted(dic, key=dic.get, reverse=True):
    a = i, dic[i]
    lista.append(a)

lista.pop()

for i in lista:
    teste = f"{i[0]} {i[1]}"
    if i[0] == "Branco" or i[0] == "Nulo":
        lista_quase.append(i)
    else:
        lista_final.append(teste)

lista_quase = sorted(lista_quase)

if lista_quase != "":
    for j in lista_quase:
        teste = f"{j[0]}s {j[1]}"
        lista_final.append(teste)

for k in lista_final:
    print(k)
