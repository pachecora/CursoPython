# Conversor de moedas

carteira = float(input("Quanto dinheiro você tem na carteira?R$ "))
preço_dolar = 5.16

valor_convertido = carteira / preço_dolar

print(f"A quantia de R${carteira:.2f} em moeda americana dá US${valor_convertido:.2f}")
