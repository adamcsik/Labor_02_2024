""" Ez az első
    labor, ahol kódot írunk
"""
print("Szia DUE!")      # output
print("Szia", "DUE!")
print("Szia", "DUE!", sep="----")
print("\nSzia", "\n\tDUE!", end="")

print('''Ez több
sorba kerül!''')

felhasznalo_neve = "Jenő"
felhasznalo_kora = 20

print("Szia", felhasznalo_neve, "!")
print(f"Szia {felhasznalo_neve}!")

print("\nNeve: \t{0} \nKor: \t{1}".format(felhasznalo_neve, felhasznalo_kora))

print(felhasznalo_neve.rjust(30, '.'))
print(str(felhasznalo_kora).rjust(30, '.'))

print(felhasznalo_neve.ljust(30, '.'))
print(str(felhasznalo_kora).ljust(30, '.'))

print(felhasznalo_neve.center(30, '.'))
print(str(felhasznalo_kora).center(30, '.'))

felhasznalo_neve = input("Hogy hívnak: ")
felhasznalo_kora = input("Hány éves vagy: ")
print("Szia", felhasznalo_neve)
print("Biztosan", felhasznalo_kora, "vagy? Nem", int(felhasznalo_kora) + 10, "?")
