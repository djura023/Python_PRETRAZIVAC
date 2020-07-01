import math
class Ispis:

    def __init__(self,r0,r1,r2,r3,r4,rang,link):
        self.link = link
        self.rang0 = r0
        self.rang1 = r1
        self.rang2 = r2
        self.rang3 = r3
        self.rang4 = r4
        self.rang  = rang

    def Ispisi(self):
        rang = round(self.rang,3)
        m0 = round(self.rang0)
        m1 = round(self.rang1,3)
        m2 = round(self.rang2,3)
        m3 = round(self.rang3,3)
        m4 = round(self.rang4,3)
        print("%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%s"%(rang,m0,m1,m2,m3,m4,self.link))
        #print(f'{rang:2}  {m0:8}  {m1:8}  {m2:8}  {m3:8}  {m4:4} ',self.link)