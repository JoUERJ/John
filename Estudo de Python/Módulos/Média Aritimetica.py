#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input("Digite sua nota da P1: "))
print('Você precisa tirar {} na P2 para ser aprovado...'.format(14-n1))



n2 = float(input("Digite sua nota da P2: "))

m = (n1 + n2)/2

if m >= 7:
    print("Sua média é {}. Você foi aprovado!".format(m))
else:
    print("Sua média é {}. Você foi reprovado...".format(m))    

