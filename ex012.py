# Calculando desconto

percentual_desconto = 5/100

valor_produto = float(input("Digite valor do produto: R$"))

valor_produto_corrigido = valor_produto - (valor_produto * percentual_desconto)

print(f"Com 5% de desconto, o produto que custava R${valor_produto} irá custar R${valor_produto_corrigido:.2f}")
