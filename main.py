from Python_PRETRAZIVAC.Funkcionalnosti.parser import Parser
from Python_PRETRAZIVAC.Funkcionalnosti.parserUpita import *
from Python_PRETRAZIVAC.StrukturePodataka.graf import *
import time
from Python_PRETRAZIVAC.Funkcionalnosti.rangiranje import *
from Python_PRETRAZIVAC.Funkcionalnosti.sortiranje import *
from Python_PRETRAZIVAC.Funkcionalnosti.paginacija import *
def menu():
    print("---------------------")
    print("\tSadrzaj: ")
    print("1. Promenite direktorijum ")
    print("2. Unesite upit za pretragu ")
    print("0. Izlaz")
    print("---------------------")
    unos = input("Izaberite opciju : ")
    return unos


def unosenjeRangaCvorova(g) :
    for link in g.getLinkove():
        #inicijalizovani su na 1/ukupan_br_linkova
        g.cvorovi[link].setRang(1/ len(g.getLinkove()))
    for i in range(100) :
        for link in g.getLinkove() :
           for ulazniLink in g.getUlazneLinkove(link) :
                g.cvorovi[link].updateRang(g.cvorovi[ulazniLink].getRang()/len(g.cvorovi[ulazniLink].getIzlazniLinkovi()))

def direktorijum(parser1,trie,g):
    print("Trenutni direktorijum je: " + os.getcwd())
    print("Unesite direktorijum koji zelite da parsirate: ")
    dir = input()

    while (not os.path.isdir(dir)):
        print("Ne postoji uneti direktorijum,unesite novi:")
        dir = input()

    if not os.path.isabs(dir):
        dir = os.path.abspath(dir)
    pocetak = time.time()
    for dirpath, dirnames, files in os.walk(str(dir)):
        for fn in files:
            if fn.endswith('.html') or fn.endswith('.htm'):
                absPath = os.path.join(dirpath, fn)
                parsed = parser1.parse(absPath)
                g.dodavanjeNoveStranice(absPath, parsed[0])
                for word in parser1.words:
                    trie.insert(word, absPath)
    # ovde je graf popunjen i prelazi se na formiranje rangova
    unosenjeRangaCvorova(g)

    kraj = time.time()
    print(kraj - pocetak)

if __name__ == "__main__":
    parser = Parser()
    trie = Trie()
    g = Graph()
    direktorijum(parser,trie,g)
    unos = -1
    while unos != 0:
        unos = menu()
        if unos == "1":
            parser1 = Parser()
            trie = Trie()
            g = Graph()
            direktorijum(parser1,trie,g)
        elif unos == "2":
            s = ParsirajUpit(trie)
            r = rjecnikZaRang(trie, s[1], s[0])
            rjecnikZaRangiranje = r[0]
            recnikZbirSvihReciNaLinkuPom = {}
            recnikZbirSvihReciNaLinku = {}
            for link in rjecnikZaRangiranje.keys():
                recnikZbirSvihReciNaLinkuPom[link] = rjecnikZaRangiranje[link]
                recnikZbirSvihReciNaLinku[link] = rjecnikZaRangiranje[link]

            rangRazlicitihReci = {}
            rangRazlicitihReci = uticajRazlicitihReci(r[1])

            rangUkupnoReci = {}
            rangUkupnoReci = uticajBrojaReci(rjecnikZaRangiranje)

            rangSnagaLinkova = {}
            rangSnagaLinkova = uticajVrednostiLinkova(g, rjecnikZaRangiranje.keys(), recnikZbirSvihReciNaLinkuPom)

            rangBrojLinkova = {}
            rangBrojLinkova = uticajBrojaLinkova(g, rjecnikZaRangiranje)

            RANG = {}
            RANG = formiranjeRanga(rangRazlicitihReci, rangUkupnoReci, rangSnagaLinkova, rangBrojLinkova)

            if len(rjecnikZaRangiranje) != 0:
                listaZaSortiranje = []
                for strana in rjecnikZaRangiranje.keys():
                    listaZaSortiranje.append(PageRang(strana, RANG[strana]))
                recnikRangova = {}
                #lista rangova

                # SORTIRANJE
                heap_sort(listaZaSortiranje)
                for pageRang in listaZaSortiranje:
                    recnikRangova[pageRang.link]=[]
                    recnikRangova[pageRang.link].append(RANG[pageRang.link])
                    recnikRangova[pageRang.link].append(recnikZbirSvihReciNaLinku[pageRang.link])
                    recnikRangova[pageRang.link].append(rangRazlicitihReci[pageRang.link])
                    recnikRangova[pageRang.link].append(rangUkupnoReci[pageRang.link])
                    recnikRangova[pageRang.link].append(rangSnagaLinkova[pageRang.link])
                    recnikRangova[pageRang.link].append(rangBrojLinkova[pageRang.link])
                # PAGINACIJA
                paginacija(recnikRangova)
            else:
                print("Nema fajlova koji zadovoljavaju pretragu!")
        elif unos == "0":
            break