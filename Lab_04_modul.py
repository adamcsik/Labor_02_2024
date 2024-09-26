def adatok_bekerese():
    muvelet = input("Milyen műveletet szeretne végrehajtani (+,-,*,/): ")
    while muvelet not in ("+", "-", "*", "/"):
        print("Nem jó műveletet adott meg!\nKérek új műveleti jelet!")
        muvelet = input("Milyen műveletet szeretne végrehajtani (+,-,*,/): ")

    szam1 = input("Kérek egy számot: ")
    while not szam1.isnumeric():
        print("Nem számot adott meg!")
        szam1 = input("Kérek egy számot: ")
    else:
        szam1 = int(szam1)

    szam2 = input("Kérek még egy számot: ")
    while not szam2.isnumeric():
        print("Nem számot adott meg!")
        szam2 = input("Kérek megint egy számot: ")
    else:
        szam2 = int(szam2)
    return szam1, muvelet, szam2


def muveletek_vegrehajtasa(szam1, muvelet, szam2):
    eredmeny = 0
    if muvelet == "+":
        eredmeny = szam1 + szam2
    elif muvelet == "-":
        eredmeny = szam1 - szam2
    elif muvelet == "*":
        eredmeny = szam1 * szam2
    elif muvelet == "/":
        eredmeny = szam1 / szam2
    return eredmeny


def eredmenyek_megjelenitese(szam1, muvelet, szam2, eredmeny):
    print("A művelet vérehajtása:")
    print(str(szam1).rjust(30))
    print(str(szam2).rjust(30))
    print(muvelet, "".rjust(29, "_"), sep="")
    print(str(eredmeny).rjust(30))
