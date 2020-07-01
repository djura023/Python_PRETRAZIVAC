def ParsirajUpit(trie):
    upit = input("Unesite upit za pretragu:")
    delovi = upit.split()
    rezultatPretrage = [None]*len(delovi)

    if len(delovi) == 0:
        ParsirajUpit(trie)
    elif len(delovi) > 3:
        for rec in delovi:
             if rec.lower() in ("and", "or", "not"):
                print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu rec1 operator rec2")
                ParsirajUpit(trie)
    else:
        if delovi[0].lower() in ("and", "or") or delovi[-1].lower() in ("and", "or", "not"):
            print("Neispravan upit,ukoliko upit ima logicki operator mora biti u formatu rec1 operator rec2")
            ParsirajUpit(trie)

    i = 0
    #trazenaLista = Set()
    for rec in delovi:
        if rec.lower() in ("and", "or", "not"):
            rezultatPretrage[i] = rec.lower()
            i = i + 1
        else:
            if not trie.search(rec):
             #   rezultatPretrage[i] = Set()
                i = i + 1
            else:
                rezultatPretrage[i] = trie.search(rec)[2].IntoSet() #dobijamo linkove na koje pokazuje taj cvor ili reci AND OR I NOT
                #trazenaLista[i] = root.search(rec)[2].IntoSet()
                i = i + 1

   s = Set()
    i = 0
    if len(rezultatPretrage) == 3:
        s = s.Unija(rezultatPretrage[0])
        if rezultatPretrage[1] == "and":
            s = s.Presek(rezultatPretrage[2])
        elif rezultatPretrage[1] == "not":
            s = s.Komplement(rezultatPretrage[2])
        elif rezultatPretrage[1] == "or":
            s = s.Unija(rezultatPretrage[2])
        else:
            s = s.Unija(rezultatPretrage[1])
            s = s.Unija(rezultatPretrage[2])
    else:
        while i < len(rezultatPretrage):
            s = s.Unija(rezultatPretrage[i])
            i = i + 1
    return s,delovi