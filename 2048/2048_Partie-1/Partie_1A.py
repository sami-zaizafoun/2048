#ZAIZAFOUN Sami
#MADER Antoine
#Groupe 1B, L1 INFORMATIQUE

from random import *
from copy import *

###################################### PARTIE 1A ######################################
#######################################################################################

# variables globales
global n
g1=[[2,2,2,2],[4,0,2,8],[0,16,32,0],[128,256,1024,2048]]
g2=[[2,2,2,2],[4,0,2,8],[0,16,32,0],[128,256,16,32]]
n=6

########################## Question 1 ##########################

def creegrille(n, val):
    res=[0]*n
    for i in range(n):
        res[i]= [val]*n            
    return res
    print (res[i]," ",end="\n")

########################## Question 2 ##########################
    
def affiche(grille):
    for i in grille:
        taille_grille='{:>7}'*len(grille)
        print(str(taille_grille).format(*i))

########################## Question 3 ##########################
            
def appartient(x,g):
    for i in g:
        if x in i:
            return True
    return False

def gagnante(g):
    for i in g:
        if 2048 in i:
            return True
    return False

def verif(g):
    for i in g:
        if 0 in i:
            return True
    return None

def pleine(g):
    veri=verif(g)
    if veri is not True:
        print("Votre grille est pleine.\n")
        return True
    return False

########################## Question 4 ##########################

def maxi(g):
    res=list(map(max,g))
    return max(res)

########################## Question 5 ##########################
    
def lescases(g,val):
    res=[]
    for x,j in enumerate(g):
        for y, i in enumerate(j):
            if i== val:
                res+=[x,y],
    return res

def vides(g):
    res=[]
    for x,j in enumerate(g):
        for y, i in enumerate(j):
            if i== 0:
                res+=[x,y],
    return res

def ajoutAlea(g,val):
    c=vides(g)[randrange(0,len(vides(g)))]
    g[c[0]][c[1]]=val

def init(n):
    base=[2,4]
    creation= creegrille(n, 0)
    ran1, ran2= base[randrange(0,2)], base[randrange(0,2)]
    ajoutAlea(creation,ran1)
    ajoutAlea(creation,ran2)
    return creation

g3= init(6)

########################## Question 6 ##########################

def haut(g):
    ###Mouvements
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j]!=0:
                for a in range(len(g)):
                    if g[a][j]==0 and a<i:
                        g[a][j]=g[i][j]
                        g[i][j]=0
                        break

def additionn_haut(g): 
    ###Additions                 
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i-1][j]==g[i][j] and i>0:
                g[i-1][j]*=2
                g[i][j]=0

###########(Mouvements sur une grille de 4x4)###########
##    i=0
##    for j in range(0,len(g)):
##        if g[i][j]!=0 or g[i+1][j]!=0 or g[i+2][j]!=0 or g[i+3][j]!=0:
##            if g[i][j]==0:
##                while g[i][j]==0:
##                    g[i][j]= g[i+1][j]
##                    g[i+1][j]= g[i+2][j]
##                    g[i+2][j]= g[i+3][j]
##                    g[i+3][j]= 0
##                    
##            if g[i+1][j] == 0:
##                while g[i+1][j]== 0:
##                    g[i+1][j]= g[i+2][j]
##                    g[i+2][j]= g[i+3][j]
##                    g[i+3][j]= 0
##                    break
##                
##
##            if g[i+2][j]== 0:
##                while g[i+2][j]== 0:
##                    g[i+2][j]= g[i+3][j]
##                    g[i+3][j]= 0
##                    break
##                
##        if g[i][j]== g[i+1][j]:
##            g[i][j]= g[i][j]+g[i+1][j]
##            g[i+1][j]= g[i+2][j]
##            g[i+2][j]= g[i+3][j]
##            g[i+3][j]= 0
##
##        if g[i+1][j]== g[i+2][j]:
##            g[i+1][j]= g[i+1][j]+g[i+2][j]
##            g[i+2][j]= g[i+3][j]
##            g[i+3][j]= 0
##
##        if g[i+2][j]== g[i+3][j]:
##            g[i+2][j]= g[i+2][j]+g[i+3][j]
##            g[i+3][j]= 0                

