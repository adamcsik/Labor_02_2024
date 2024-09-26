# Számológép a négy alapműveletre
#import Lab_04_modul

from Lab_04_modul import eredmenyek_megjelenitese, adatok_bekerese, muveletek_vegrehajtasa

# Főprogram
adatok = adatok_bekerese()
muvelet_eredmenye = muveletek_vegrehajtasa(adatok[0], adatok[1], adatok[2])
eredmenyek_megjelenitese(adatok[0], adatok[1], adatok[2], muvelet_eredmenye)
