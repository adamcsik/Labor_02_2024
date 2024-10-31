class Jelszo:
    felhasznalo_jelszava = "nincs"

    def __init__(self, felhasznalo_jelszava = "valamiJelszo123"):
        self.felhasznalo_jelszava = felhasznalo_jelszava

    def jelszo_bekerese(self,hosszusag):
        def hossz(_jelszo, min_hossz):
            ok = True
            if len(_jelszo) < min_hossz:
                ok = False
            return ok

        def szamjegyek(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isnumeric():
                    ok = True
                    break
            return ok

        def kisbetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.islower():
                    ok = True
                    break
            return ok

        def nagybetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isupper():
                    ok = True
                    break
            return ok

        jelszo = input("Kérem a jelszót: ")
        while not hossz(jelszo, hosszusag) or not szamjegyek(jelszo) or not kisbetu(jelszo) or not nagybetu(jelszo) or " " in jelszo:
            print("Nem megfelelő a jelszó!")
            jelszo = input("Kérem a jelszót: ")
        self.felhasznalo_jelszava = jelszo

    def jelszo_generalasa(self, hossz=8, kisbetu=True, nagybetu=True, szam=True):
        import random
        import string
        jelszo = ""
        karaktersor = ""
        if kisbetu:
            karaktersor = string.ascii_lowercase
        if nagybetu:
            karaktersor = karaktersor + string.ascii_uppercase
        if szam:
            karaktersor = karaktersor + string.digits
        for _ in range(hossz):
            jelszo = jelszo + karaktersor[random.randint(0, len(karaktersor))]
        self.felhasznalo_jelszava = jelszo

    def jelszo_ellenorzese(self):
        ok = False
        proba = 0
        while True:
            jelszo2 = input("Kérem ismét a jelszót: ")
            if self.felhasznalo_jelszava == jelszo2:
                ok = True
                break
            else:
                proba += 1
                print("Nem megfelelő a jelszó!")
                if proba == 3:
                    break
        return ok


class Felhasznalo(Jelszo):
    felhasznalo_neve = "Valaki@valami.hu"

    def __init__(self, felhasznalo_jelszava = "ÚjJelszó2"):
        super().__init__(felhasznalo_jelszava)

    def felhasznalonev(self):
        _felhasznalo_neve = input("Kérem a felhasználói nevet (email): ")
        while " " in _felhasznalo_neve or "@" not in _felhasznalo_neve or "." not in _felhasznalo_neve:
            print("Érvénytelen emailformátum!")
            if " " in _felhasznalo_neve:
                print("Szóközt használt az emailben!")
            if "@" not in _felhasznalo_neve:
                print("Hiánzik a @ jel")
            if "." not in _felhasznalo_neve:
                print("Hiánzik a . jel")
            _felhasznalo_neve = input("Kérem a felhasználói nevet (email): ")
        self.felhasznalo_neve = _felhasznalo_neve

    def rogtites(self):
        with open('dolgozok.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(self.felhasznalo_neve + ";" + self.felhasznalo_jelszava + "\n")

    def tarolas(self):
        import sqlite3
        kapcsolat = sqlite3.connect("dolgozok.db")
        ab = kapcsolat.cursor()
        ab.execute('CREATE TABLE IF NOT EXISTS dolgozok(nev TEXT, jelszo TEXT)')
        nev = self.felhasznalo_neve
        jelszo = self.felhasznalo_jelszava
        ab.execute('INSERT INTO dolgozok (nev, jelszo) VALUES (?, ?)', (nev, jelszo))
        kapcsolat.commit()
        kapcsolat.close()

    def felhasznalo_ell(self):
        # vagy egy jelszót ad vissza vagy False
        pass
    
# Főprogram
dolgozo = Felhasznalo()
# dolgozo.jelszo_generalasa()
# dolgozo.felhasznalonev()
print(dolgozo.felhasznalo_neve)
print(dolgozo.felhasznalo_jelszava)
dolgozo.tarolas()
