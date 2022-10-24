i = 0
dic = {}
dic2 = {}
while i == 0:
    pedido = input()
    if " : " in pedido:
        pedido = pedido.split(" : ")
        produto = pedido[0]
        quantidade = int(pedido[1])

        if produto not in dic:
            dic[produto] = 0
            dic2[produto] = [0, 0]

        if int(quantidade) <= 0:
            quantidade_estoque = dic.get(produto)
            if quantidade_estoque >= int(quantidade) * -1:
                dic[produto] -= quantidade * -1
                dic2[produto][1] += 1
            else:
                print(f'Quantidade indisponivel para a venda de {quantidade * -1} unidade(s) do produto {produto}.')

        else:
            dic[produto] += quantidade
            dic2[produto][0] += 1
    else:
        dic_ordenado = sorted(dic)
        for produto in dic_ordenado:
            if dic[produto] >= 0 and dic2[produto][0] > 0:
                print(f'Produto: {produto}')
                print(f'Quantidade em Estoque: {dic.get(produto)}')
                print(f'Pedidos de Compra: {dic2[produto][0]}')
                print(f'Pedidos de Venda: {dic2[produto][1]}')
        i = +1
