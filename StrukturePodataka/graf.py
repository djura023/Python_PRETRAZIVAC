import os

from StrukturePodataka.trieStruct import Trie
from Funkcionalnosti.parser import Parser

class Graph:
    def __init__(self):
        self.ulazniLinkovi = {}
        self.izlazniLinkovi = {}

    def dodavanjeNoveStranice(self, link, linkoviNaKojePokazuje):
        self.dodavanjeLinka(link)
        self.dodavanjeGrana(link,linkoviNaKojePokazuje)

    def dodavanjeGrana(self,link,linkoviNaKojePokazuje):
        for linkNaKojiPokazuje in linkoviNaKojePokazuje:
            self.dodavanjeGrane(link, linkNaKojiPokazuje)


    def dodavanjeLinka(self, link):
        if link not in self.izlazniLinkovi.keys():
            self.izlazniLinkovi[link] = []
        if link not in self.ulazniLinkovi.keys():
            self.ulazniLinkovi[link] = []

    def dodavanjeGrane(self, pocetniLink, krajnjiLink):
        if pocetniLink not in self.ulazniLinkovi.keys():
            self.ulazniLinkovi[pocetniLink] = []
        if krajnjiLink not in self.ulazniLinkovi.keys():
            self.ulazniLinkovi[krajnjiLink] = []

        self.izlazniLinkovi[pocetniLink].append(krajnjiLink)
        self.ulazniLinkovi[krajnjiLink].append(pocetniLink)


    def getLinkove(self):
        return list(
            self.ulazniLinkovi.keys())

    def getIzlazneLinkove(self, link):
        return list(self.izlazniLinkovi[link])

    def getUlazneLinkove(self, link):
        return list(self.ulazniLinkovi[link])
