
from StrukturePodataka.strukturaStabla import *
from StrukturePodataka.set import *
from StrukturePodataka.graf import *

def parsirajUpit(stablo):
    upit = input("Unesite upit za pretragu:")
    delovi = upit.split()
    rezultatPretrage = [None]*len(delovi)

    if validacijaUpita(delovi,upit) == -1:
        return -1

    pocetniSetovi(delovi,stablo,rezultatPretrage)
    s = Set()
    return finalniSet(rezultatPretrage,s),delovi



def validacijaUpita(delovi,upit):

    if len(delovi) > 3:
        for rec in delovi:

             if rec.lower() in ("or","not","and"):
                print("Neispravan upit! Ukoliko upit sadrzi logicki operator,on mora biti u formatu rec1 operator rec2")
                parsirajUpit(stablo)
    elif upit == "":
        parsirajUpit(stablo)
    elif delovi[0].lower() in ("or","not","and"):
        print("Neispravan upit! Ukoliko upit sadrzi logicki operator,on mora biti u formatu rec1 operator rec2")
        parsirajUpit(stablo)
    elif delovi[-1].lower() in ("or", "not", "and"):
        print("Neispravan upit! Ukoliko upit sadrzi logicki operator,on mora biti u formatu rec1 operator rec2")
        parsirajUpit(stablo)

def pocetniSetovi(delovi,stablo,rezultatPretrage):
    i = 0
    for rec in delovi:
        if rec.lower() in ("or","not","and"):
            rezultatPretrage[i] = rec.lower()
            i = i + 1
        else:
            if stablo.nadjiRec(rec) != False:
                rezultatPretrage[i] = stablo.nadjiRec(rec)[2].prebaciUSet()
                i = i + 1
            else:
                rezultatPretrage[i] = Set()
                i = i + 1

def finalniSet(rezultatPretrage,s):
    i = 0
    if len(rezultatPretrage) == 3:
        s = s.unijaRecnika(rezultatPretrage[0])
        if rezultatPretrage[1] == "and":
            s = s.presekRecnika(rezultatPretrage[2])
        elif rezultatPretrage[1] == "not":
            s = s.komplementRecnika(rezultatPretrage[2])
        elif rezultatPretrage[1] == "or":
            s = s.unijaRecnika(rezultatPretrage[2])
        else:
            s = s.unijaRecnika(rezultatPretrage[1])
            s = s.unijaRecnika(rezultatPretrage[2])
    else:
        while i < len(rezultatPretrage):
            s = s.unijaRecnika(rezultatPretrage[i])
            i = i + 1
    return s
