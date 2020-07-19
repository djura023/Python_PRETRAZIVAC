
from StrukturePodataka.strukturaStabla import *
from StrukturePodataka.set import Set
from Funkcionalnosti.parser import Parser
from Funkcionalnosti.parserUpita import *
from StrukturePodataka.graf import *
from StrukturePodataka.rang import *
import time
from Funkcionalnosti.rangiranje import *
from Funkcionalnosti.sortiranje import *
from Funkcionalnosti.paginacija import *
def menu():
    print("---------------------")
    print("\t\tSadrzaj: ")
    print("0. Novi direktorijum ")
    print("1. Unesite upit za pretragu ")
    print("2. Kraj programa")
    print("---------------------")
    unos = input("Izaberite : ")
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
    print("Nalazite se u direktorijumu : " + os.getcwd())
    print("Unesite direktorijum za parsiranje: ")
    dir = input()

    proveraDirektorijuma(dir)
    dir = dodajAbsolutnuPutanju(dir)

    pocetak = time.time()
    popuniGrafIStablo(dir,parser,stablo,graf)
    unosenjeRangaCvorova(graf)
    kraj = time.time()
    print(kraj - pocetak)

def proveraDirektorijuma(dir):
    while (not os.path.isdir(dir)):
        print("Ne postoji uneti direktorijum,unesite drugi:")
        dir = input()

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
            recnikR = rjecnikZaRang(stablo, s[1], s[0],graf)

            if len(recnikR) != 0:
                sortiraj = []
                for strana in recnikR.keys():
                    sortiraj.append(PageRang(strana, recnikR[strana].getRang()))
                recnikRangova = {}
                #lista rangova
                zaPaginaciju =[]
                # SORTIRANJE
                heap_sort(sortiraj)
                for pageRang in sortiraj:
                    recnikRangova[pageRang.link]=recnikR[pageRang.link]
                # PAGINACIJA
                paginacija(recnikRangova)
            else:
                print("Nema fajlova za uneti upit!")
        elif unos == "2":
            break