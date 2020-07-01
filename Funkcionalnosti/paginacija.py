import math

def ispisiLinkove(linkovi,r0,r1,r2,r3,r4):
    print(100 * '*')
    print("RANG\t\tBR RECI\t\tR1\t\t\tR2\t\t\tR3\t\t\tR4\t\t\t\t\t\t\t\t\t\t\tlink")
    print(100 * '*')
    for link in linkovi:
        print("%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%0.3f\t\t%s" % (
        link.getRang(), r0[link.getPage()], r1[link.getPage()], r2[link.getPage()],
        r3[link.getPage()], r4[link.getPage()], link.getPage()))
    print(100 * '*')

def paginacija(linkovi,r0,r1,r2,r3,r4):
    trenutnaStrana = 1
    ukupnoLinkova = len(linkovi)
    brojLinkovaKojiSePrikazuju = 10

    while True:
        brojLinkovaKojiSePrikazuju = input("Unesite broj linkova koji zelite da se prikaze na jednoj stranici :  ")
        try:
            brojLinkovaKojiSePrikazuju = int(brojLinkovaKojiSePrikazuju)
        except:
            print('Unesite broj : ')
            continue

        if brojLinkovaKojiSePrikazuju < 1:
            print("Unesite prirodan broj : ")
            continue
        break

    while True:
        pocetak = (trenutnaStrana - 1) * brojLinkovaKojiSePrikazuju
        kraj = (trenutnaStrana - 1) * brojLinkovaKojiSePrikazuju + brojLinkovaKojiSePrikazuju
        linkoviZaIspis = linkovi[ pocetak : kraj]

        ispisiLinkove(linkoviZaIspis,r0,r1,r2,r3,r4)

        stranice = []
        for brojStranice in range(1, math.ceil(ukupnoLinkova / brojLinkovaKojiSePrikazuju) + 1):
            stranice.append(brojStranice)

        print('Nalazite se na stranici : '+ str(trenutnaStrana)+' / '+str(len(stranice)))

        choice = izaberiOpciju(stranice)
        if not choice:
            print('Pogresan unos, pokusajte ponovo')
            choice = izaberiOpciju(stranice)
        if not choice.isdigit() and choice.lower() not in ("n","b","c","x") :
            print('Pogresan unos, pokusajte ponovo')
            choice = izaberiOpciju(stranice)

        if choice.lower() == "x":
            break
        elif choice.lower() == "n":
            if(trenutnaStrana < len(stranice)):
                trenutnaStrana = trenutnaStrana+1
            else:
                print("Dosli ste do poslednje stanice!")
                choice = izaberiOpciju(stranice)

        elif choice.lower() == "b":
            if (trenutnaStrana > 1):
                trenutnaStrana = trenutnaStrana - 1
            else:
                print("Nalazite se na pocetnoj stanici!")
                choice = izaberiOpciju(stranice)
        elif choice.lower() == "c":
            paginacija(linkovi,r0,r1,r2,r3,r4)
        elif choice.isdigit() not in stranice and choice.lower() not in ("n","b","c","x"):
            print('Pogresan unos, pokusajte ponovo')
            choice = izaberiOpciju(stranice)
        else:
            unesenaVrednost = int(choice)
            if(unesenaVrednost <= len(stranice) and unesenaVrednost>0):
                 trenutnaStrana = unesenaVrednost
            else:
                print('Pogresan unos broja strane, pokusajte ponovo')
                choice = izaberiOpciju(stranice)


def izaberiOpciju(stranice) :
        print()
        print()
        print("Izaberite zeljenu opciju :")
        print()
        print("1.   Predjite na prethodnu stranicu (B) :")
        print("2.   Predjite na narednu stranicu (N) :")
        print("3.   Izaberite novi broj prikazanih linkova (C) :")
        print("4.   Izadjite iz programa (X)")
        unesenaVrednost = input('Unesite opciju  (ili broj strane na koju zelite da odete): ')
        return  unesenaVrednost



