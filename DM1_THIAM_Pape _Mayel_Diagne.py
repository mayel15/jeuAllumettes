#coding:utf-8

#-------------------------- DM1 | THIAM Pape Mayel Diagne ------------------

#------------------------------ JEU D'ALLUMETTES ---------------------------

""" Le jeu d'allumettes est un jeu qui se joue à deux. Il y a un nombre initial d'allumettes bien fixe.
Au fur et à mesure du jeu, chaque joueur devra retirer 1,2 ou 3 allumettes jusqu'a ce que celui qui retire
la dernière allumette gagne. Le jeu est mis en place de tel sorte que si le joueur choisit de retirer un nombre
différent de 1,2 ou 3; il perd son tour et c'est à l'autre joueur de jouer. Et si le nombre d'allumette restant est 3,
il sera obligé de retirer un nombre correcte selon la situation"""

"""
NB - On fera attention aux cas où le nombre d'allumettes restant est 3, 2 ou 1 allumettes et que le joueur sera obligé de retirer un nombre correcte
afin que la dernière allumette puisse être retirée par le futur gagnant.
"""
#voir consigne : le jeu doit continuer jusqu'à ce que la dernière allumette soit prise

#-------------------------------- Sous Programmes --------------------------

def infoJoueurs():                                                         #permet d'avoir les noms des joueurs
    print("Bienvenue dans JEU D'ALLUMETTES")
    nomJoueur1 = input("Entrez le nom du 1er joueur : ")                   #nomJoueur1 est le nom du Joueur 1
    nomJoueur2 = input("Entrez le nom du 2e joueur : ")                    #nomJoueur2 est le nom du Joueur 2 
    return(nomJoueur1,nomJoueur2)

def NbrAlluInitial (n):     #permet de définir et d'afficher le nombre initial d'allumettes 
    afficheNbrA(n)          #n est le nombre initiale d'allummettes

def afficheNbrA(n):                                                        #permet d'afficher le nombre d'allumettes
    print("\n\nIl y a",n,"allumettes","\n",n*"| ")

def tourDeJeu_PourUnDeuxTroisA(i):
    """permet d'indiquer le tour de jeu pour chaque joueur lorsque le nombre d'allumettes restant est soit 1,2 ou 3 allumettes
    pour que tout gagnant soit obligé de tirer la dernière allumettes"""
    if i%2 == 0:        
        print("C'est à",nomJoueur2,"de jouer.\n")
    if i%2 != 0:
        print("C'est à",nomJoueur1,"de jouer.\n")

#-------------------------------- Programme Principale ---------------------

(nomJoueur1,nomJoueur2)=infoJoueurs()
n = 10 
afficheNbrA(n)                    #n est le nombre initiale d'allummettes
i = 0                             #permet d'indiquer le tour de chaque joueur

while 0 < n :
    
    if i%2 == 0:
        print("C'est à",nomJoueur1,"de jouer.\n")
    if i%2 != 0:
        print("C'est à",nomJoueur2,"de jouer.\n")
    x = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))   #x est le nombre d'allumettes retirés par le joueur 1 à chaque tour
    if 1 <= x <= 3 :
        n = n - x
        
        if n == 3:
            afficheNbrA(n)
            tourDeJeu_PourUnDeuxTroisA(i)
            y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
            while y != 1 and y != 2:
                print("\n\nValeur invalide. Veuillez choisir une aure correcte.\n")
                afficheNbrA(n)
                tourDeJeu_PourUnDeuxTroisA(i)
                y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
            n = n - y
            i = i + 1
            if n == 2:
                afficheNbrA(n)
                tourDeJeu_PourUnDeuxTroisA(i)
                y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
                while  y != 1 :
                    print("\n\nValeur invalide. Veuillez choisir une aure correcte.\n")
                    afficheNbrA(n)
                    tourDeJeu_PourUnDeuxTroisA(i)
                    y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
                    #y est la valeur choisie par les joueurs à l'intérieur des boucles qui sont dans une condition
                n = n - y
                i = i + 1
                if n == 1:
                    afficheNbrA(n)
                    tourDeJeu_PourUnDeuxTroisA(i)
                    y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))  
                    while y != 1 :
                        print("\n\nValeur invalide. Veuillez choisir une aure correcte.\n")
                        afficheNbrA(n)
                        tourDeJeu_PourUnDeuxTroisA(i)
                        y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
                    n = n - y
                    if i%2 == 0 and n == 0:
                        print("\n",nomJoueur2,"a gagné. Félicitations !\n\nJeu réalisé par Pape Mayel Diagne THIAM ")
                    elif i%2 != 0 and n == 0:
                        print("\n",nomJoueur1,"a gagné. Félicitations !\n\nJeu réalisé par Pape Mayel Diagne THIAM ")        
            
        elif n == 2:
            afficheNbrA(n)
            tourDeJeu_PourUnDeuxTroisA(i)
            y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
            while  y != 1 :
                print("\n\nValeur invalide. Veuillez choisir une aure correcte.\n")
                afficheNbrA(n)
                tourDeJeu_PourUnDeuxTroisA(i)
                y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
            n = n - y
            i = i + 1
            if n == 1:
                afficheNbrA(n)
                tourDeJeu_PourUnDeuxTroisA(i)
                y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
                while y != 1 :
                    print("\n\nValeur invalide. Veuillez choisir une aure correcte.\n")
                    afficheNbrA(n)
                    tourDeJeu_PourUnDeuxTroisA(i)
                    y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
                n = n - y
                if i%2 == 0 and n == 0:
                    print("\n",nomJoueur2,"a gagné. Félicitations !\n\nJeu réalisé par Pape Mayel Diagne THIAM ")
                elif i%2 != 0 and n == 0:
                    print("\n",nomJoueur1,"a gagné. Félicitations !\n\nJeu réalisé par Pape Mayel Diagne THIAM ")
            
        elif n == 1:
            afficheNbrA(n)
            tourDeJeu_PourUnDeuxTroisA(i)
            y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
            while y != 1 :
                print("\n\nValeur invalide. Veuillez choisir une aure correcte.\n")
                afficheNbrA(n)
                tourDeJeu_PourUnDeuxTroisA(i)
                y = int(input("Combien d'allumettes voulez vous retirer ? (1,2 ou 3)"))
            n = n - y
            if i%2 == 0 and n == 0:
                print("\n",nomJoueur2,"a gagné. Félicitations !\n\nJeu réalisé par Pape Mayel Diagne THIAM ")
            elif i%2 != 0 and n == 0:
                print("\n",nomJoueur1,"a gagné. Félicitations !\n\nJeu réalisé par Pape Mayel Diagne THIAM ")        

        else:
            afficheNbrA(n)
            
    else:
        print("\n\nValeur entrée invalide. Tour perdu.\n")
        afficheNbrA(n)
        
    i = i + 1






