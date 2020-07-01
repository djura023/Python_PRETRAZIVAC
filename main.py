from StrukturePodataka.trieStruct import *
from StrukturePodataka.set import Set
from StrukturePodataka.ispis import *
from Funkcionalnosti.parser import Parser
from Funkcionalnosti.parserUpita import *
from StrukturePodataka.graf import *
import time
import os
from Funkcionalnosti.rangiranje import *
from Funkcionalnosti.sortiranje import *
from Funkcionalnosti.paginacija import *
def menu():
    print("---------------------")
    print("\tSadrzaj: ")
    print("1. Promenite direktorijum ")
    print("2. Unesite upit za pretragu ")
    print("0. Izlaz")
    print("---------------------")
    unos = input("Izaberite opciju : ")
    return unos

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
            s = ParsirajUpit(trie)  # s vraca trazenu listu i niz rijeci iz upita (s,exists)
            # 1
            r = rjecnikZaRang(trie, s[1], s[0])
            # r[0] zbir svih pojavljivanja r[1] pojavljivanje razlicitih reci
            rjecnikZaRangiranje = r[0]  # link i ukupan br pojavljiavanja reci na njemu
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

                # SORTIRANJE
                heap_sort(listaZaSortiranje)

                # PAGINACIJA
                paginacija(listaZaSortiranje, recnikZbirSvihReciNaLinku, rangRazlicitihReci, rangUkupnoReci,
                           rangSnagaLinkova, rangBrojLinkova)


            else:
                print("Nema fajlova koji zadovoljavaju pretragu!")



        elif unos == "0":
            break