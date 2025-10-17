def produkt(sez):
    pr = 1

    for k in range(len(sez)):
        pr = pr * sez[k]

    return pr


def produkt2(sez):
    pr = 1

    for el in sez:
        pr = pr * el

    return pr


def indeks_najvecjega(sez):
    najvecji = sez[0]
    indeks = 0

    for i in range(len(sez)):
        el = sez[i]
        if el > najvecji:
            najvecji = el
            indeks = i

    return indeks


def sodi_elementi(sez):
    nov_seznam = []

    for x in sez:
        if x % 2 == 0:
            nov_seznam.append(x)

    return nov_seznam
