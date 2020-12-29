# Sorteando um item na lista

from random import randint

lista_alunos = list()

lista_alunos.append(input("Primeiro aluno: "))
lista_alunos.append(input("Segundo aluno: "))
lista_alunos.append(input("Terceiro aluno: "))
lista_alunos.append(input("Quarto aluno: "))

print(f"O aluno escolhido foi {lista_alunos[randint(0, 3)]}")
