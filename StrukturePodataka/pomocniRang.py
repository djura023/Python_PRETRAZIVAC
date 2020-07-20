class PomocniRang:
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