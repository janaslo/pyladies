
def je_palindrom(retezec):
    """Tato funkce zjistí, zda je vstupní řetězec palindrom 
    (tj. čte se stejně zepředu i zezadu), a vrátí příslušnou 
    logickou hodnotu (True/False).
    """
    pass    # nahraď svým kódem


# Základní otestování funkce
palindromy_skupiny = [
    ("aha", "abba", "radar"),  # pokud projdou tyto, vyvěs zelený lístek ;)
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
