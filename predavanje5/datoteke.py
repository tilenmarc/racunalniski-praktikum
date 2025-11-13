import os


def prestej_pojavitve(niz):
    pojavitve = {}

    for crka in niz:
        if not crka.isalpha():
            continue
        if crka in pojavitve:
            pojavitve[crka] = pojavitve[crka] + 1
        else:
            pojavitve[crka] = 1

    return pojavitve


def kljuc_najvecje_vrednosti(slovar):
    najvecji = None
    kljuc_naj = None

    for kljuc, vrednost in slovar.items():
        if najvecji == None:
            najvecji = vrednost
            kljuc_naj = kljuc
        else:
            if vrednost > najvecji:
                najvecji = vrednost
                kljuc_naj = kljuc

    return kljuc_naj


def prestej_crke(ime_datoteke):
    with open(ime_datoteke) as dat:
        datoteka_niz = dat.read()
        datoteka_niz = datoteka_niz.lower()

        return prestej_pojavitve(datoteka_niz)


def prestej_besede(ime_datoteke):
    dat = open(ime_datoteke)

    pojavitve = {}

    for vrstica in dat:
        besede = vrstica.split(" ")

        for beseda in besede:
            cista_beseda = ""
            for crka in beseda:
                if crka.isalpha():
                    cista_beseda += crka.lower()

            if cista_beseda == "":
                continue

            if cista_beseda not in pojavitve:
                pojavitve[cista_beseda] = 1

            else:
                pojavitve[cista_beseda] += 1

    dat.close()

    return pojavitve


def izpisi_imenik(pot, zamik=""):
    datoteke = os.listdir(pot)

    for datoteka in datoteke:
        print(zamik + datoteka)

        if os.path.isdir(os.path.join(pot, datoteka)):
            izpisi_imenik(os.path.join(pot, datoteka), zamik + "  ")
