#ZAIZAFOUN Sami
#MADER Antoine
#Groupe 1B, L1 INFORMATIQUE

from tkinter import*
from tkinter import messagebox
from Partie_2A import*
from copy import*
from random import *

#############################
##### variables globales #### 
#############################

n= 6 #Taille de la grille
nb= 0 #Le nombre d'origine dans la case
c=90 #Dimension d'une case supposée carrée
x0= 5 #Coordonnées x du point en haut à gauche
y0= 5 #Coordonnées y du point en haut à gauche
cpt= 0 #Compteur coups

base=[2,4] #valeurs qui s'ajoutent

############ Dictionnaires des couleurs ############

dico_couleurs_case={2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563",
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61",    ### Dictionnaire pour le fond des cases remplies
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e", 4096:"#656363"}

dico_couleurs_chiffre={2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2",
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2",    ### Dictionnaire pour les chiffres
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2", 4096:"#f9f6f2"}

#################################### Les fonctions sur la grille ####################################


############ Cette fonction sert à dessiner la grille ############

def dessineGrille(g):        
    can.delete(ALL)
    for i in range(n+1):
        can.create_line(x0+c*i, y0,x0+c*i,y0 + n*c,fill="#92877d")
        can.create_line(x0, y0+c*i,x0+n*c ,y0+c*i,fill="#92877d")

############ Cette fonction sert à créer et afficher les carré ############ 
def Creecarré(g):    
    for i in range(n):
        for j in range(n):
            x=g[i][j]
            if x!=0:
                can.create_rectangle((x0 +c*j+2, y0+c*i+2), (x0 +c*(j+1)-2, y0+c*(i+1)-2), fill= dico_couleurs_case.get(x), outline= dico_couleurs_case.get(x))

def couleur(nb):
    for i in range(n):
        for j in range(n):
            nb=g[i][j]
            if nb!=0:
                can.create_text((x0 +c*j+45,y0+c*i+45), text= nb, font=("Ubuntu",28,"bold"), fill= dico_couleurs_chiffre.get(nb))

############ Les commandes pour les touches clavier ############
def clavier(event):
    if event.keycode == 38:
        H()
        
    if event.keycode == 40:
        B()
        
    if event.keycode == 37:
        G()
        
    if event.keycode == 39:
        D()
    
####################################################################

###################### Conditions pour afficher le message ######################

def compteur():
    global cpt
    cpt+=1

def surprise():
    global nb
    sup= randint(0, 4)
    res=[]
    
    if cpt%10== 0:
        if sup== 0:
            m.config(state=NORMAL)
            m.delete("1.0", END)
            m.insert(END, " Pas de surprise."+"\n Nombre de coups: "+ str(cpt))
            m.config(state=DISABLED)

        elif sup== 1:
            for i in g:
                i[0], i[n-1]=i[n-1], i[0]
                
                m.config(state=NORMAL)
                m.delete("1.0", END)
                m.insert(END, " Inversion 1ère et dernière \n colonne.")
                m.config(state=DISABLED)

                dessineGrille(m)
                Creecarré(g)
                couleur(nb)

        elif sup== 2:
            o= g[0]
            g[0], g[len(g)-1]=g[len(g)-1], g[0]
            dessineGrille(m)
            Creecarré(g)
            couleur(nb)
                    
            m.config(state=NORMAL)
            m.delete("1.0", END)
            m.insert(END, " Inversion 1ère et dernière \n ligne.")
            m.config(state=DISABLED)

        elif sup== 3:
            for i in range(n):
                for j in range(n):
                    nb=g[i][j]
                    if nb==8:
                        g[i][j]=2
                        dessineGrille(m)
                        Creecarré(g)
                        couleur(nb)
                        
                    if nb==2:
                        g[i][j]= 8
                        dessineGrille(m)
                        Creecarré(g)
                        couleur(nb)

                                                
            m.config(state=NORMAL)
            m.delete("1.0", END)
            m.insert(END, " Inversion des 2 et 8."+"\n Nombre de coups: "+ str(cpt))
            m.config(state=DISABLED)
                        
                                    

        elif sup== 4:
            ajoutAlea(g, 32)
            
            dessineGrille(m)
            Creecarré(g)
            couleur(nb)
            
            m.config(state=NORMAL)
            m.delete("1.0", END)
            m.insert(END, " Un 32 se rajoute."+"\n Nombre de coups: "+ str(cpt))
            m.config(state=DISABLED)

            
        
    
def Message(m):
    global game,continuer, cpt

    ### Si le joueur gagne (possibilite de choisir s'il veut continuer) ###
    if gagnante(g) and continuer== None: 
        m.config(state=NORMAL)
        m.delete("1.0", END)
        m.insert(END, " Vous avez gagné.\n Votre score est: "+ str(maxi(g)))
        m.config(state=DISABLED)
        game= None
        continuer= messagebox.askyesno("print", "Voulez vous continuez?")
        if continuer== True:
            game= True

    ### Si le joueur perd ###
    elif pleine(g):
        m.config(state=NORMAL)
        m.delete("1.0", END)
        m.insert(END, " Vous avez perdu.\n Votre score est: "+ str(maxi(g)))
        m.config(state=DISABLED)
        game= None

    ### Affichage du score ###
    else:
        m.config(state=NORMAL)
        m.delete("0.0", END)
        m.insert(END, " Votre score: "+str(maxi(g))+"\n Nombre de coups: "+ str(cpt))
        m.config(state=DISABLED)

    ### Arret du jeu apres atteindre 4096 ###
    for i in g:
        if 4096 in i:
            game= None
            m.config(state=NORMAL)
            m.delete("0.0", END)
            m.insert(END, " Vous avez gagné le jeu.\n Votre score: "+str(maxi(g)))
            m.config(state=DISABLED)

    if cpt%10==0 and cpt!=0:
        surprise()
            
###################################################################################
        


#####################################  Fonctions Tkinter #####################################

############ Cette fonction sert à fermer la fenêtre ############
        
def monquitter():    
    dessin.quit()
    dessin.destroy()


############ defenir les boutons des directions ############    
def H():
    global game
        
    if game== True:
        g_verif= deepcopy(g)
        haut(g)
        additionn_haut(g)
        haut(g)
        if g_verif!= g:
            ran= base[randrange(0,2)]
            ajoutAlea(g,ran)
            compteur()
            
        dessineGrille(m)
        Creecarré(g)
        couleur(nb)
        Message(m)
        
        
    if game== False:
        game= True
        bdem.config(state=DISABLED)
        aban.config(state=NORMAL)
        new()
            
        dessineGrille(m)
        Creecarré(g)
        couleur(nb)
        Message(m)
        
def D():
    global game
        
    if game== True:
        g_verif= deepcopy(g)
        droite(g)
        additionn_droite(g)
        droite(g)
        if g_verif!= g:
            ran= base[randrange(0,2)]
            ajoutAlea(g,ran)
            compteur()
            
        dessineGrille(m)
        Creecarré(g)
        couleur(nb)
        Message(m)

    if game== False:
        game= True
        bdem.config(state=DISABLED)
        aban.config(state=NORMAL)
        new()
            
        dessineGrille(m)
        Creecarré(g)
        couleur(nb)
        Message(m)
    
def G():
    global game
        
    if game== True:
        g_verif= deepcopy(g)
        gauche(g)
        additionn_gauche(g)
        gauche(g)
        if g_verif!= g and cpt!=0:
            ran= base[randrange(0,2)]
            ajoutAlea(g,ran)
            compteur()

        dessineGrille(m)
        Creecarré(g)
        couleur(nb)
        Message(m)

    if game== False:
        game= True
        bdem.config(state=DISABLED)
        aban.config(state=NORMAL)
        new()
            
        dessineGrille(m)
        Creecarré(g)
        couleur(nb)
        Message(m)
    
def B():
    global game
    
    if game== True:
        g_verif= deepcopy(g)
        bas(g)
        additionn_bas(g)
        bas(g)
            
        if g_verif!= g:
            ran= base[randrange(0,2)]
            ajoutAlea(g,ran)
            compteur()
            
        dessineGrille(m)
        Creecarré(g)
        couleur(nb)
        Message(m)

    if game== False:
        game= True
        bdem.config(state=DISABLED)
        aban.config(state=NORMAL)
        new()
            
        dessineGrille(m)
        Creecarré(g)
        couleur(nb)
        Message(m)
    
#############################################################

########### Bouton pour commencer une nouvelle partie ###########
def new():
    global g, game, continuer, cpt
    cpt=0
    game= True #Autoriser les mouvements
    continuer= None #Continuer apres la fin
    ## Nettoyer le widget message ##
    bdem.config(state=DISABLED)
    aban.config(state=NORMAL)
    m.config(state=NORMAL)
    m.delete("0.0", END)
    m.insert(END, " Utilisez les boutons ou les\n fleches du clavier pour jouer.")
    m.config(state=DISABLED)

    ## faire une nouvelle grille ##
    g= init(n)
    dessineGrille(g)
    Creecarré(g)
    couleur(nb)

def abandon():
    global game
    game= False
    bdem.config(state=NORMAL)
    aban.config(state=DISABLED)
    
            
##################################### Les widgets TK #####################################
    
dessin=Tk()
dessin.title("Jeu de 2048. Par: Sami Zaizafoun et Antoine Mader")
Label(dessin,text="Jeu de 2048",font=("Ubuntu",20,"bold")).pack()


can= Canvas(dessin,height=n*91,width=n*91,bg="#9e948a")
can.pack(side=LEFT)


########### Boutons pour lancer ou fermer le jeu ###########

bdem=Button(dessin,text="Nouvelle partie",command=new,font=("Ubuntu",20,"bold"))
bdem.pack(side=TOP)

aban=Button(dessin,text="Abandon",command=abandon,font=("Ubuntu",20,"bold"))
aban.pack(side=TOP)

bq=Button(dessin,text="Quitter",command=monquitter,font=("Ubuntu",20,"bold"))
bq.pack(side=BOTTOM)

##############################################################

cadre= Frame(dessin, bd=10)
cadre.pack(fill=BOTH, expand=YES)

Label(cadre,text=" ",font=("Ubuntu",20,"bold"), width=3).grid(row=0, column=0)

###################### Affichage des boutons ########### ###########

BH=Button(cadre, command=H, text='H',font=("Ubuntu",20,"bold")).grid(row=1, column=2)
BG=Button(cadre, command=G, text='G',font=("Ubuntu",20,"bold")).grid(row=2, column=1)
Button(cadre, text='   ',font=("Ubuntu",20,"bold")).grid(row=2, column=2)
BD=Button(cadre, command=D, text='D',font=("Ubuntu",20,"bold")).grid(row=2, column=3)
BB=Button(cadre, command=B, text='B',font=("Ubuntu",20,"bold")).grid(row=3, column=2)

##################################################################


###################### Creation du cadre du message ######################

cadreT=Frame(dessin, pady=50, width=160)
cadreT.pack(side=BOTTOM)

m= Text(cadreT, height=2, width=26,font=("Minion Pro Med",15))
m.pack(side=BOTTOM)

##########################################################################

###################### Appel au widget de boutons ######################
dessin.bind("<Key>", clavier)


#######################################################################

dessin.mainloop()
