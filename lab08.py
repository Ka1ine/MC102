palavra_certa = input()

for i in range(6):
    palavra_imprimir = []
    palavra_teste = input()
    for j in range(len(palavra_teste)):
        for k in range(len(palavra_certa)):
            if palavra_teste[j] == palavra_certa[k]:
                if j == k:
                    palavra_imprimir.append(palavra_teste[j].capitalize())
                    break
                else:
                    palavra_imprimir.append(palavra_teste[j])
                    break
            if k + 1 == len(palavra_certa):
                palavra_imprimir.append("_")

    if palavra_certa == palavra_teste:
        print(palavra_certa.upper())
        print("Resposta correta")
        exit()

    palavra_imprimir = ("".join(palavra_imprimir))
    print(palavra_imprimir)

    if i == 5:
        print(f"Palavra correta: {palavra_certa}")
        exit()
