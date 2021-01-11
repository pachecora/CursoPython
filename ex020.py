# Sorteando uma ordem na lista

from random import shuffle

lista_alunos = list()

lista_alunos.append(input("Aluno 1: "))
lista_alunos.append(input("Aluno 2: "))
lista_alunos.append(input("Aluno 3: "))
lista_alunos.append(input("Aluno 4: "))

shuffle(lista_alunos)

print(f"A ordem escolhida foi {lista_alunos}")
