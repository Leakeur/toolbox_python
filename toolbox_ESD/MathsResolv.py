#!usr/bin/env python
#-*- coding:utf-8 -*-
#Exo1 Python - Wilson Leclercq ESD17

# 5 9 4 est une solution delta > 0

from math import sqrt #Importation module math.sqrt

print("\nBienvenue dans le calculateur d'équation de second degré pour ax+bx+x\n") #Petite présentation d'acceuil

#Demander à l'utilisateur les valeurs de A,B et C qu'il souhaite calculer.
#+Obliger l'utilisateur à rentrer des nombres et non des lettres. (try)
try:
	A = float(input("selectionner une valeur pour A : "))
	B = float(input("selectionner une valeur pour B : "))
	C = float(input("selectionner une valeur pour C : "))
except:
	print("il faut absolument indiquer un chiffre !")
else:
	delta = B*B-4*A*C
	print(delta)
#La 1ere possibilité, si le resultat du delta est inf. à 0
if delta < 0:
	print("ce delta ne peut pas être calculé car il est inferieur à 0")
#2ème possibilité, si le resultat du delta est égal a 0, il existe une possibilité donc faire le calcul et afficher l'unique déterminant.
if delta == 0:
	print("Delta est égal à 0, donc une solution trouvé")
	X0=-B/2*A
	print(X0)
#3ème possibilité, si delta est sup. à 0, il existe deux possibilité, donc faire les deux calculs pour trouvé les déterminants et les affichers.
if delta > 0:
	print("Delta est supérieur à 0, donc deux solution trouvé")
	X1=-B-sqrt(delta)/2*A
	X2=-B+sqrt(delta)/2*A
	print("X1: {} et X2: {}".format(X1, X2))
