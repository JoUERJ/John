#Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa.
import math
from math import hypot, sqrt

co = float(input("Cateto Oposto: "))

ca = float(input("Cateto Adjecente: "))

hi = hypot(co, ca)

print("A hipotenusa dos catetos {} e {} é {:.2f}.".format(co,ca,hi))

#==================================================================================================#

hi = sqrt(math.pow(ca, 2) + math.pow(co, 2))


print(co,ca,hi)