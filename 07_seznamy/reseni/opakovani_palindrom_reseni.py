
def je_palindrom(retezec):
    """Tato funkce zjistí, zda je vstupní řetězec palindrom
    (tj. čte se stejně zepředu i zezadu), a vrátí příslušnou
    logickou hodnotu (True/False).

    Funkce bere v úvahu pouze alfanumerické znaky, ignoruje
    velikost písmen a diakritiku.
    """
    # vstupní řetězec nejprve zbavíme zbytečností a zjednodušíme
    retezec = nech_jen_pismena_cisla(retezec)
    retezec = zmensi_pismena(retezec)
    retezec = odstran_diakritiku(retezec)
    # a konečně otestujeme
    return je_stejny_pozpatku(retezec)


def je_stejny_pozpatku(retezec):   # základ
    # jedna možnost; šlo by také např. postupně porovnávat krajní znaky
    return retezec == retezec[::-1]


def zmensi_pismena(retezec):    # pro druhou testovací skupinku
    return retezec.lower()


def nech_jen_pismena_cisla(retezec):  # pro třetí skupinku
    novy = ''
    for znak in retezec:
        if znak.isalnum():
            novy += znak
    return novy


def odstran_diakritiku(retezec):    # pro poslední testovací skupinu
    # varianta s překladovou tabulkou
    # sofistikovanější možnosti v modulech unicodedata, unidecode

    diakritika = 'áéíóúýěžščřďťň'
    nahrada =    'aeiouyezscrdtn'
    novy = ''
    for znak in retezec:    # nebo: použít metodu str.maketrans
        if znak in diakritika:
            index = diakritika.index(znak)
            novy += nahrada[index]
        else:
            novy += znak
    return novy


# Základní otestování funkce
palindromy_skupiny = [
    ("a", "aha", "abba", "radar"),  # pokud projdou tyto, vyvěs zelený lístek ;)
    ("Oto", "Anna", "Idol z lodi"),
    ("Jelenovi pivo nelej!", "Kuna nese nanuk.", "Báře jede jeřáb."),
    ("Kobyla má malý bok.", "V elipse spí lev.")    # pro experty
]

for skupina in palindromy_skupiny:
    for testovaci_retezec in skupina:
        if je_palindrom(testovaci_retezec):
            vysledek = 'OK'
        else:
            vysledek = 'ZATIM NE'
        print(vysledek, testovaci_retezec)
    print('-' * 30)

# Pro úplnost můžeš doplnit kód, který ověří, že funkce správně
# vrací False pro výrazy, které palindromy nejsou
for vyraz in ('Anča', 'korek'):
    if je_palindrom(vyraz):
        vysledek = 'CHYBA'
    else:
        vysledek = 'OK'
    print(vysledek, vyraz)
