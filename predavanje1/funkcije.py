def ploscina_trikotnika(a, b, c):
    s = (a + b + c) / 2
    ploscina_trik = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)

    return ploscina_trik


ploscina = ploscina_trikotnika(3, 4, 6)
print(ploscina)
