
class Cvor :
    def __init__(self,link,ulazniLinkovi,izlazniLinikovi,rang = 0):
        self.ulazniLinkovi = ulazniLinkovi
        self.izlazniLinkovi = izlazniLinikovi
        self.link = link
        self.rang = rang

    def getUlazniLinkovi(self):
        return self.ulazniLinkovi

    def getIzlazniLinkovi(self):
        return self.izlazniLinkovi

    def addUlazniLink(self, link):
        self.ulazniLinkovi.append(link)

    def addIzlazniLink(self,link):
        self.izlazniLinkovi.append(link)

    def set_rang(self,rang):
        self.rang = rang