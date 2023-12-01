class Wagon:
    '''
    Creation d'un wagon que l'on attache à une suite de wagons, et ayant 
    un nom, et un numero  (non forcement sa position dans le convoi) 
    (0 = locomotive, 1 = premier wagon, ...)
    On pourra donner un numero et un nom par défaut ! 
    attributs : precedent, numero, nom
    '''
   
    def __init__(self,numero=1,nom="Wagon 1",precedent=None):
        self.numero=numero
        self.nom=nom
        self.precedent=precedent
        
    def __str__(self):
        return f'nom : {self.nom} numero : {self.numero} wagon precedent : {self.precedent}'


class Train (Wagon):
    
    '''
    Creation d'un train : on le caractérise par son nom et dernier_wagon puisque 
    ce wagon est relie aux autres (le connaissant, on a acces a l'ensemble du train)
    attributs : nom, dernier_wagon   
    '''
    
    def __init__ (self, nom) : 
        self.nom = nom 
        self.dernierWagon = None 
        
    def __len__ (self) : 
        c = self.dernierWagon 
        if c == None :                       # s'il n'y a pas de dernier wagon, cela signifie que le train est vide donc sa longueur est égal à 0 
            return 0

        else : 
            i = 1 
            while c.precedent is not None :      # tant que le precedent du dernier wagon n'est pas la locomotive 
                c = c.precedent                  # on avance dans le train 
                i = i + 1                        # on ajoute 1 à i 
            return i                             # on retourne la longueur du train 
        
    def __str__ (self) :        
        c = self.dernierWagon    # dernier wagon     
        affichage = f'le train s appelle {self.nom}  '
        
        while c is not None :                                        # tant que le precedent du dernier wagon n'est pas la locomotive 
            affichage += f'le Wagon suivant est : {c.nom} son numero est : {c.numero}  '      # on met dans affichage les wagons suivants 
            c =  c.precedent 
        affichage +=  f'et nous avons ensuite la locomotive ' 
        return affichage
        
    def estVide (self,nom) : 
        return nom.dernierWagon is None       # teste si le nom du dernier wagon et égal à None et retourne True ou False 
            
        
    def ajouter (self, wagon): 
        wagon.precedent = self.dernierWagon   # met au wagon ajouté l'ancien dernier wagon car il se situe maintenant avant 
        self.dernierWagon = wagon             # maintenant le wagon ajouté est le dernier wagon 
    
    
    
    def attributsNiemeWagon (self,n):
        '''
        le premier wagon est la tête du train, et le dernier est le dernier wagon ajouté        
        '''        
        c = self.dernierWagon  
        if  n == 0 :                                            # si n est égal à la place de la locomotive 
            return f"la locomotive s'appelle {self.nom} " 
        elif  n > self.dernierWagon.numero :                    # si n est superieur au numero du dernier wagon 
            return f"il n'y a pas autant de wagons donc pas de numéro {n}"
        elif  n < 0 :                                           # si n est superieur à 0 
            return f"il n'y a pas de train avec un rang négatif, mais ça pourrait être le cas"
        else:
            while c.precedent is not None : 
                while n != c.numero :                               # tant que n est différent du numero du wagon testé 
                    c = c.precedent 
            return c                                                # retourne le wagon demandé 
            
    def enlever_wagon(self,n):
        ''' 
    Soit on utilise un train temporaire (une copie) que l'on crée à partir de l’autre sans prendre en compte le wagon que l'on veut enlever
    
        '''
    
        trainCopie = Train ("trainCopie")           
        c = self.dernierWagon  
        if  n == 0 : 
            return "on ne peut pas enlever la locomotive"
        elif  n > self.dernierWagon.numero : 
            return f"il n'y a pas autant de wagons donc pas de numéro {n}"
        elif  n < 0 : 
            return f"il n'y a pas de train avec un rang négatif, mais ça pourrait être le cas"
        else:

            while c is not None :                    # tant que c est différent de None   
                if n != c.numero :                   # si n est différent du numero du wagon testé 
                    trainCopie.ajouter (c)           # on ajoute le wagon testé au train copie 
                c = c.precedent
            
            nom = self.nom                           # on met le nom du train dans nom 
            del (self)                               # on supprime le train 
            train = trainCopie                       # on met le train copie dans un nouveau train 
            train.nom = nom                          # on met le nom dans le nom du nouveau train 
            return train                             # on retourne le train 
        
    def inserer_wagon (self, wagon, n) : 
        '''
    On veut inserer un wagon en n-ieme position, il faut donc 
    casser le lien entre le n-1 ieme wagon et le nieme existant
        '''
       
        trainCopie = Train ("trainCopie")   
        c = self.dernierWagon 
        if self.dernierWagon is None : 
                self.ajouter (wagon) 
        else : 
            if  n == 0 : 
                return "on ne peut pas enlever la locomotive"
            if  n > c.numero : 
                return f"il n'y a pas autant de wagons donc pas de numéro {n}"
            elif  n < 0 : 
                return f"il n'y a pas de train avec un rang négatif, mais ça pourrait être le cas"
            else:
                while c is not None : 
                    if n > c.numero :                        # si le wagon testé est avant le wagon qu'on veut inserer 
                        trainCopie.ajouter (c)               # on ajoute le wagon testé à train copie 
                    if n-1 == c.numero :                     # si le wagon testé est le wagon avant celui qu'on veut inserer 
                        wagon.precedent = c                  # on change son wagon precedent pour mettre celui qu'on veut inserer  
                    c = c.precedent
               
                c = self.dernierWagon 
                while c is not None :                        
                    if n == c.numero :                       # si le wagon testé est le wagon ou devrait être le wagon qu'on veut inserer 
                        c.precedent = wagon                  # on change le wagon precedent du wagon qu'on veut inserer en mettant le wagon testé 
                        trainCopie.ajouter (wagon)           # on ajoute le wagon qu'on veut inserer au train copie 
                        trainCopie.ajouter (c)               # on ajoute le wagon testé au train copie 
                    c = c.precedent
                
                c = self.dernierWagon 
                while c is not None :                        
                    if n < c.numero :                    # si le wagon testé est aprés le wagon qu'on veut inserer 
                        trainCopie.ajouter (c) 
                    c = c.precedent         
                          
                nom = self.nom                           # on met le nom du train dans nom 
                del (self)                               # on supprime le train 
                train = trainCopie                       # on met le train copie dans un nouveau train 
                train.nom = nom                          # on met le nom dans le nom du nouveau train 
                return train                             # on retourne le train 
            
    def changerNomNiemeWagon (self, n, nom) : 
        '''
        Pour changer le nom du n- ieme wagon
        '''
        
        c = self.dernierWagon
        if  n == 0 : 
            return "on ne peut pas changer le nom du train"
        if  n > c.numero : 
            return f"il n'y a pas autant de wagons donc pas de numéro {n}"
        elif  n < 0 : 
            return f"il n'y a pas de train avec un rang négatif, mais ça pourrait être le cas"
        else:
            wagon = self.attributsNiemeWagon (n)                     # on cherche le wagon à la place n 
            wagon.nom = nom                                          # on change le nom du wagon 
            return "le nom a ete change" 
        
    def trouverWagonAvecNom (self, nom) : 
        '''
        Pour trouver si un wagon particulier ( numero et ou nom ) se trouve dans le train
        renvoyer un booleen : True ou False
        '''
        
        c = self.dernierWagon 
        i= 1 
        while c is not None :                                # tant que le wagon testé est différent de la locomotive 
            if nom == c.nom or nom == c.numero :             # si le nom rentré est égal au nom du wagon ou que le nom rentré est égal au numéro du wagon 
                i = 0                                        
            c = c.precedent
        return i == 0                                        # on retourne True ou False si i est égal à 0 

    def triNumWagonsOrdreCroissant (self) : 
        '''
        Un simple tri sélection suffit ici mais on peut utiliser d'autres façons
        '''
        
        c = self.dernierWagon 
        i = len (self)                                       # i est égal à la longueur du train 
        while c.precedent is not None :                      # tant que le precedent du wagon testé est différent de la locomotive 
            c.numero = i 
            i = i - 1 
            c = c.precedent 
        return self 
 



    





