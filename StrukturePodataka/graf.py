
import os

from StrukturePodataka.cvor import Cvor
from StrukturePodataka.set import Set
from StrukturePodataka.strukturaStabla import *
from Funkcionalnosti.parser import Parser

class Graph:
    def __init__(self):
       self.cvorovi = {}


    def getLinkove(self):
        return  self.cvorovi.keys()

    def getLinkoveKaoSet(self):
        s = Set()
        for link in self.cvorovi.keys():
            s.recnik[link] = link
        return s

    def getUlazneLinkove(self, link):
        return self.cvorovi[link].getUlazniLinkovi()
    def getIzlazneLinkove(self, link):
        return self.cvorovi[link].getIzlazniLinkovi()


    def dodavanjeNoveStranice(self, link, linkoviNaKojePokazuje):
        self.dodavanjeLinka(link)
        self.dodavanjeGrana(link,linkoviNaKojePokazuje)

    def dodavanjeGrana(self,link,linkoviNaKojePokazuje):
        if link not in self.cvorovi.keys() :
            novi = Cvor(link,[],linkoviNaKojePokazuje)
            self.cvorovi[link] = novi
        else :
            for linkNaKojiPokazuje in linkoviNaKojePokazuje:
                if linkNaKojiPokazuje not in self.cvorovi.keys() :
                    novi = Cvor(linkNaKojiPokazuje,[],[])
                    self.cvorovi[linkNaKojiPokazuje] = novi
                self.cvorovi[linkNaKojiPokazuje].addUlazniLink(link)
                self.cvorovi[link].addIzlazniLink(linkNaKojiPokazuje)
                #self.dodavanjeGrane(link, linkNaKojiPokazuje)


    def dodavanjeLinka(self, link):
        if link not in self.cvorovi.keys() :
            novi = Cvor(link,[],[])
            self.cvorovi[link] = novi

