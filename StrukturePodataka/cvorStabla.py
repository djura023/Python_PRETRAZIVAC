from StrukturePodataka.set import Set
class CvorStabla:

    def __init__(self):
        self.deca = {}
        self.krajReci = (False,0)
        self.linkovi = {}

    def prebaciUSet(self):
        s = Set()
        for link in self.linkovi:
            s.recnik[link] = link
        return s
