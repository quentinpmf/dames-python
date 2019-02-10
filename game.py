from math import *
from numpy import *
from random import *
from copy import * 
from tkinter import * 

# case blanche : 0
# case noire vide : 1
# case noire avec pion noir : 2
# case noire avec pion blanc : -2
    
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


def parcours_du_plateau(k):         #définir de quel pion on veut dresser la liste des possibilités
    Damier=pions().tolist()
    liste_possibilites=[]
    for i in range(10):
        for j in range(10):
            if Damier[i][j]==k:
                liste_possibilites=liste_possibilites+[[i,j]]
    return liste_possibilites



def tri_bords(k):   # il faut enlever les éléments qui font partie des bords du plateau
    P=parcours_du_plateau(k)
    n=len(P)
    P1=[]
    for i in range(n):
        if P[i][0]!=0 and P[i][0]!=9 and P[i][1]!=0 and P[i][1]!=9:
            P1=P1+[P[i]]
    return P1

def liste_possibilites(k):
    L=tri_bords(k)
    n=len(L)
    M=[]
    P=pions().tolist()
    for u in range(n):
        i=L[u][0]       #coordonnées des éléments de la liste des possibilités 
        j=L[u][1]
        H=[P[i-1][j-1],P[i-1][j+1],P[i+1][j-1],P[i+1][j+1]]
        for g in range(4):
            if H[g]==k:
                M=M+[H[g]]
        return M

def verification_pion_existant(i,j):
    couple=[i,j]
    n=len(parcours_du_plateau(k))
    for u in range(n):
        if parcours_du_plateau(k)[u]==couple:
            return couple
    return "choisir d'autres coordonnées"
    
def deplacer_pion(plateau,i1,j1,i2,j2):
    temporaire_arrivee =plateau[i2][j2];
    plateau[i2][j2] = plateau[i1][j1];
    plateau[i1][j1] = temporaire_arrivee;
    return plateau

def jouer():
    plateau=pions()
    i = 1
    while i < 5:
        i_depart = int(input("coordonnées i départ : "))
        j_depart = int(input("coordonnées j départ : "))
        i2_depart = int(input("coordonnées i arrivée : "))
        j2_depart = int(input("coordonnées i arrivée : "))
        test = deplacer_pion(plateau,i_depart,j_depart,i2_depart,j2_depart)
        print(test);
        i += 1
    return plateau    
