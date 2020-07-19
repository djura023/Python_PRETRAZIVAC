import math
class Rang:

    def __init__(self,brojReci,razliciteReci,uticajBrReci,snagaLinkova,brLinkova,rang,link):
        self.link = link
        self.brojReci = brojReci
        self.razliciteReci = razliciteReci
        self.uticajBrReci = uticajBrReci
        self.snagaLinkova = snagaLinkova
        self.brLinkova = brLinkova
        self.ukupniRang  = rang

    def getR0(self):
        return self.brojReci
    def getR1(self):
        return self.razliciteReci
    def getR2(self):
        return self.uticajBrReci
    def getR3(self):
        return self.snagaLinkova
    def getR4(self):
        return self.brLinkova
    def getRang(self):
        return self.ukupniRang

