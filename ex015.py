# Aluguel de carros

preço_aluguel_por_dia = 60.00
preço_aluguel_por_km_rodado = 0.15

dias_alugados = int(input("Quantos dias o carro foi alugado? "))
kms_rodados = float(input("Quantos kms rodados? "))

preço_carro = dias_alugados * preço_aluguel_por_dia + (kms_rodados * preço_aluguel_por_km_rodado)

print(f"O valor do aluguel do carro para {dias_alugados} dias e {kms_rodados}kms é R${preço_carro:.2f}")
