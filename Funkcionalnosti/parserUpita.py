from StrukturePodataka.strukturaStabla import *
from StrukturePodataka.set import *
from StrukturePodataka.graf import *

def parsirajUpit(stablo):
    upit = input("Unesite upit za pretragu:")
    delovi = upit.split()
    rezultatPretrage = [None]*len(delovi)

    validacijaUpita(delovi,stablo)
    pocetniSetovi(delovi,stablo,rezultatPretrage)
    s = Set()
    return finalniSet(rezultatPretrage,s),delovi



def validacijaUpita(delovi,stablo):
    if len(delovi) == 0:
        parsirajUpit(stablo)
    elif len(delovi) > 3:
        for rec in delovi:
             if rec.lower() in ("and", "or", "not"):
                print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu rec1 operator rec2")
                parsirajUpit(stablo)
    else:
        if delovi[0].lower() in ("and", "or", "not") or delovi[-1].lower() in ("and", "or", "not"):
            print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu rec1 operator rec2")
            parsirajUpit(stablo)

def pocetniSetovi(delovi,stablo,rezultatPretrage):
    i = 0
    for rec in delovi:
        if rec.lower() in ("and", "or", "not"):
            rezultatPretrage[i] = rec.lower()
            i = i + 1
        else:
            if not stablo.nadjiRec(rec):
                rezultatPretrage[i] = Set()
                i = i + 1
            else:
                rezultatPretrage[i] = stablo.nadjiRec(rec)[2].prebaciUSet()
                i = i + 1

def finalniSet(rezultatPretrage,s):
    i = 0
    while i < len(rezultatPretrage):
        if rezultatPretrage[i] == "and":
            s = s.presekRecnika(rezultatPretrage[i + 1])
            i = i + 2
        elif rezultatPretrage[i] == "not":
            s = s.komplementRecnika(rezultatPretrage[i + 1])
            i = i + 2
        elif rezultatPretrage[i] == "or":
            s = s.unijaRecnika(rezultatPretrage[i + 1])
            i = i + 2
        else:
            s = s.unijaRecnika(rezultatPretrage[i])
            i = i + 1
    #return s, delovi # delovi su sve reci koje se unesu sa logickim operatorima
    return s
