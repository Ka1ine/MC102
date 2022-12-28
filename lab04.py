###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Yasmin Kaline de Carvalho Silva
# RA: 241066
###################################################

pedido = 1
pedidos = []
while pedido != 0:
    pedidos.append(pedido)
    pedido = int(input())

pedidos.pop(0)
estoque = 0
vendas = 0

for i in pedidos:
    if i >= 0:
        estoque = estoque + i
    else:
        estoque = estoque + i
        if estoque < 0:
            print(f"Quantidade indisponível para a venda de {i*-1} unidades.")
            estoque = estoque - i
            continue
        vendas += 1

print(f"Quantidade de vendas realizadas: {vendas}")
print(f"Quantidade em estoque: {estoque}")