def bas(g):
    ###Mouvements
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j]!=0:
                for a in range(len(g)):
                    if g[a][j]==0 and a>i:
                        g[a][j]=g[i][j]
                        g[i][j]=0
                        break

def additionn_bas(g):
    ###Additions
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i-1][j]==g[i][j] and i>0:
                g[i-1][j]*=2
                g[i][j]= 0

###########(Mouvements sur une grille de 4x4)###########
##    i=0
##    for j in range(0,len(g)):
##        if g[i][j]!=0 or g[i-1][j]!=0 or g[i-2][j]!=0 or g[i-3][j]!=0:
##            if g[i+3][j]== 0:
##                while g[i+3][j]== 0:
##                    g[i+3][j]= g[i+2][j]
##                    g[i+2][j]= g[i+1][j]
##                    g[i+1][j]= g[i][j]
##                    g[i][j]= 0
##                    
##                    
##            if g[i+2][j]== 0:
##                while g[i+2][j]== 0:
##                    g[i+2][j]= g[i+1][j]
##                    g[i+1][j]= g[i][j]
##                    g[i][j]= 0
##                    break
##                    
##            if g[i+1][j]== 0:
##                while g[i+1][j]== 0:
##                    g[i+1][j]= g[i][j]
##                    g[i][j]= 0
##                    break
##          
##        if g[i+3][j]== g[i+2][j]:
##            g[i+3][j]= g[i+3][j]+g[i+2][j]
##            g[i+2][j]= g[i+1][j]
##            g[i+1][j]= g[i][j]
##            g[i][j]= 0
##    
##        if g[i+2][j]== g[i+1][j]:
##            g[i+2][j]= g[i+2][j]+g[i+1][j]
##            g[i+1][j]= g[i][j]
##            g[i][j]= 0
##
##        if g[i+1][j]== g[i][j]:
##            g[i+1][j]= g[i+1][j]+g[i][j]
##            g[i][j]= 0

def droite(g):
    ###Mouvements
    for j in range(len(g)):
        for i in range(len(g[j])):
            if g[i][j]!=0:
                for a in range(len(g)):
                    if g[i][a]==0 and a>j:
                        g[i][a]=g[i][j]
                        g[i][j]=0
                        break

def additionn_droite(g):
    ###Additions
    for j in range(len(g)):
        for i in range(len(g[j])):
            if g[i][j-1]==g[i][j] and j>0:
                g[i][j]*=2
                g[i][j-1]= 0

###########(Mouvements sur une grille de 4x4)###########
##    j=0
##    for i in range(0,len(g)):
##        if g[i][j]!=0 or g[i][j-1]!=0 or g[i][j-2]!=0 or g[i][j-3]!=0:
##            if g[i][j+3]==0:
##                while g[i][j+3]==0:
##                    g[i][j+3]= g[i][j+2]
##                    g[i][j+2]= g[i][j+1]
##                    g[i][j+1]= g[i][j]
##                    g[i][j]= 0
##                    
##            if g[i][j+2] == 0:
##                while g[i][j+2]== 0:
##                    g[i][j+2]= g[i][j+1]
##                    g[i][j+1]= g[i][j]
##                    g[i][j]= 0
##                    break                    
##
##            if g[i][j+1]== 0:
##                while g[i][j+1]== 0:
##                    g[i][j+1]= g[i][j]
##                    g[i][j]= 0
##                    break
##                
##        if g[i][j+3]== g[i][j+2]:
##            g[i][j+3]= g[i][j+3]+g[i][j+2]
##            g[i][j+2]= g[i][j+1]
##            g[i][j+1]= g[i][j]
##            g[i][j]= 0
##    
##        if g[i][j+2]== g[i][j+1]:
##            g[i][j+2]= g[i][j+2]+g[i][j+1]
##            g[i][j+1]= g[i][j]
##            g[i][j]= 0
##
##        if g[i][j+1]== g[i][j]:
##            g[i][j+1]= g[i][j+1]+g[i][j]
##            g[i][j]= 0
                    
