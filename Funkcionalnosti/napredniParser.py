from parglare import Grammar, Parser, ParseError


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


def greska():
    fr = 2000
    d = 50
    print(Fore.RED + "\033[1m" + "Pogresan unos!" + "\033[0m")


def napredniParsirajUpit(stablo, graf):
    upit = input("Unesite upit za pretragu:")
    delovi = upit.split()

    gramatika = r"""
    E: E '||' E  {left, 1}
     | E E       {left, 1}
     | E '&&' E  {left, 2}
     | '(' E ')'
     | '!' E1
     | rec;
    E1: rec
     | '(' E ')';

    terminals
    rec: /[\w\d]+/;
    """

    try:
        akcije = {
            "E": [lambda _, n: n[0].unijaRecnika(n[2]),
                  lambda _, n: n[0].unijaRecnika(n[1]),
                  lambda _, n: n[0].presekRecnika(n[2]),
                  lambda _, n: n[1],
                  lambda _, n: graf.getLinkoveKaoSet().komplementRecnika(n[1]),
                  lambda _, n: stablo.nadjiRec(n[0])[2].prebaciUSet()],
            "E1": [lambda _, n: stablo.nadjiRec(n[0])[2].prebaciUSet(),
                   lambda _, n: n[1]]
        }
    except TypeError:
        greska()
        return -1

    g = Grammar.from_string(gramatika)
    parser = Parser(g, actions=akcije)

    try:
        finalniSkup = parser.parse(upit)
    except ParseError:
        greska()
        return -1

    return finalniSkup, delovi
