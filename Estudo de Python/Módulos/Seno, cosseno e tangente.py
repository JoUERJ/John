#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos , tan, radians

angulo = float(input("Digite um ângulo de uma circunferência (ou seja, entre 0° e 360°): "))

seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))

print("O ângulo de {} tem o seno de {:.2f}.".format(angulo, seno))
print("O ângulo de {} tem o cosseno de {:.2f}.".format(angulo, coss))
print("O ângulo de {} tem a tangente de {:.2f}.".format(angulo, tang))

