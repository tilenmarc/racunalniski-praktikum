def rekurzija(n):
    print(n)

    if n == 0:
        return

    rekurzija(n - 1)


def fakulteta(n):
    if n == 1:
        return 1

    return n * fakulteta(n - 1)


def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_bolje(n, nicti=1, prvi=1):
    if n == 0:
        return nicti
    if n == 1:
        return prvi

    return fibonacci_bolje(n - 1, prvi, nicti + prvi)
