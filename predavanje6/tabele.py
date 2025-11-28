import csv

with open("tabela.csv", "w") as dat:
    pistelj = csv.writer(dat)

    pistelj.writerow(["ime", "priimek"])

    pistelj.writerow(["Tilen", "Marc"])
