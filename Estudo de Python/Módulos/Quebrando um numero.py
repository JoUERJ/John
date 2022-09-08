#Crie um programa que leia um número real qualquer pelo telcado e mostre na tela a sua porção inteira.

from math import trunc

num = float(input("Digite um número real: "))

print("O valor digitado é {} e sua porção inteira é {}.".format(num,int(num)))

print("O valor digitado é {} e sua porção inteira é {}.".format(num, trunc(num)))
