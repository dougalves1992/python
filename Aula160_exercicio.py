import copy

produtos = [
    {'nome': 'Produto 5', 'Preco': 10.00},
    {'nome': 'Produto 1', 'Preco': 22.32},
    {'nome': 'Produto 3', 'Preco': 10.11},
    {'nome': 'Produto 2', 'Preco': 105.87},
    {'nome': 'Produto 4', 'Preco': 69.90},
]
produtos10 = [
    {**nproduto, 'Preco': round(nproduto['Preco'] * 1.1, 2)}
    for nproduto in produtos
]

print('Os valores originais')
for i in produtos:
    print(i)
print()

print('Os valores com 10 de aumento')
for i in produtos10:
    print(i)


# novos_produtos = []
# for elemento in produtos:
#     novos_produtos.append(elemento)

    
produtos_crescente = copy.deepcopy(produtos)

produtos_crescente_ordem = sorted(produtos_crescente, key=lambda x: x['nome'], reverse=True)
produtos_crescente_ordem_valor = sorted(produtos_crescente, key=lambda x: x['Preco'])


print()
print('A lista decrescente por nome')
for i in produtos_crescente_ordem:
    print(i)

print()
print('A lista crescente por Preco')
for i in produtos_crescente_ordem_valor:
    print(i)



