### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]
vendas_agrupado = {}
for item in vendas:
    categoria_agg = item['categoria']
    valor_agg = item['valor']
    if categoria_agg in vendas_agrupado:
        vendas_agrupado[categoria_agg] += valor_agg
    else:
        vendas_agrupado[categoria_agg] = valor_agg

print(vendas_agrupado)
