class Jelszo:
    felhasznalo_jelszava = ""

    def __init__(self):
        self.felhasznalo_jelszava = ""

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


fjelszo = Jelszo()
print("Jelszavak")
print(fjelszo.felhasznalo_jelszava)
fjelszo.jelszo_generalasa()
print("Jelszógenerálás után")
print(fjelszo.felhasznalo_jelszava)


