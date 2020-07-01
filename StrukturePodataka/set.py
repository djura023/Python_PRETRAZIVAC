import  os
class Set():
    def __init__(self,skup = None):
        if skup is None:
            self.recnik = {}
        else:
            self.recnik = skup.recnik

    def unijaRecnika(self, drugiSkup):
        unijaSkupova = Set()
        for elementPrvogSkupa in self.recnik:
            unijaSkupova.dodavanjeLinka(elementPrvogSkupa)
        for elementDrugogSkupa in drugiSkup.recnik:
            unijaSkupova.dodavanjeLinka(elementDrugogSkupa)
        return unijaSkupova

    def komplementRecnika(self, drugiRecnik):
        komplementSkupa = Set()
        for elementIzPrvogRecnika in self.recnik:
            if not drugiRecnik.daLiImaLink(elementIzPrvogRecnika):
                komplementSkupa.dodavanjeLinka(elementIzPrvogRecnika)
        return komplementSkupa

    def presekRecnika(self, drugiSkup):
        presekSkupova = Set()
        for elementIzPrvogSkupa in self.recnik:
             if drugiSkup.sadrziLink(elementIzPrvogSkupa):
                presekSkupova.dodavanjeLinka(elementIzPrvogSkupa)
        return presekSkupova

    def uklanjanjeLinka(self, elementZaUklanjanje):
        if elementZaUklanjanje in self.recnik.keys():
            del self.recnik[elementZaUklanjanje]

    def dodavanjeLinka(self, link):
        self.recnik[link] = link

    def daLiImaLink(self, link):  # menjala
        if link not in self.recnik.keys():
             return False
        return True

    def kljucevi(self):
        return self.recnik.keys()

    def duzinaRecnika(self):
        return len(self.recnik.keys())

    def pretvoriRecnikUListu(self):
        lista = []
        for element in self.recnik.keys():
            lista.append(element)
        return lista

    def ispisRecnika(self):
        for elementZaIspis in self.recnik:
            print(elementZaIspis)











