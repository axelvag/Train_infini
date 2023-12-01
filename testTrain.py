from train import Wagon 
from train import Train

w = Wagon(1, "beauWagon")
v = Wagon (2, "wagon")
print (w)

train = Train("train") 
print (train.estVide(train))
train.ajouter (w) 
print (train)
print (len (train))
print (train.attributsNiemeWagon (1))  
train.inserer_wagon (v, 1)
print(train)
train.changerNomNiemeWagon (2, "lewagon") 
print (train.enlever_wagon (2)) 
print (train.trouverWagonAvecNom ("beauWagon")) 
print (train.triNumWagonsOrdreCroissant()) 
