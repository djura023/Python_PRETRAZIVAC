# Preuzeta implementacija sa : https://www.geeksforgeeks.org/trie-insert-and-search/
from StrukturePodataka.cvorStabla import CvorStabla

class Stablo:

    def __init__(self):
        self.koren = self.getCvor()

    def _slovoUIndeks(self, ch):

        return ord(ch) - ord('a')

    def getCvor(self):

        return CvorStabla()

    def dodaj(self, rec,link):
        rec = rec.lower()
        cvor = self.koren
        duzina = len(rec)
        for level in range(duzina):
            indeks = self._slovoUIndeks(rec[level])
            if indeks not in cvor.deca:
                cvor.deca[indeks] = self.getCvor()
            cvor = cvor.deca[indeks]
        m = cvor.krajReci[1] + 1
        cvor.krajReci = (True, m)

        self.brojReciUlinku(cvor,link)

    def nadjiRec(self, rec):
        rec = rec.lower()
        cvor = self.koren
        duzina = len(rec)
        for level in range(duzina):
            indeks = self._slovoUIndeks(rec[level])
            if indeks not in cvor.deca:
                return False
            cvor =  cvor.deca[indeks]
        return  cvor.krajReci,cvor.linkovi,cvor

    def brojReciUlinku(self,cvor,link):
        if link not in cvor.linkovi:
            cvor.linkovi[link] = 1
        else:
            cvor.linkovi[link] += 1


    def nadjiCvor(self, rijecZaPretragu):
        recZaKojuSeOdredjujeBrojPonavljanja = rijecZaPretragu.lower()
        postoji = False
        if self.nadjiRec(recZaKojuSeOdredjujeBrojPonavljanja):
            postoji = True
            novicvor = self.nadjiRec(recZaKojuSeOdredjujeBrojPonavljanja)[2]  # vraca cvor
        else:
            novicvor = self.koren
        return novicvor, postoji

