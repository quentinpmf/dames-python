from math import *
from numpy import *
from random import *
from copy import * 
from tkinter import * 

# case blanche : 0
# case noire vide : 1
# case noire avec pion noir : 2
# case noire avec pion blanc : -2
 
##matrice test pour essayer les programmes : 

def matrice_test():
    return [[0,2,0,1,0,1,0,1,0,1],[1,0,-2,0,1,0,1,0,1,0],[0,1,0,1,0,-2,0,1,0,1],[1,0,1,0,1,0,2,0,1,0],[0,1,0,1,0,-2,0,1,0,1],[1,0,1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1,0,1],[1,0,2,0,1,0,1,0,1,0],[0,1,0,-2,0,1,0,1,0,1],[1,0,2,0,1,0,1,0,1,0]]
## création du plateau avec les pions
def damier():
    Damier=zeros((10,10))
    for i in range(10):
        for j in range(10):
            if i%2!=j%2:
                Damier[i][j]=1
    return Damier
    
def pions():
    Damier=damier().tolist()
    for i in range(0,4):
        for j in range(10):
            if Damier[i][j]==1:
                Damier[i][j]=Damier[i][j]+1
    for i in range (6,10):
        for j in range(10):
            if Damier[i][j]==1:
                Damier[i][j]=Damier[i][j]-3
    return array(Damier)

##vérifications nécessaires au déplacement d'un pion 
def liste_des_pions(k):         #définir de quel pion on veut dresser la liste des possibilités
    Damier=pions().tolist()     #matrice_test() pour essayer
    liste_pions=[]
    for i in range(10):
        for j in range(10):
            if Damier[i][j]==k:
                liste_pions=liste_pions+[[i,j]]
    return liste_pions

def liste_possibilites(k,test,c):
    L=liste_des_pions(k) 
    n=len(L)
    P1=[]   #liste des pions qu'on peut déplacer
    P=pions().tollist()
    if test==2 or test==-2:    #il faut distinguer les bornes externes (1 si test=1, 2 si test=2ou-2)
        a=1
        b=8
    else :      
        a=0
        b=9    
    for u in range(n):
        i=L[u][0]       #coordonnées des éléments de la liste des pions présents sur le plateau 
        j=L[u][1]
        if a<i<b and  a<j<b:    #on regarde le milieu du plateau
            H=[P[i-c][j-c],P[i-c][j+c],P[i+c][j-c],P[i+c][j+c]]
            if H[0]==test or H[1]==test or H[2]==test or H[3]==test : 
                P1=P1+[[i,j]]
#on regarde maintenant les bords du plateau (pour manger, il faut regarder les deux bandes externes)
        elif 0<=j<=a:  
            if 0<=i<=a:
                if P[i+c][j+c]==test:  
                    P1=P1+[[i,j]]
            elif a<i<b:
                if P[i+c][j+c]==test or P[i-c][j+c]==test:
                    P1=P1+[[i,j]]
            elif b<=i<=9:
                if P[i-c][j+c]==test:
                    P1=P1+[[i,j]]
        elif a<j<b:
            if 0<=i<=a:
                if P[i+c][j+c]==test or P[i+c][j-c]==test:
                    P1=P1+[[i,j]]
            elif b<=i<=9:
                if P[i-c][j+c]==test or P[i-c][j-c]==test :  
                    P1=P1+[[i,j]]
        elif b<=j<=9:
            if 0<=i<=a:
                if P[i+c][j-c]==test:  #première ligne et dernière colonne
                    P1=P1+[[i,j]]
            elif b<=i<=9:
                if P[i-c][j-c]==test:  #dernière ligne et dernière colonne
                    P1=P1+[[i,j]]
            elif a<i<b:
                if P[i-c][j-c]==test or P[i+c][j-c]==test:
                    P1=P1+[[i,j]]
    return P1
    
