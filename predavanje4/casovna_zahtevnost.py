def indeks_najmanjsega(sez):
    if len(sez) == 0:
        return None

    najmanjsi = sez[0]
    indeks = 0

    for i in range(len(sez)):
        el = sez[i]
        if el < najmanjsi:
            najmanjsi = el
            indeks = i

    return indeks


def uredi_seznam(sez):
    """Vrne nov seznam, ki ima elemente urejene po velikosti."""
    nov_seznam = []

    for _ in range(len(sez)):
        ind = indeks_najmanjsega(sez)
        nov_seznam.append(sez[ind])
        del sez[ind]

    return nov_seznam
