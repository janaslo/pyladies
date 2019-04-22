
def preved_uzly(rychlost_uzly):     # hlavicka funkce: def, nazev, vstupni parametry
    "Tato funkce prevadi rychlost v uzlech na km/h."    # strucny popis

    rychlost_kmh = rychlost_uzly * 1.852
    return rychlost_kmh             # navratova hodnota - co se dostane z funkce ven


def vypis_silu_vetru(rychlost_kmh): # tato funkce pouze vypisuje, nic nevraci
    "Tato funkce vypise, jak silny je vitr o zadane rychlosti (v km/h)."

    print('Zadana rychlost v km/h:', rychlost_kmh)
    if rychlost_kmh < 1:
        print('Vubec nefouka.')
    elif rychlost_kmh < 25:
        print('Trochu fouka.')
    elif rychlost_kmh < 65:
        print('To je ficak!')
    else:
        print('Vichrice!!')


# uz tohle je vlastne volani dvou funkci: int, input
vstup = int(input('Zadej rychlost vetru v uzlech: '))

vstup_kmh = preved_uzly(vstup)
vypis_silu_vetru(vstup_kmh)

# da se zkombinovat i na jednom radku:
vypis_silu_vetru(preved_uzly(vstup))


print(20 * '-')     # oddelovac :)
print('Ukazka vracenych hodnot:')
x = preved_uzly(5)
y = vypis_silu_vetru(x)
print('Prvni funkce vraci', x)  # cislo
print('Druha funkce vraci', y)  # None, protoze nevraci nic jineho prikazem return

