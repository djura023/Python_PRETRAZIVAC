from Funkcionalnosti.napredniParser import *
from StrukturePodataka.strukturaStabla import *
from StrukturePodataka.set import Set
from Funkcionalnosti.parser import Parser
from Funkcionalnosti.parserUpita import *
from StrukturePodataka.graf import *
from StrukturePodataka.rang import *
from StrukturePodataka.pomocniRang import PomocniRang
import time
from Funkcionalnosti.rangiranje import *
from Funkcionalnosti.sortiranje import *
from Funkcionalnosti.paginacija import *
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

def menu():
    print(30*"-")
    print(Fore.YELLOW +10*' '+ "SADRZAJ :"+ "\033[0m")
    print(Fore.BLUE +5*' '+"0. Novi direktorijum "+ "\033[0m")
    print(Fore.BLUE +5*' '+"1. Unesite upit za pretragu "+ "\033[0m")
    print(Fore.BLUE +5*' '+"2. Unesite upit za naprednu pretragu "+ "\033[0m")
    print(Fore.BLUE +5*' '+"3. Kraj programa"+ "\033[0m")
    print(30*"-")
    unos = input(Fore.BLUE+"Izaberite : "+"\033[0m")
    return unos


def unosenjeRangaCvorova(g) :
    for link in g.getLinkove():
        #inicijalizovani su na 1/ukupan_br_linkova
        g.cvorovi[link].setRang(1/ len(g.getLinkove()))
        #g.cvorovi[link].setRang(1)
    for i in range(16) :
        for link in g.getLinkove() :
           for ulazniLink in g.getUlazneLinkove(link) :
                g.cvorovi[link].updateRang(g.cvorovi[ulazniLink].getRang()/len(g.cvorovi[ulazniLink].getIzlazniLinkovi()))

def direktorijum(parser,stablo,graf):
    print(Fore.BLUE + "\033[1m" + "Nalazite se u direktorijumu : " + Fore.YELLOW  + "\033[1m" + os.getcwd() + "\033[0m"+ "\033[0m")
    print(Fore.BLUE  + "Unesite naziv zeljenog direktorijuma :"+ "\033[0m")
    dir = input()
    dir = dir.strip()
    dir = proveraDirektorijuma(dir)
    dir = dodajAbsolutnuPutanju(dir)

    pocetak = time.time()
    print(Fore.YELLOW + "Parsiranje je u toku..." + "\033[0m")
    popuniGrafIStablo(dir,parser,stablo,graf)
    unosenjeRangaCvorova(graf)
    print(Fore.YELLOW + "Parsiranje uspesno zavrseno!"+"\033[0m")
    kraj = time.time()
    print(kraj- pocetak)

def greska() :
    fr = 2000
    d = 50
    print(Fore.RED + "\033[1m" + "Pogresan unos!" + "\033[0m")
    winsound.Beep(fr,d)

def proveraDirektorijuma(dir):
    while (not os.path.isdir(dir.strip())):
        greska()
        print(Fore.RED  + "\033[1m" + "Ne postoji uneti direktorijum! Unesite ispravan direktorijum :" + "\033[0m")
        dir = input()
    return dir.strip()

def dodajAbsolutnuPutanju(dir):
    if not os.path.isabs(dir):
        dir = os.path.abspath(dir)
    return dir
def popuniGrafIStablo(dir,parser,stablo,graf):
    for dirpath, dirnames, files in os.walk(str(dir)):
        for fn in files:
            if fn.endswith('.html') or fn.endswith('.htm'):
                absPath = os.path.join(dirpath, fn)
                parsed = parser.parse(absPath)
                for word in parser.words:
                    stablo.dodaj(word, absPath)
                graf.dodavanjeNoveStranice(absPath, parsed[0])


if __name__ == "__main__":
    parser = Parser()
    stablo = Stablo()
    graf = Graph()
    direktorijum(parser,stablo,graf)
    unos = -1
    while True:
        unos = menu()
        if unos == "0":
            parser = Parser()
            stablo = Stablo()
            graf = Graph()
            direktorijum(parser,stablo,graf)
        elif unos == "1":

            while True:
                s = parsirajUpit(stablo)
                if s != -1:
                    break
            recnikR = rjecnikZaRang(stablo, s[1], s[0],graf,1)

            if len(recnikR) != 0:
                sortiraj = []
                for strana in recnikR.keys():
                    sortiraj.append(PomocniRang(strana, recnikR[strana].getRang()))
                recnikRangova = {}
                #lista rangova
                zaPaginaciju =[]
                # SORTIRANJE
                merge_sort(sortiraj)
                for pageRang in sortiraj:
                    recnikRangova[pageRang.link]=recnikR[pageRang.link]
                # PAGINACIJA
                paginacija(recnikRangova)
            else:
                print("Nema fajlova za uneti upit!")
        elif unos == "2":
            while True:
                s = napredniParsirajUpit(stablo, graf)
                if s != -1:
                    break
            recnikR = rjecnikZaRang(stablo, s[1], s[0],graf,0)

            if len(recnikR) != 0:
                sortiraj = []
                for strana in recnikR.keys():
                    sortiraj.append(PomocniRang(strana, recnikR[strana].getRang()))
                recnikRangova = {}
                #lista rangova
                zaPaginaciju =[]
                # SORTIRANJE
                merge_sort(sortiraj)
                for pageRang in sortiraj:
                    recnikRangova[pageRang.link]=recnikR[pageRang.link]
                # PAGINACIJA
                paginacija(recnikRangova)
            else:
                print("Nema fajlova za uneti upit!")
        elif unos == "3":
            break