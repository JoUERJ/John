#Escreva um programa que leia um valor em metro e exiba convertido em centímetros e milímetros.

v = float(input('Digite um valor em metros:'))

cm = v*10**2
mm = v*10**3

print("O Valor em metros {} m, em centímetros {} cm, em milímetros {} mm.".format(v,cm,mm))