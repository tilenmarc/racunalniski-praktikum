import math


class Ulomek:
    def __init__(self, stevec, imenovalec):
        self.stevec = stevec
        self.imenovalec = imenovalec
        self.okrajsaj()

    def __mul__(self, drugi):
        return Ulomek(self.stevec * drugi.stevec, self.imenovalec * drugi.imenovalec)

    def __repr__(self):
        return f"{self.stevec} / {self.imenovalec}"

    def okrajsaj(self):
        gcd = math.gcd(self.stevec, self.imenovalec)
        self.stevec = self.stevec // gcd
        self.imenovalec = self.imenovalec // gcd

        if self.imenovalec < 0:
            self.imenovalec *= -1
            self.stevec *= -1

    def __add__(self, drugi):
        return Ulomek(
            self.stevec * drugi.imenovalec + self.imenovalec * drugi.stevec,
            self.imenovalec * drugi.imenovalec,
        )
