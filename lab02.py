###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: Yasmin Kaline de Carvalho Silva
# RA: 241066
###################################################

D1 = int(input())
V1 = int(input())
T = int(input())
D2 = int(input())
V2 = int(input())

horas = T * 24
SpaceX = D1 / V1
Blue = (D2 / V2) + horas

if SpaceX < Blue:
    print("True")
else:
    print("False")
