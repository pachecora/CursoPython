# seno, cosseno e tangente

from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo que você deseja: "))
angulo_em_radianos = radians(angulo)

seno = sin(angulo_em_radianos)
cosseno = cos(angulo_em_radianos)
tangente = tan(angulo_em_radianos)

print(f"O ângulo de {angulo} tem o SENO {seno:.2f}")
print(f"O ângulo de {angulo} tem o COSSENO {cosseno:.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE {tangente:.2f}")
