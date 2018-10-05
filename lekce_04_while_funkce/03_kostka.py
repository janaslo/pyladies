
from random import randrange

pocet_hodu = 0  # sem budeme ukládat, kolikrát jsme házeli

while True:     # platí stále => z cyklu musíme někde vyskočit pomocí break
    kostka = randrange(1,7)     # simulace hodu kostkou, vrací čísla 1 - 6
    print(kostka)               # co nám padlo
    pocet_hodu += 1             # nebo: pocet_hodu = pocet_hodu + 1
    if kostka == 6:             # když padne šestka, končíme
        break

print('Počet hodů:', pocet_hodu)
