class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def __getitem__(self, n):
        return self.zacetni_clen + n * self.razlika

    def __add__(self, drugi):
        return AritmeticnoZaporedje(
            self.zacetni_clen + drugi.zacetni_clen, self.razlika + drugi.razlika
        )

    def __repr__(self):
        return f"Aritmeticno zaporedje: {self.zacetni_clen}, {self.n_ti_clen(1)},{self.n_ti_clen(2)},..."

    def __eq__(self, drugi):
        return self.zacetni_clen == drugi.zacetni_clen and self.razlika == drugi.razlika

    def __str__(self):
        return f"Aritmeticno zaporedje({self.zacetni_clen}, {self.razlika})"
