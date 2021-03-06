
from StrukturePodataka.strukturaStabla import *
from StrukturePodataka.set import *
from StrukturePodataka.graf import *
import winsound

class Fore():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def parsirajUpit(stablo):
    upit = input("Unesite upit za pretragu:")
    delovi = upit.split()
    rezultatPretrage = [None]*len(delovi)

    if validacijaUpita(delovi,upit,stablo) == -1:
        return -1

    pocetniSetovi(delovi,stablo,rezultatPretrage)
    s = Set()
    return finalniSet(rezultatPretrage,s),delovi


def greska() :
    fr = 2000
    d = 50
    winsound.Beep(fr,d)
    print(Fore.RED + "\033[1m" + "Pogresan unos!" + "\033[0m")

def validacijaUpita(delovi,upit,stablo):

    if len(delovi) > 3:
        for rec in delovi:

             if rec.lower() in ("or","not","and"):
                greska()
                print(Fore.RED + "\033[1m"+"Unesite upit u formatu :  REC1 OPERATOR REC2"+ "\033[0m")
                return -1
    elif upit == "":
        return -1
    elif delovi[0].lower() in ("or","not","and"):
        greska()
        print(Fore.RED + "\033[1m" + "Unesite upit u formatu :  REC1 OPERATOR REC2" + "\033[0m")
        return -1
    elif delovi[-1].lower() in ("or", "not", "and"):
        greska()
        print(Fore.RED + "\033[1m" + "Unesite upit u formatu :  REC1 OPERATOR REC2" + "\033[0m")
        return -1

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
