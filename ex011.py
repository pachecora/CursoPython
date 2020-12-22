# Pintando parede

altura_parede = float(input("Digite a altura da parede em metros: "))
largura_parede = float(input("Digite a largura da parede em metros: "))

quanto_um_litro_pinta = 2

area_parede = altura_parede * largura_parede

quantidade_litros_tinta = area_parede / quanto_um_litro_pinta

print(f"A área da parede é {area_parede:.2f}m²")
print(f"Para uma parede de {area_parede:.2f}m² é necessário {quantidade_litros_tinta:.2f}L de tinta.")
