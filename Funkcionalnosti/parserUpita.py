from Python_PRETRAZIVAC.StrukturePodataka.trieStruct import *
from Python_PRETRAZIVAC.StrukturePodataka.set import *
from Python_PRETRAZIVAC.StrukturePodataka.graf import *



def ParsirajUpit(trie):
    upit = input("Unesite upit za pretragu:")
    delovi = upit.split()
    rezultatPretrage = [None]*len(delovi)

    if len(delovi) == 0:
        ParsirajUpit(trie)
    elif len(delovi) > 3:
        for rec in delovi:
             if rec.lower() in ("and", "or", "not"):
                print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu rec1 operator rec2")
                ParsirajUpit(trie)
    else:
        if delovi[0].lower() in ("and", "or", "not") or delovi[-1].lower() in ("and", "or", "not"):
            print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu rec1 operator rec2")
            ParsirajUpit(trie)

    i = 0
    #trazenaLista = Set()
    for rec in delovi:
        if rec.lower() in ("and", "or", "not"):
            rezultatPretrage[i] = rec.lower()
            i = i + 1
        else:
            if not trie.search(rec):
                rezultatPretrage[i] = Set()
                i = i + 1
            else:
                rezultatPretrage[i] = trie.search(rec)[2].IntoSet()
                i = i + 1


    s = Set()
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
    return s, delovi # delovi su sve reci koje se unesu sa logickim operatorima