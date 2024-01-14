"""
Secret Santa
Date : 30/11/22
Auteur : Maxime L
Ce script permet de mélanger une liste donnée de prénoms et donne un nom avec un code hexadécimal d'un autre nom
"""
#lien utile pour décripter : https://www.rapidtables.com/convert/number/hex-to-ascii.html

from random import *

"""
Creation des listes et mélanges
"""
def main( estCripte ):
    #Initialisations
    tabPersonne = ["Lars"        , "Maxime"          , "Marcus"          , "Léane"         , "Anais"         , "Camille"           , "Alexandre"             ]
    tabMelange  = ["Lars"        , "Maxime"          , "Marcus"          , "Léane"         , "Anais"         , "Camille"           , "Alexandre"             ]
    tabHex      = ["||4c617273||", "||4d6178696d65||", "||4d6172637573||", "||4ce9616e65||", "||416e616973||", "||43616d696c6c65||", "||416c6578616e647265||"]
    nbPersonne  = 7

    #Melange
    cpt = 0
    while cpt < nbPersonne:
        alea = randint( 0, nbPersonne-1 )
        temp = tabMelange[ cpt ]
        tempHex = tabHex[ cpt ]

        tabMelange[ cpt ] = tabMelange[ alea ]
        tabHex[ cpt ] = tabHex[ alea ]

        tabMelange[ alea ] = temp
        tabHex[ alea ] = tempHex

        #on verifie qu'une personne n'est pas le père noel d'elle meme
        if tabMelange[ cpt ] == tabPersonne[ cpt ] or tabMelange[ alea ] == tabPersonne[ alea ]:
            cpt = 0
        else:
            cpt += 1

    #affichage
    if not estCripte:
        cpt = 0
        while cpt < nbPersonne:
            print(tabPersonne[cpt] + " est le Secret Santa de "+ tabMelange[cpt] + "(" + tabHex[cpt] + ")")
            cpt += 1
    else :
        cpt = 0
        while cpt < nbPersonne:
            print(tabPersonne[cpt] + " est le Secret Santa de " + tabHex[cpt] + ".")
            cpt += 1

"""
Fonction de test
"""
def test():
    #boucle pour les test
    cpt = 0
    while cpt < 10:
        main()
        cpt += 1

"""
Appel du programme
"""
estCripte = True
main( estCripte )
