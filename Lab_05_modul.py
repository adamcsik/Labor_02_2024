def felhasznalonev():
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
    return _felhasznalo_neve


def jelszo_bekerese(hosszusag):
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
    return jelszo
