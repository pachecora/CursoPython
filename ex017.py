# Catetos e hipotenusa

from math import hypot

cateto_adjacente = float(input("Qual medida cateto adjacente: "))
cateto_oposto = float(input("Qual a medida do cateto oposto: "))

# hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** (1/2)
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print("A hipotenusa será {:.2f}".format(hipotenusa))
