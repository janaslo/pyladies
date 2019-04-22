
import requests

# základní adresa pro Svátky API
SVATKY_URL = 'http://svatky.adresa.info/json'


def zjisti_jmena(den=None, mesic=None):
    """Funkce, která zjistí, kdo má svátek v určitý den.

    Přijímá nepovinné parametry den a mesic, které mohou být celá čísla nebo
    řetězce. Pokud nejsou uvedeny, zjistí svátek pro aktuální den.

    Vrací seznam jmen.
    """
    if den and mesic:   # TODO zkontrolovat jejich hodnoty
        # doplnění nulami do formátu DDMM
        # jiný způsob např.: datum = str(den).zfill(2) + str(mesic).zfill(2)
        datum = '{0:0>2}{1:0>2}'.format(den, mesic)
        odpoved = requests.get(SVATKY_URL, params={'date': datum})
    else:   # bez zadaného dne a měsíce vrátí dnešní svátek
        odpoved = requests.get(SVATKY_URL)

    # kontrola, jestli server nevrátil chybový kód
    odpoved.raise_for_status()

    jmena = []
    for slovnik in odpoved.json():
        jmena.append(slovnik['name'])

    return jmena


def zjisti_data(jmeno):
    """Tato funkce určí, na které datum připadá svátek.

    Přijímá povinný parametr jmeno (řetězec)
    a vrací seznam dvojic čísel (den, měsíc).
    """
    odpoved = requests.get(SVATKY_URL, params={'name': jmeno})
    odpoved.raise_for_status()

    data = []
    for slovnik in odpoved.json():
        datum = slovnik['date']
        # převedeme datum na dvojici čísel (den, měsíc) - není nutné
        datum_prevedene = int(datum[:2]), int(datum[2:])
        data.append(datum_prevedene)

    return data