def gauche(g):
    ###Mouvements
    for j in range(len(g)):
        for i in range(len(g[j])):
            if g[i][j]!=0:
                for a in range(len(g)):
                    if g[i][a]==0 and a<j:
                        g[i][a]=g[i][j]
                        g[i][j]=0
                        break

def additionn_gauche(g):
    ###Additions
    for j in range(len(g)):
        for i in range(len(g[j])):
            if g[i][j-1]==g[i][j] and j>0:
                g[i][j-1]*=2
                g[i][j]=0
                    
###########(Mouvements sur une grille de 4x4)###########
##    j=0
##    for i in range(0,len(g)):
##        if g[i][j]!=0 or g[i][j+1]!=0 or g[i][j+2]!=0 or g[i][j+3]!=0:
##            if g[i][j]==0:
##                while g[i][j]==0:
##                    g[i][j]= g[i][j+1]
##                    g[i][j+1]= g[i][j+2]
##                    g[i][j+2]= g[i][j+3]
##                    g[i][j+3]= 0
##                    
##            if g[i][j+1] == 0:
##                while g[i][j+1]== 0:
##                    g[i][j+1]= g[i][j+2]
##                    g[i][j+2]= g[i][j+3]
##                    g[i][j+3]= 0
##                    break
##
##            if g[i][j+2]== 0:
##                while g[i][j+2]== 0:
##                    g[i][j+2]= g[i][j+3]
##                    g[i][j+3]= 0
##                    break
##
##        if g[i][j]== g[i][j+1]:
##            g[i][j]= g[i][j]+g[i][j+1]
##            g[i][j+1]= g[i][j+2]
##            g[i][j+2]= g[i][j+3]
##            g[i][j+3]= 0
##
##        if g[i][j+1]== g[i][j+2]:
##            g[i][j+1]= g[i][j+1]+g[i][j+2]
##            g[i][j+2]= g[i][j+3]
##            g[i][j+3]= 0
##
##        if g[i][j+2]== g[i][j+3]:
##            g[i][j+2]= g[i][j+2]+g[i][j+3]
##            g[i][j+3]= 0


########################## Question 7 ##########################                   

def partie(n):
    g= init(n)
    affiche(g)
    base= [2,4]
    choix=""
    continuer=""
    while choix!= "0":
        choix= input("\n"+"Choisissez la direction (H: haut, B: bas, D: droite, G: gauche et 0: quitter): ")
        verif_g= deepcopy(g)        
        ran= base[randrange(0,2)]
        choix= choix.lower()

        ###Les mouvemenets
        if choix=="h":
            haut(g)
            additionn_haut(g)
            haut(g)
            
        elif choix=="b":
            bas(g)
            additionn_bas(g)
            bas(g)

        elif choix=="d":
            droite(g)
            additionn_droite(g)
            droite(g)
            

        elif choix=="g":
            gauche(g)
            additionn_gauche(g)
            gauche(g)
            
        ### Verification s'il y a possibilité de se deplacer
        if verif_g!= g:
            ajoutAlea(g,ran)
            affiche(g)
            
        elif verif_g== g:
            affiche(g)

        ### Verification des conditions de perte ou victoire
        if gagnante(g) is True:    
            while continuer !="o":            
                print("Félicitations, vous avez gagné","\n")
                continuer= input("Voulez-Vous continuer O/N: ")
                continuer= continuer.lower()
                if continuer== "o":
                    break
                elif continuer== "n":
                    print("Fin de partie, Votre score est: ", end="")
                    return maxi(g)               

        elif pleine(g) is True:
            break
        
    print("Fin de partie, Votre score est: ", end="")
    return maxi(g)
