import stopaj


def poisci_v_neurejenem(sez, x):
    return x in sez


def naredi_neurejenega(elementi):
    sez = []
    for x in elementi:
        sez.append(x)


def poisci_v_mnozici(mn, x):
    return x in mn


def naredi_mnozico(elementi):
    mn = set()
    for x in elementi:
        mn.add(x)


stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_seznam(500 * n) for n in range(1, 50)],
    [
        lambda sez: poisci_v_neurejenem(sez, 0),
    ],
)
stopaj.izmeri_case_poskusov(
    [set(stopaj.nakljucen_seznam(500 * n)) for n in range(1, 50)],
    [
        lambda sez: poisci_v_mnozici(sez, 0),
    ],
)


stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_seznam(500 * n) for n in range(1, 20)],
    [
        lambda sez: naredi_neurejenega(sez),
    ],
)
stopaj.izmeri_case_poskusov(
    [stopaj.nakljucen_seznam(500 * n) for n in range(1, 20)],
    [
        lambda sez: naredi_mnozico(sez),
    ],
)
