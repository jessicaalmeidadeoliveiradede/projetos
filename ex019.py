from random import choice
n1=input("primeiro aluno")
n2=input("segundo aluno")
n3=input("terceiro aluno")
n4=input("quarto aluno")
lista= [n1 , n2 , n3 , n4]
escolha=choice(lista)
print("o aluno escolido foi {} ".format(escolha))
