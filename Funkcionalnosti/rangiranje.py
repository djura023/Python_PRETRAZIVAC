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
    for link in linokviPretrage.recnik:
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
                if (len(graf.getUlazneLinkove(os.path.abspath(link))) != 0):
                    recnikBrojaLinkova[link] = len(graf.getUlazneLinkove(os.path.abspath(link)))
                recnikZaUkupnoPojavljivanjeReciNaLinku[link] += recnikBrojaPonavljanjaJedneReciULink[link]
                recnikZaRazliciteReci[link]+=1

        # recnik -> kljuc je snaga linkova
        for odredjeniLink in recnikZaUkupnoPojavljivanjeReciNaLinku :
            for linkPokazivac in graf.cvorovi[odredjeniLink].getUlazniLinkovi() :
                if linkPokazivac in recnikZaUkupnoPojavljivanjeReciNaLinku :
                    recnikSnageLinkova[odredjeniLink] += recnikZaUkupnoPojavljivanjeReciNaLinku[linkPokazivac]

    for link in recnikZaUkupnoPojavljivanjeReciNaLinku :
        if (len(graf.getUlazneLinkove(os.path.abspath(link))) != 0):

            recnikBrojaLinkova[link] = len(graf.getUlazneLinkove(os.path.abspath(link)))
            brojRazlicitihReci = recnikZaRazliciteReci[link]
            brojzaSnaguLinkova = recnikSnageLinkova[link]
            brUkupnoPojav = recnikZaUkupnoPojavljivanjeReciNaLinku[link]
            brZaRangIzCvora = round(float(graf.cvorovi[link].getRang()),5)
            if brojRazlicitihReci == 0 :
                brojRazlicitihReci = 1
            if brojzaSnaguLinkova == 0 :
                brojzaSnaguLinkova = 1
            if brUkupnoPojav == 0 :
                brUkupnoPojav = 1
            if brZaRangIzCvora == 0 :
                brZaRangIzCvora = 1
            snagaL = 0.35 / brojzaSnaguLinkova
            brR = 0.32 /brUkupnoPojav
            pr = 0.33 / brZaRangIzCvora
            velicinaRanga = brojRazlicitihReci + 1-(snagaL+brR+pr)

            recnikRangova[link] = Rang(brUkupnoPojav,brojRazlicitihReci,brR,pr,snagaL,velicinaRanga,odredjeniLink)

    return recnikRangova


