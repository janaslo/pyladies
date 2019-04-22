
teploty = [23.4, 22.3, 26.6, 52.0, 22.4]

# přidej na konec seznamu teplot hodnotu 23.3
teploty.append(23.3)

# přidej na konec další dvě libovolné číselné hodnoty
teploty.extend([22.4, 19.9])

# vypiš celý seznam teplot, jeho délku a minimální, maximální a průměrnou teplotu
print(teploty)
print('délka:', len(teploty))
print('minimum a maximum:', min(teploty), max(teploty))

prumer = sum(teploty)/len(teploty)
print('průměr:', prumer)
print('průměr: {:.2f}'.format(prumer))  # formátování: jen 2 čísla za desetinnou čárkou

# do seznamu teplot se vloudil překlep - 52.0 má být správně 25.0
# oprav tuto chybu (pomocí Pythonu a měnění seznamu;)
chybny_index = teploty.index(52.0)
teploty[chybny_index] = 25.0


# odstraň ze seznamu hodnotu 22.3
teploty.remove(22.3)

# odstraň ze seznamu třetí hodnotu
del teploty[2]
print('teploty:', teploty)

# vytvoř nový seznam, kde budou teploty seřazené podle velikosti
serazene = sorted(teploty)
print('serazene:', serazene)

# vytvoř nový seznam, kde budou všechny teploty zmenšené o 2 stupně
zmensene = []
for teplota in teploty:
    zmensene.append(teplota - 2)
print('zmensene:', zmensene)

# postupně (pomocí while cyklu) vyprázdni seznam teplot, odstraň vždy
# poslední hodnotu a vypiš ji na obrazovku
while teploty:
    print(teploty.pop())
