import os
import math
import random
from StrukturePodataka.rang import Rang
import operator
class PageRang:
    def __init__(self,link,brojZaRangiranje):
        self.link = link
        self.brojZaRangiranje = brojZaRangiranje

    def getLink(self):
        return self.link

    def getBrojRanga(self):
        return self.brojZaRangiranje

    def setLink(self,noviLink):
        self.link = noviLink

    def setBrojRanga(self,noviBrojZaRangiranje):
        self.brojZaRangiranje = noviBrojZaRangiranje

    def ispisi(self):
        print(self.brojZaRangiranje,self.link)
                    #d = niz reci upita, s = linkovi pretrage

    #pravi dve mapa
    #(1. kljuc je link,vrednost broj pojavljivanja svih trazenkih reci na tom linku)
    #(2. kljuc je link,vrednost broj pojavljivanja razlicitih reci na tom linku)
def rjecnikZaRang(root, nizReciIzUpita, linokviPretrage,graf):
    recnikRangova = {}
    recnikSnageLinkova = {}
    recnikBrojaLinkova = {}
    recnikZaUkupnoPojavljivanjeReciNaLinku = {}
    recnikZaRazliciteReci = {}
    reciZaPrebrojavanje = {}

    # inicijalizovanje recnika
    for link in linokviPretrage.kljucevi():
        recnikZaUkupnoPojavljivanjeReciNaLinku[os.path.abspath(link)] = 0
        recnikZaRazliciteReci[os.path.abspath(link)]=0
        recnikSnageLinkova[os.path.abspath(link)] = 0
        recnikRangova[os.path.abspath(link)] = 0
        recnikBrojaLinkova[os.path.abspath(link)] = 0
    #filtriranje niza (dobijamo niz sa potrebnim recima)
    for rec in nizReciIzUpita:
        if rec.upper() not in ("AND","OR","NOT"):
            reciZaPrebrojavanje[rec] = rec

    # dobijanje cvora za odredjenu rec
    for rec in reciZaPrebrojavanje:
        cvorNaKomSeZavrsavaRec = root.nadjiCvor(rec)[0] # vrednost treba da bude cvor na kom  se zavrsava rijec
        recnikBrojaPonavljanjaJedneReciULink = {}

        # popunjavanje recnika (vrednost = link, kljuc = broj pojavljivanja jedne reci na njemu)

        for pom in cvorNaKomSeZavrsavaRec.linkovi:
            recnikBrojaPonavljanjaJedneReciULink[os.path.abspath(pom)] = cvorNaKomSeZavrsavaRec.linkovi[pom]

        #popunjavanje potrebnih recnika koji se salju dalje
        for link in recnikBrojaPonavljanjaJedneReciULink:
            if link in recnikZaUkupnoPojavljivanjeReciNaLinku.keys():
                #if (len(graf.getUlazneLinkove(os.path.abspath(link))) != 0):
                 #   recnikBrojaLinkova[link] = len(graf.getUlazneLinkove(os.path.abspath(link)))
                recnikZaUkupnoPojavljivanjeReciNaLinku[link] += recnikBrojaPonavljanjaJedneReciULink[link]
                recnikZaRazliciteReci[link]+=1

        # recnik -> kljuc je snaga linkova
        #for odredjeniLink in recnikZaUkupnoPojavljivanjeReciNaLinku :
        #    for linkPokazivac in graf.cvorovi[odredjeniLink].getUlazniLinkovi() :
        #        if linkPokazivac in recnikZaUkupnoPojavljivanjeReciNaLinku :
        #            recnikSnageLinkova[odredjeniLink] += recnikZaUkupnoPojavljivanjeReciNaLinku[linkPokazivac]

        #for link in recnikZaUkupnoPojavljivanjeReciNaLinku :
        #    if (len(graf.getUlazneLinkove(os.path.abspath(link))) != 0):
        #        recnikBrojaLinkova[link] = len(graf.getUlazneLinkove(os.path.abspath(link)))

        #for odredjeniLink in recnikZaUkupnoPojavljivanjeReciNaLinku :
        #    recnikRangova[link] = Rang(recnikZaUkupnoPojavljivanjeReciNaLinku[odredjeniLink],
        #                               recnikZaRazliciteReci[odredjeniLink],graf.cvorovi[odredjeniLink].getRang(),recnikBrojaLinkova[odredjeniLink],
        #                               recnikSnageLinkova[odredjeniLink],recnikZaUkupnoPojavljivanjeReciNaLinku[odredjeniLink],odredjeniLink)


    return recnikZaUkupnoPojavljivanjeReciNaLinku,recnikZaRazliciteReci

def uticajVrednostiLinkova(root, linkoviUpita, rjecnikUpita):
    rang3={}
    broj = 10 * 0.5
    for link1 in linkoviUpita:
        rjecnikUpita[link1] = broj

    for link1 in linkoviUpita:
        link1 = os.path.abspath(link1)
        dodatak = 1
        for link2 in root.getUlazneLinkove(link1):
            if link2 in rjecnikUpita.keys():
                dodatak += rjecnikUpita[link2] #dodatak sadrzi zbir vrednosti svih njegovih linkova
        rjecnikUpita[link1] = broj/dodatak
    for k in linkoviUpita:
        rang3[k] = rjecnikUpita[k]
    return rang3

def  uticajBrojaLinkova(g,rjecnikLinkova):
        rang4 = {}
        broj = 10*0.2
        for link in rjecnikLinkova.keys():
            rjecnikLinkova[link]=1

        for link in rjecnikLinkova.keys():
            if(len(g.getUlazneLinkove(os.path.abspath(link))) !=0) :
                 rjecnikLinkova[link] = len(g.getUlazneLinkove(os.path.abspath(link)))

        for link in rjecnikLinkova.keys():
            rjecnikLinkova[link] = broj/rjecnikLinkova[link]

        for link in rjecnikLinkova.keys():
            rang4[link] = rjecnikLinkova[link]
        return rang4

def uticajRazlicitihReci(mapaRazlicitihReci):
    rang1 = {}
    for link in mapaRazlicitihReci.keys():
        rang1[link] = 10

    for link in mapaRazlicitihReci.keys():
        rang1[link]= math.pow(rang1[link],mapaRazlicitihReci[link])
    return rang1

def uticajBrojaReci(mapaZaRang):
    broj = 10*0.3
    rang2 ={}
    for link in mapaZaRang.keys():
        mapaZaRang[link] = broj/(mapaZaRang[link])
    for link in mapaZaRang.keys():
        rang2[link] = mapaZaRang[link];
    return rang2

def formiranjeRanga(rangRazlicitihReci,rangUkupnoReci,rangSnagaLinkova,rangBrojLinkova):
    RANG = {}
    for r in rangRazlicitihReci.keys():
        RANG[r] = rangRazlicitihReci[r] - rangUkupnoReci[r] - rangSnagaLinkova[r] - rangBrojLinkova[r]
    return RANG
