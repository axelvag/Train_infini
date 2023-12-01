# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:14:13 2020

@author: 33782
"""
# ********************************************************************************
# Test des classes Wagon et Train
# ********************************************************************************

from ClassInfinityTrain import Wagon,Train

w = Wagon(1,"wagon1", 0)
print (w)

train = Train("InfinityTrain", 0)
print (train.estVide())

n=int(input("nombre de wagon à ajouter ?"))
print (train.ajouter(w,n))
print (train.ajouter(w,1))

print (train.estVide())

#print (len(train))

#e=int(input("Quel wagon voulez vous enlever ?"))
#print (train.enlever_wagon(e))

#rang=int(input("A quel rang voulez vous insérer le wagon?"))
#print (train.inserer_wagon(w,rang))

#n=int(input("De quel wagon voulez vous changer le nom?"))
#newnom=input("Le nouveaux nom du wagon?")
#print(train.changerNomNiemeWagon(n,newnom))

#print (train.triNumWagonsOrdreCroissant)