def verif_manger(k,test): #ne marche pas 
    poss=liste_possibilites(k,test,1)
    n=len(poss)
    N=matrice_test()
    P2=[]
    #on regarde pour chaque pion qui peut peut-être manger si il y a une case libre après la cible
    for r in range(n): 
        i=poss[r][0]     #coordonnées des pions qui peuvent peut-être manger  
        j=poss[r][1]
        sous_liste_coord=[]
    # on regarde les diagonales formée par pion attaque-pion cible pour savoir si on peut déplacer
        if 1<i<8 and 1<j<8:
            if N[i-1][j-1]==test and N[i-2][j-2]==1: 
                sous_liste_coord=sous_liste_coord+[i-2,j-2]
            elif N[i-1][j+1]==test and N[i-2][j+2]==1:
                sous_liste_coord=sous_liste_coord+[i-2,j+2]
            elif N[i+1][j-1]==test and N[i+2][j-2]==1:
                sous_liste_coord=sous_liste_coord+[i+2,j-2]
            elif N[i+1][j+1]==test and N[i+2][j+2]==1:
                sous_liste_coord=sous_liste_coord+[i+2,j+2]
        elif 0<=i<=1 and 0<=j<=1:
            if N[i+1][j+1]==test and N[i+2][j+2]==1:
                sous_liste_coord=sous_liste_coord+[i+2,j+2]
        elif 8<=i<=9 and 0<=j<=1:
            if N[i-1][j+1]==test and N[i-2][j+2]==1:
                sous_liste_coord=sous_liste_coord+[i-2,j+2]
        elif 1<i<8 and 0<=j<=1:
            if N[i+1][j+1]==test and N[i+2][j+2]==1:
                sous_liste_coord=sous_liste_coord+[i+2,j+2]
            elif N[i-1][j+1]==test and N[i-2][j+2]==1:
                sous_liste_coord=sous_liste_coord+[i-2,j+2]
        elif 8<=i<=9 and 1<j<8:
            if N[i-1][j-1]==test and N[i-2][j-2]==1:
                sous_liste_coord=sous_liste_coord+[i-2,j-2]
            elif N[i-1][j+1]==test and N[i-2][j+2]==1:
                sous_liste_coord=sous_liste_coord+[i-2,j+2]
        elif 8<=i<=9 and 8<=j<=9:
            if N[i-1][j-1]==test and N[i-2][j-2]==1:
                sous_liste_coord=sous_liste_coord+[i-2,j-2]
        elif 1<i<8 and 8<=j<=9:
            if N[i-1][j-1]==test and N[i-2][j-2]==1:
                sous_liste_coord=sous_liste_coord+[i-2,j-2]
            elif N[i+1][j-1]==test and N[i+2][j-2]==1:
                sous_liste_coord=sous_liste_coord+[i+2,j-2]
        elif 0<=i<=1 and 8<=j<=9:
            if N[i+1][j-1]==test and N[i+2][j-2]==1:
                sous_liste_coord=sous_liste_coord+[i+2,j-2]
        elif 0<=i<=1 and 1<j<8 :
            if N[i+1][j-1]==test and N[i+2][j-2]==1:
                sous_liste_coord=sous_liste_coord+[i+2,j-2]
            elif N[i+1][j+1]==test and N[i+2][j+2]==1:
                sous_liste_coord=sous_liste_coord+[i+2,j+2]
        P2=P2+[sous_liste_coord] #on obtient une liste de listes de coordonnées 
    return P2
   
##déplacement du pion    
def deplacer_pion(plateau,i1,j1,i2,j2):
    temporaire_arrivee =plateau[i2][j2];
    plateau[i2][j2] = plateau[i1][j1];
    plateau[i1][j1] = temporaire_arrivee;
    return plateau
    
def jouer():
    plateau=pions()
    print (pions())
    while liste_des_pions(2)!=[]:       #tant que on a encore des pions à bouger 
        i_depart = int(input("coordonnées i départ : "))
        j_depart = int(input("coordonnées j départ : "))
        i_arrivee = int(input("coordonnées i arrivée : "))
        j_arrivee = int(input("coordonnées j arrivée : "))                                                                                                                                                                      
        if j_arrivee == j_depart+1 or j_arrivee == j_depart-1 and i_arrivee == i_depart+1 :
            if plateau[i_arrivee][j_arrivee]==1:
                test = deplacer_pion(plateau,i_depart,j_depart,i_arrivee,j_arrivee)
                print(test)
            else : print("choisir d'autres coordonnées")
        else : print("choisir d'autres coordonnées")
    return plateau     

def déplacement_ordi():
    déplacement_manger_i_depart=random.choice(liste_possibilites(-2,2))[0]
    déplacement_normal_j_depart=random.choice(liste_possibilites(-2,2))[1]
