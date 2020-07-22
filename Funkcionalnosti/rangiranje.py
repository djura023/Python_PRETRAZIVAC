import os
import math
import random
from StrukturePodataka.rang import Rang
import operator

def rjecnikZaRang(root, nizReciIzUpita, linokviPretrage,graf, flag):
    recnikRangova = {}
    recnikSnageLinkova = {}
    recnikBrojaLinkova = {}
    recnikZaUkupnoPojavljivanjeReciNaLinku = {}
    recnikZaRazliciteReci = {}
    reciZaPrebrojavanje = {}


    for link in linokviPretrage.recnik:
        recnikZaUkupnoPojavljivanjeReciNaLinku[os.path.abspath(link)] = 0
        recnikZaRazliciteReci[os.path.abspath(link)]=0
        recnikSnageLinkova[os.path.abspath(link)] = 0
        recnikRangova[os.path.abspath(link)] = 0
        recnikBrojaLinkova[os.path.abspath(link)] = 0
    f = 0
    if flag == 1 :
        for i in range(len(nizReciIzUpita)):
            if nizReciIzUpita[i].lower() in ("not") :
                f=1
            if f == 1 or f == 2 :
                f=2
                continue
            f = 0
            if nizReciIzUpita[i].lower() not in ("and","or","not"):
                reciZaPrebrojavanje[nizReciIzUpita[i]] = nizReciIzUpita[i]
    else :
        for i in range(len(nizReciIzUpita)):
            if nizReciIzUpita[i].lower() in ("!"):
                f = 1
            if f == 1 or f == 2:
                f = 2
                continue
            f = 0
            if nizReciIzUpita[i].lower() not in ("&&", "||", "!"):
                reciZaPrebrojavanje[nizReciIzUpita[i]] = nizReciIzUpita[i]

    for rec in reciZaPrebrojavanje:
        cvorNaKomSeZavrsavaRec = root.nadjiCvor(rec)[0]
        recnikBrojaPonavljanjaJedneReciULink = {}


        for pom in cvorNaKomSeZavrsavaRec.linkovi:
            recnikBrojaPonavljanjaJedneReciULink[os.path.abspath(pom)] = cvorNaKomSeZavrsavaRec.linkovi[pom]


        for link in recnikBrojaPonavljanjaJedneReciULink:
            if link in recnikZaUkupnoPojavljivanjeReciNaLinku.keys():
                if (len(graf.getUlazneLinkove(os.path.abspath(link))) != 0):
                    recnikBrojaLinkova[link] = len(graf.getUlazneLinkove(os.path.abspath(link)))
                recnikZaUkupnoPojavljivanjeReciNaLinku[link] += recnikBrojaPonavljanjaJedneReciULink[link]
                recnikZaRazliciteReci[link]+=1


        for odredjeniLink in recnikZaUkupnoPojavljivanjeReciNaLinku :
            for linkPokazivac in graf.cvorovi[odredjeniLink].getUlazniLinkovi() :
                if linkPokazivac in recnikZaUkupnoPojavljivanjeReciNaLinku :
                    recnikSnageLinkova[odredjeniLink] += recnikZaUkupnoPojavljivanjeReciNaLinku[linkPokazivac]

    for link in recnikZaUkupnoPojavljivanjeReciNaLinku :
        if (len(graf.getUlazneLinkove(os.path.abspath(link))) != 0):

            recnikBrojaLinkova[link] = len(graf.getUlazneLinkove(os.path.abspath(link)))
            brojRazlicitihReci = recnikZaRazliciteReci[link]
            brojzaSnaguLinkova = recnikSnageLinkova[link] + 1
            brUkupnoPojav = recnikZaUkupnoPojavljivanjeReciNaLinku[link] + 1
            brZaRangIzCvora = round(float(graf.cvorovi[link].getRang()),5) + 1
            snagaL = 0.35 / brojzaSnaguLinkova
            brR = 0.32 /brUkupnoPojav
            pr = 0.33 / brZaRangIzCvora
            velicinaRanga = brojRazlicitihReci + 1-(snagaL+brR+pr)

            recnikRangova[link] = Rang(brUkupnoPojav - 1,brojRazlicitihReci,brR,pr,snagaL,velicinaRanga,link)

    return recnikRangova


