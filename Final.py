#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 03:10:16 2019

@author: elisabethgoossens
"""

### Index :
# A. Listes initiales                     L.23
# B.1 Tableau de connexion                L.63
# B.2 Retour du tableau de connexion      L.98
# C. Passage dans les rotors              L.114
# D. Alphabet final                       L.126
# E. Et on fait tourner les rotors        L.149
# F. Choix des Rotors et du Réflecteur    L.160
# G. Positions des rotors                 L.197
# H. Fonctions finales                    L.223
# I. Commande                             L.268



### A. Listes initiales

Alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

enter=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

enterbis=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

#Les listes suivantes sont les opérations affectuées lorsqu'on passe dans le rotor ou reflecteur correspondant
#Les listes Reflector sont les réflecteurs
#les listes Rotor sont le passage aller dans un rotor
#Les listes Retor sont le passage retour dans un rotor

ReflectorB=[24,16,18,4,12,13,5,-4,7,14,3,-5,2,-3,-2,-7,-12,-16,-13,6,-18,1,-1,-14,-24,-6]

ReflectorC=[5,20,13,6,4,-5,8,17,-4,-6,7,14,11,9,-8,-13,3,-7,2,-3,-2,-20,-9,-11,-17,-14]

RotorV=[16,1,22,8,19,17,-2,6,-3,10,15,3,6,-1,7,-6,4,-14,-8,-13,-12,-21,-5,-8,-17,-24]

RotorIV=[7,24,20,18,-4,12,13,6,3,-3,10,4,11,3,-12,-11,-7,-5,-17,-1,-10,-18,2,-9,-16,-20]

RotorIII=[1,2,3,4,5,6,-4,8,9,10,13,10,13,0,10,-11,-8,5,-12,-19,-10,-9,-2,-5,-8,-11]

RotorII=[0,8,1,7,14,3,11,13,15,-8,1,-4,10,6,-2,-13,0,-11,7,-6,-5,3,-17,-2,-10,-21]

RotorI=[4,9,10,2,7,1,-3,9,13,16,3,8,2,9,10,-8,7,3,0,-4,-20,-13,-21,-6,-22,-16]

RetorI=[20,21,22,3,-4,-2,-1,8,13,16,-9,-7,-10,-3,-2,4,-9,6,0,-8,-3,-13,-9,-7,-10,-16]

RetorII=[0,8,13,-1,21,17,11,4,-3,-8,-7,-1,2,6,10,5,0,-11,-14,-6,-13,2,-10,-15,-3,-7]

RetorIII=[19,-1,4,-2,11,-3,12,-4,8,-5,10,-6,9,0,11,-8,8,-9,5,-10,2,-10,-5,-13,-10,-13]

RetorIV=[4,17,12,18,11,20,3,-7,16,7,10,-3,5,-6,9,-4,-3,-12,1,-13,-10,-18,-20,-11,-2,-24]

RetorV=[21,24,-1,14,2,3,13,17,12,6,8,-8,1,-6,-3,8,-16,5,-6,-10,-4,-7,-17,-19,-22,-15]




### B.1 Tableau de connexion

#Cette fonction permet d'échanger deux valeurs d'une liste
def echange(c,d):
    a=enter[c]
    enter[c]=enter[d]
    enter[d] = a

#On demande ici les lettres à échanger :
a,b=str(input("Brchmt 1, entrer la première lettre qui sera câblée: ")),str(input("entrer la seconde qui sera cablée: "))

c,d=str(input("Brchmt 2, entrer la première lettre qui sera câblée: ")),str(input("entrer la seconde qui sera câblée: "))

e,f=str(input("Brchmt 3, entrer la première lettre qui sera câblée: ")),str(input("entrer la seconde qui sera câblée: "))

g,h=str(input("Brchmt 4, entrer la première lettre qui sera câblée: ")),str(input("entrer la seconde qui sera câblée: "))

i,j=str(input("Brchmt 5, entrer la première lettre qui sera câblée: ")),str(input("entrer la seconde qui sera câblée: "))

#Puis on éffectue les échanges:
k,l=int(Alpha.index(a)),int(Alpha.index(b))
m,n=int(Alpha.index(c)),int(Alpha.index(d))
o,p=int(Alpha.index(e)),int(Alpha.index(f))
q,r=int(Alpha.index(g)),int(Alpha.index(h))
s,t=int(Alpha.index(i)),int(Alpha.index(j))

echange(k,l)
echange(m,n)
echange(o,p)
echange(q,r)
echange(s,t)




### B.2 Retour du tableau de connexion

enter1=[]

#Cette fonction permet d'obtenir la liste correspondant aux opérations effectuées lors du passage retour dans le tableau de connexion
def Cabret(enter1):
    for k in range(0,26):
        a=-(enterbis[k]-enter[k])
        enter1.append(a)
    return(enter1)

Cabret(enter1)




### C. Passage dans les rotors

#Cette fonction donne la sortie de l'alphabet lorsqu'il passe dans un rotor
#Le res est l'alphabet codé par le rotor
def Rotor(rotor,res):
    for k in range(0,26):
        a=(k+rotor[k])%26
        res.append(a)




### D. Alphabet final

#Cette fonction calcule le numéro j après codage d'une lettre donnée
def Let(lettre,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9):
    a=Alpha.index(lettre)
    b=enter[a]
    c=enter2[b]
    d=enter3[c]
    e=enter4[d]
    f=enter5[e]
    g=enter6[f]
    h=enter7[g]
    i=enter8[h]
    j=enter9[i]
    return(j)
    
#Cette fonction donne la lettrede l'alphabet codée par un numéro a donné
def Msgcode(a):
    return(Alpha[a])




### E. Et on fait tourner les rotors

#Cette fonction permet de faire tourner un rotor d'un cran
def Transform(rotor):
    rotor.append(rotor[0])
    rotor.remove(rotor[0])
    return rotor




### F. Choix des Rotors et du Réflecteur

#On demande ici les rotors et le reflecteur à utiliser :
k=input("entrer le premier rotor : ")
l=input("entrer le deuxième rotor : ")
m=input("entrer les troisième rotor : ")
n=input("entrer le reflecteur utilisé : ")

#Cette fonction permet de déterminer les rotors choisis par l'utilisateur
def Rotorchoisi(num):
    if int(num)==1:
        return(RotorI,RetorI)
    elif int(num)==2:
        return(RotorII,RetorII)
    elif int(num)==3:
        return(RotorIII,RetorIII)
    elif int(num)==4:
        return(RotorIV,RetorIV)   
    else :
        return(RotorV,RetorV)
        
#Cette fonction permet de déterminer le réflecteur choisi par l'utiisateur
def Reflecteurchoisi(num):
    if str(num)==b:
        return(ReflectorB)
    else :
        return(ReflectorC)

#On renomme les rotors pour les utiliser dans l'orde choisi par l'utilisateur
Rotor1,Retor1=Rotorchoisi(k)
Rotor2,Retor2=Rotorchoisi(l)
Rotor3,Retor3=Rotorchoisi(m)
Reflecteur=Reflecteurchoisi(n)




### G. Positions des rotors

#Cette fonction utilise la fonction Transform précédente afin de faire tourner le Rotor jusqu'à la position choisie par l'utilisateur
def Position(position,Rotor):
    if int(position)==0:
        print()
    else :
        for k in range(int(position)):
            Transform(Rotor)

#On demande ici la position des rotors :
x=input("Entrer la position du premier rotor : ")
y=input("Entrer la position du deuxième rotor : ")
z=input("Entrer la position du troisième rotor : ")

#On effectue les deplacements de rotors
Position(x,Rotor1)
Position(x,Retor1)
Position(y,Rotor2)
Position(y,Retor2)
Position(z,Rotor3)
Position(z,Retor3)




### H. Fonctions finales

#Cette fonction permet de coder une seul lettre donnée en fonction des Rotors et du Réflecteur choisis
def Codage(lettre,Rotor1,Rotor2,Rotor3,Reflector,Retor1,Retor2,Retor3):
    enter2=[]
    enter3=[]
    enter4=[]
    enter5=[]
    enter6=[]
    enter7=[]
    enter8=[]
    enter9=[]
    Rotor(Rotor1,enter2)
    Rotor(Rotor2,enter3)
    Rotor(Rotor3,enter4)
    Rotor(Reflector,enter5)
    Rotor(Retor3,enter6)
    Rotor(Retor2,enter7)
    Rotor(Retor1,enter8)
    Rotor(enter1,enter9)
    p=Let(str(lettre),enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9)
    k=Msgcode(p)
    return(k)

#Cette fonction code une phrase donnée en fonction des Rotors et du Réflecteur choisis
def Cod(trad,Rotor1,Rotor2,Rotor3,Reflector,Retor1,Retor2,Retor3):
    result=''
    compt=0
    for k in range(1,len(trad)+1):
        o=Codage(trad[k-1],Rotor1,Rotor2,Rotor3,Reflector,Retor1,Retor2,Retor3)
        Transform(Rotor1)
        Transform(Retor1)
        compt=compt+1
        if compt%26==0:
            Transform(Rotor2)
            Transform(Retor2)
            if compt%676==0:
                Transform(Rotor3)
                Transform(Retor3)
        result=result+str(o)
    print('le codage obtenu est : ',result)




### I. Commande

#On demande ici la lettre à coder
phrase=str(input("rentrer la phrase à coder sans espace :"))

#On effectue le codage finale !!!!
Cod(phrase,Rotor1,Rotor2,Rotor3,Reflecteur,Retor1,Retor2,Retor3)

