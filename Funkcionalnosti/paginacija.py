import math
import winsound
class Fore():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def ispisiRangove(recnikRangova):
    print(Fore.WHITE + 170 * '*')
    print(Fore.BLUE +70*' '+ "\033[1m" +"SADRZAJ" + "\033[0m")
    print(Fore.WHITE + 170 * '-')
    print(Fore.BLUE+"RANG"+8*' '+"BROJ"+7*' '+"RAZLICITE"+4*' '+"UTICAJ BROJA"+5*' '+"UTICAJ SNAGE"+4*' '+"UTICAJ BROJA"+45*' '+"LINKOVI")
    print(Fore.BLUE+"LINKA"+7*' '+"RECI"+9*' '+"RECI"+11*' '+"RECI"+12*' '+"LINKOVA"+9*' '+"LINKOVA")
    print(Fore.WHITE+170 * '-')
    for link in recnikRangova.keys():
        print(Fore.CYAN+ "%-12.3f%-12.3f%-12.3f\t%-12.3f\t%-12.3f\t%-12.3f\t\t\t%s" % (
        recnikRangova[link][0],recnikRangova[link][1],recnikRangova[link][2],recnikRangova[link][3],recnikRangova[link][4],recnikRangova[link][5],link))
    print(Fore.WHITE+170 * '*')

def odredjivanjeLinkovaZaPrikaz(linkovi,brojLinkovaKojiSePrikazuju, stranicaKojaSePrikazuje)   :
    sviLinkovi = []
    for link in linkovi :
        sviLinkovi.append(link)
    indexPrvogLinka = (stranicaKojaSePrikazuje - 1) * brojLinkovaKojiSePrikazuju
    indexPoslednjegLinka = (stranicaKojaSePrikazuje - 1) * brojLinkovaKojiSePrikazuju + brojLinkovaKojiSePrikazuju
    return sviLinkovi[indexPrvogLinka: indexPoslednjegLinka]

def odredjivanjeStranica(ukupnoLinkova,brojLinkovaKojiSePrikazuju,stranicaKojaSePrikazuje):
    stranice = []
    for brStr in range(1, math.ceil(ukupnoLinkova / brojLinkovaKojiSePrikazuju) + 1):
        stranice.append(brStr)
    print(Fore.BLUE+'STRANA  : ' + str(stranicaKojaSePrikazuje) + ' / ' + str(len(stranice)))
    if stranicaKojaSePrikazuje > len(stranice) :
        stranicaKojaSePrikazuje = len(stranice)
    return stranice

def izmeniBrojLinkovaKojiSePrikazuju():
    fr = 2000
    d = 50
    while True:
        ukupnoPrikazanihLinkova = input(Fore.BLUE+ "Unesite zeljeni broj :  ")
        if not ukupnoPrikazanihLinkova.isdigit():
            greska()
            continue
        ukupnoPrikazanihLinkova = int(ukupnoPrikazanihLinkova)
        if ukupnoPrikazanihLinkova < 1:
            greska()
            continue
        break
    return  ukupnoPrikazanihLinkova

def izaberiBrojStranice(ukupno):
    fr = 2000
    d = 50
    while True :
        brStr = input(Fore.BLUE+"Unesite broj stranice na koju zelite da predjete : ")
        if not brStr.isdigit():
            greska()
            continue
        brStr = int(brStr)
        if brStr < 1 or brStr > ukupno:
            greska()
            continue
        break
    return brStr

def greska() :
    fr = 2000
    d = 50
    print(Fore.RED + 'Pogresan unos, pokusajte ponovo. ')
    winsound.Beep(fr, d)

def izaberiOpciju(stranice,indikator) :
    ponovi = True
    odgovor = ""

    while ponovi:
        if(indikator=="pocetak") :
            print(Fore.GREEN + "\033[1m" + """
                    IZABERITE :
            2. Naredna stranica
            3.Promeni broj linkova koji se prikazuju
            4.Unesi broj stranice na koju zelite da odete
            5.Izbor prethodnih opcija
            """ + "\033[0m")
        elif (indikator == "kraj"):
            print(Fore.GREEN + "\033[1m" + """
                    IZABERITE :
            1. Prethodna stranica
            3.Promeni broj linkova koji se prikazuju
            4.Unesi broj stranice na koju zelite da odete
            5.Izbor prethodnih opcija
            """ + "\033[0m")
        else :
            print(Fore.GREEN+"\033[1m" +"""
                    IZABERITE :
            1. Prethodna stranica
            2. Naredna stranica
            3.Promeni broj linkova koji se prikazuju
            4.Unesi broj stranice na koju zelite da odete
            5.Izbor prethodnih opcija
            """ + "\033[0m")
        odgovor = input(Fore.BLUE + "\033[1m" +"\tKoju opciju birate? " + "\033[0m")
        if not odgovor.isdigit():
            greska()
            continue
        odgovor = int(odgovor)
        if indikator == "pocetak" and odgovor == 1 :
            greska()
            continue
        if indikator == "kraj" and odgovor == 2:
            greska()
            continue
        if odgovor > 5 or odgovor < 1 :
            greska()
            continue
        ponovi= False

    return odgovor

def paginacija(recnikRangova):

    stranicaKojaSePrikazuje = 1
    ukupnoLinkova = len(recnikRangova)
    ukupnoPrikazanihLinkova = 10
    indikator = ""
    stranice = []

    while True:
        prikaziOve = {}

        zaPrikaz = odredjivanjeLinkovaZaPrikaz(recnikRangova.keys(),ukupnoPrikazanihLinkova,stranicaKojaSePrikazuje)
        for link in zaPrikaz :
            prikaziOve[link] = recnikRangova[link]
        ispisiRangove(prikaziOve)
        stranice =odredjivanjeStranica(ukupnoLinkova,ukupnoPrikazanihLinkova,stranicaKojaSePrikazuje)
        izabranaOpcija = izaberiOpciju(stranice,indikator)

        if izabranaOpcija == 5:
            indikator=""
            break
        elif izabranaOpcija ==4:
            indikator=""
            stranicaKojaSePrikazuje = izaberiBrojStranice(len(stranice))
            continue
        elif izabranaOpcija == 3:
            indikator = ""
            ukupnoPrikazanihLinkova = izmeniBrojLinkovaKojiSePrikazuju()
            stranice = odredjivanjeStranica(ukupnoLinkova,ukupnoPrikazanihLinkova,stranicaKojaSePrikazuje)
            if stranicaKojaSePrikazuje > len(stranice) :
                stranicaKojaSePrikazuje =len(stranice)
            continue
        elif izabranaOpcija == 2:
            indikator=""
            if(stranicaKojaSePrikazuje < len(stranice)):
                stranicaKojaSePrikazuje +=1
                continue
            else:
                print(Fore.RED+"PRIKAZANA JE POSLEDNJA STRANICA")
                indikator = "kraj"
                continue
        elif izabranaOpcija == 1:
            indikator = ""
            if (stranicaKojaSePrikazuje > 1):
                stranicaKojaSePrikazuje -= 1
                continue
            else:
                print(Fore.RED+"PRIKAZANA JE PRVA STRANICA")
                indikator = "pocetak"










