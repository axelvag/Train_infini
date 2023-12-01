# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:36:01 2020

@author: 33782
"""

# ********************************************************************************
# CLASSE WAGON - CREATION D'UNE CLASSE en POO avec une List Python
# ********************************************************************************

class Wagon:                                    

    '''
    Creation d'un wagon que l'on attache à une suite de wagons, et ayant
    un nom, et un numero (non forcement sa position dans le convoi)
    (0 = locomotive, 1 = premier wagon, ...)
    On pourra donner un numero et un nom par défaut !
    attributs : precedent, numero, nom
    '''
 
    def __init__(self,numero,nom,precedent):      #création de la méthode spéciale constructeur avec les attributs numéro,nom et précedent
        self.numero = numero                      
        self.nom = nom
        self.precedent = precedent
    
    def __str__(self):                            #méthode spéciale qui surcharge et permettra d’utiliser print pour afficher les attributs du wagon
        return f'Nom du wagon:{self.nom} \nNumero du wagon:{self.numero}  '
    
# ********************************************************************************
# CLASSE TRAIN - CREATION SECONDE D'UNE CLASSE en POO avec une List Python
# ********************************************************************************
        
class Train:

    '''
    Creation d'un train : on le caractérise par son nom et dernier_wagon puisque
    ce wagon est reli'e aux autres (le connaissant, on a acces a l'ensemble du train)
    attributs : nom, dernier_wagon
    '''

    def __init__(self, nom, dernier_wagon):       #création de la méthode spéciale constructeur avec les attributs nom et dernier_wagon
        self.nom = nom                   
        self.dernier_wagon = dernier_wagon
        
    '''def __len__(self):                            #Surcharge de la méthode spéciale len qui permettra d’utiliser print pour obtenir la longueur du train
        c = self.dernierWagon 
        if c == None :                            #si il n'y a pas de dernier wagon (car il est None)                
            return 0                              #donc on retourne 0 qui est bien la longueur du train
        else : 
            i = 1 
            while c.precedent is not None :       #tant que le precedent du dernier wagon n'est pas la locomotive 
                c = c.precedent                   #on avance dans le train 
                i = i + 1                         #on ajoute 1 à i 
            return i                              #on retourne la longueur du train'''
                
    def __str__(self):                            #Méthode spéciale qui surcharge __str__ 
        c = self.dernier_wagon                    #on transmet dernier_wagon à la variable c
        affichage="Wagon final"                   #on met dans affichage le texte "Wagon final"
        while c>0 :                               #bloucle, tant que c est supérieur à 0 alors on rentre dans la boucle
            affichage += self.dernier_wagon       #on met ensuite dans affichage le nouveau dernier wagon
            c = self.dernier_wagon -1             #la variable décremente dernier_wagon jusqu'à la locomotive
        affichage += "Locomotive"                 #on met "locomotive" en mémoire dans affichage, en sortie de boucle
        return affichage                          #on renvoi affichage et son contenu
        
                
    def estVide(self):                            #création d'une méthode public qui permet de savoir si la liste train est vide
        if self.dernier_wagon==0:                 #si il n'y a pas de dernier wagon alors il ne reste que la locomotive donc le train est vide
            print("Le train est vide")
        else:                                     #sinon le train n'est pas vide
            print("Le train n'est pas vide")
            
    def ajouter(self,elem,n):                     #méthode public qui permet d'ajouter un wagon 
        for i in range (0,n-1):                   #en partant du rang 0, on active n fois la boucle for en ajoutant un wagon, à chaque tour de boucle, au bout de la liste (train)
            self.train.append(elem)
        self.dernier_wagon = self.dernier_wagon+n #la place du dernier wagon est ensuite actualisée au nouvel emplacement dans la liste
        c = self.dernier_wagon                    #création d'une variable intermédiaire c qui désigne le dernier wagon
        
    '''def attributsNiemeWagon(self,n): 
        #le premier wagon est la tête du train, et le dernier est le dernier wagon ajouté      
        c = self.dernierWagon  
        if n == 0 :                                            #si n est égal à la place de la locomotive alors on retourne le f string
            return f"la locomotive s'appelle {self.nom} " 
        elif n > self.dernierWagon.numero :                    #si n est superieur au numero du dernier wagon alors on retourne le f string
            return f"il n'y a pas autant de wagons donc pas de numéro {n}"
        elif n < 0 :                                           #si n est superieur à 0 alors on retourne le f string
            return f"il n'y a pas de train avec un rang négatif, mais ça pourrait être le cas"
        else:
            while c.precedent is not None : 
                while n != c.numero :             #tant que n est différent du numero du wagon testé 
                    c = c.precedent 
            return c                              #retourne le wagon demandé
         
    def enlever_wagon(self,e):                    #création d'une méthode public qui permet d'enlever un wagon au rang demandé
        #Soit on utilise un train temporaire (une copie) que l'on crée à partir de l’autre
        #sans prendre en compte le wagon que l'on veut enlever
        if not self.estVide():                    #si la liste n'est pas vide, on supprime la wagon au rang(e) indiqué
            del self.train(e)
        else:                                     #sinon l'opération n'est pas faisable
            return False
            
    def inserer_wagon(self,elem,rang):            #crétion d'une méthode public qui permet d'insérer un wagon (elem) au rang demandé
        #On veut inserer un wagon en n-ieme position, il faut donc
        #casser le lien entre le n-1 ieme wagon et le nieme existant
        self.train.insert(rang,elem)              #insert un wagon au rang indiqué dans la liste train
        
    
    def changerNomNiemeWagon (self,n,newnom):     #création d'une méthode qui change le nom nième wagon par newnom au rang (n) demandé
        #Pour changer le nom du n- ieme wagon
        self.wagon(n)[1] = newnom                 #remplace par le newnom le nom(au rang 1)du wagon au rang n
        
    
    def trouverWagonAvecNom (self):
        #Pour trouver si un wagon particulier ( numero et ou nom ) se trouve dans le train
        #renvoyer un booleen : True ou False
        c = self.dernierWagon 
        i= 1 
        while c is not None :                      #tant que le wagon testé est différent de la locomotive 
            if nom == c.nom or nom == c.numero :   #si le nom rentré est égal au nom du wagon ou que le nom rentré est égal au numéro du wagon 
                i = 0                                        
            c = c.precedent
        return i == 0                              #on retourne True ou False si i est égal à 0 
        
        
    def triNumWagonsOrdreCroissant (self):         #méthode public qui tri par sélection la liste train
        c = self.dernierWagon 
        i = len (self)                             #i est égal à la longueur du train 
        while c.precedent is not None :            #tant que le precedent du wagon testé est différent de la locomotive 
            c.numero = i 
            i = i - 1 
            c = c.precedent 
        return self '''