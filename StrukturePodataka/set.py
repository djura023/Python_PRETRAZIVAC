import  os
class Set():
    def __init__(self,skup = None):
        if skup != None:
            self.recnik = skup.recnik
        else:
            self.recnik = {}

    def unijaRecnika(self, drugiSkup):

        unijaSkupova = Set()
        for elementPrvogSkupa in self.recnik:
            unijaSkupova.recnik[elementPrvogSkupa] = elementPrvogSkupa
        for elementDrugogSkupa in drugiSkup.recnik:
            unijaSkupova.recnik[elementDrugogSkupa] = elementDrugogSkupa
        return unijaSkupova

    def komplementRecnika(self, drugiSkup):
        komplementSkupa = Set()
        for elementPrvogSkupa in self.recnik:
            if elementPrvogSkupa not in drugiSkup.kljucevi:
                komplementSkupa.recnik[elementPrvogSkupa] = elementPrvogSkupa
        return komplementSkupa

    def presekRecnika(self, drugiSkup):
        presekSkupova = Set()
        for elementPrvogSkupa in self.recnik:
             if elementPrvogSkupa not in drugiSkup.kljucevi:
                presekSkupova.recnik[elementPrvogSkupa] = elementPrvogSkupa
        return presekSkupova

    def kljucevi(self):
        return self.recnik.keys()

    def pretvoriRecnikUListu(self):
        lista = []
        for element in self.kljucevi():
            lista.append(element)
        return lista












