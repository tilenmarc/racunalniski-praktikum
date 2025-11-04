def pogovor():
    print("Zivijo, kako ti je ime?")

    odgovor1 = input()

    print(f"{odgovor1} je lepo ime. Koliko si star?")

    while True:
        odgovor2 = input()
        starost = int(odgovor2)
        if starost > 25:
            print(f"Uff {odgovor2} je zelo veliko. Poskusi ponovno.")
        else:
            print("dobro zate")
            break
