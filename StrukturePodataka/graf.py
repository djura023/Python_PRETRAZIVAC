from Python_PRETRAZIVAC.StrukturePodataka.cvor import Cvor

class Graph:
    def __init__(self):
       self.cvorovi = {}


    def dodajLinkUCvorove(self, link):
        if link not in self.cvorovi.keys() :
            novi = Cvor(link,[],[])
            self.cvorovi[link] = novi

    def dodajGranuNaCvor(self,link,linkoviNaKojePokazuje):
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

    def dodavanjeNoveStranice(self, link, linkoviNaKojePokazuje):
        self.dodajLinkUCvorove(link)
        self.dodajGranuNaCvor(link,linkoviNaKojePokazuje)

    def getLinkove(self):
        return  self.cvorovi.keys()

    def getUlazneLinkove(self, link):
        return self.cvorovi[link].getUlazniLinkovi()
    def getIzlazneLinkove(self, link):
        return self.cvorovi[link].getIzlazniLinkovi()
