#Faça um programa que leia num número qualquer e mostre na tela a sua tabuada.

n = float(input("Digite um número qualquer:"))

i = 0

while i <= 10:
    d = n*i
    print("{} X {} = {}.".format(n,i,d))
    i = i + 1