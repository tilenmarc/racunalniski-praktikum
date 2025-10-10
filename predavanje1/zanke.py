# a = 1
# while a <= 1000000:
#     print(a)
#     a = a + 1


def fakulteta(n):
    rezultat = 1
    i = 1
    # ponavljamo zanko
    while i <= n:
        rezultat = rezultat * i
        i = i + 1

    return rezultat


def fakulteta2(n):
    rezultat = 1
    for i in range(n):
        rezultat = rezultat * (i + 1)

    return rezultat
