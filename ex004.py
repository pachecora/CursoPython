# Dissecando uma variável

variavel = input("Digite algo para ser processado: ")

print(f"O tipo primitivo deste valor é: {type(variavel)}")

# O método isspace() é só tem espaços? Retorna True ou False.
print(f"Só tem espaços? {variavel.isspace()}")

# Testa se a string digitada pode ser convertido em um número
print(f"É um número? {variavel.isnumeric()}")

print(f"É alfabético? {variavel.isalpha()}")

print(f"É alfa-numérico? {variavel.isalnum()}")

print(f"Está em maiúsculo? {variavel.isupper()}")

print(f"Está em minúsculo? {variavel.islower()}")

print(f"Está capitalizada? (primeira letra em maiúscula?) {variavel.istitle()}")
