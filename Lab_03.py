""" Jövedelemszámítás bruttó és kor alapján
print("Jövedelemszámítás\n")
brutto = int(input("Kérem a bruttó jövedelmét: "))
kor = int(input("Hány éves vagy: "))

if kor < 25:
    if brutto < 599790:
        szja = 0
    else:
        szja = (brutto - 599790) * 0.15
else:
    szja = brutto * 0.15
nyugdij = brutto * 0.1
tb = brutto * 0.07
munkanelkuli = brutto * 0.015
netto = brutto - szja - nyugdij - tb - munkanelkuli

print("Jövedelem".center(50))
print("")
print("Bruttó jövedelem:".ljust(25, "_"), str(brutto).rjust(25, "_"), " Ft", sep="")
print("SZJA:".ljust(25, "_"), str(int(szja)).rjust(25, "_"), " Ft", sep="")
print("Nyugdíj:".ljust(25, "_"), str(int(nyugdij)).rjust(25, "_"), " Ft", sep="")
print("TB:".ljust(25, "_"), str(int(tb)).rjust(25, "_"), " Ft", sep="")
print("Munkanélküli:".ljust(25, "_"), str(int(munkanelkuli)).rjust(25, "_"), " Ft", sep="")
print("")
print("Nettó jövedelem:".ljust(25, "_"), str(int(netto)).rjust(25, "_"), " Ft", sep="")
"""

# Számológép a négy alapműveletre
print("Számológép")
eredmeny = 0
muvelet = input("Milyen műveletet szeretne végrehajtani (+,-,*,/): ")
if muvelet not in ("+", "-", "*", "/"):
    print("Nem jó műveletet adott meg!")
    exit()
else:
    szam1 = int(input("Kérek egy számot: "))
    szam2 = int(input("Kérek még egy számot: "))

    if muvelet == "+":
        eredmeny = szam1 + szam2
    elif muvelet == "-":
        eredmeny = szam1 - szam2
    elif muvelet == "*":
        eredmeny = szam1 * szam2
    elif muvelet == "/":
        eredmeny = szam1 / szam2

    print("A művelet:", szam1, muvelet, szam2, "=", eredmeny)
