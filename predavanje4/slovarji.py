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


besedilo = """RTV stands for "Room-Temperature Vulcanizing," referring to a type of silicone rubber that cures at ambient temperatures without requiring external heat.
 This curing process involves the cross-linking of silicone polymer chains, typically triggered by moisture in the air for one-component systems or through a chemical reaction between two components in two-part systems.
 RTV silicones are available in various hardnesses (typically 15 to 40 Shore A) and can be cured using catalysts such as platinum or tin compounds like dibutyltin dilaurate.
 They are widely used in applications including mold-making, automotive gaskets"""


def odstrani_podvojitve(seznam):
    """Vrne nov seznam brez podvojenih elementov"""

    nov_seznam = []
    for x in seznam:
        if x not in nov_seznam:
            nov_seznam.append(x)

    return nov_seznam


def odstrani_podvojitve2(seznam):
    """Vrne nov seznam brez podvojenih elementov"""

    nov_seznam = []

    ze_videni = set()
    for x in seznam:
        if x not in ze_videni:
            nov_seznam.append(x)
            ze_videni.add(x)

    return nov_seznam


def odstrani_podvojitve3(seznam):
    """Vrne nov seznam brez podvojenih elementov"""
    return list(set(seznam))
