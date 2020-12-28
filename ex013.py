# Reajuste salarial

valor_salario = float(input("Qual o valor do salário? R$"))

percentual_aumento = 0.15

salario_corrigido = valor_salario + (valor_salario * percentual_aumento)

print(f"Para um salário de R${valor_salario:.2f}, aumentado 15% fica R${salario_corrigido:.2f}")
