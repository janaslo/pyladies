
import json
import requests

# základní URL pro Svátky API
# lze použít parametry date (ve formátu DDMM) nebo name
# další popis viz http://svatky.adresa.info
SVATKY_URL = 'http://svatky.adresa.info/json'


# vypiš, kdo má dnes svátek

# posíláme požadavek na server; jeho odpověď se uloží do proměnné odpoved
odpoved = requests.get(SVATKY_URL)
# řetězec, který nám server vrátil:
print("vrácený řetězec:", odpoved.text)
# si pomocí modulu json převedeme na datovou strukturu Pythonu,
# kterou můžeme dále zpracovávat (zde seznam slovníků)
vysledek1 = json.loads(odpoved.text)
# nebo pro nás tento krok může udělat přímo modul requests
vysledek2 = odpoved.json()
# výsledek je stejný:
print(vysledek1 == vysledek2)
# a teď už jen získáme jméno z prvního slovníku v seznamu
jmeno = vysledek2[0]['name']
print('Dnes má svátek', jmeno)


# kdy má svátek Adam?

# params je slovník parametrů, které by v adrese byly za otazníkem
# zde např.: http://svatky.adresa.info/json?name=Adam
odpoved = requests.get(SVATKY_URL, params={'name': 'Adam'})
# můžeme si zkontrolovat, že modul requests sestavil adresu správně:
print('URL:', odpoved.url)
datum = odpoved.json()[0]['date']
# rozdělíme si datum ve formátu DDMM na části
den, mesic = datum[:2], datum[2:]
print('Adam má svátek {}.{}.'.format(den, mesic))

# BONUS
# uprav výpis tak, aby byl správný a úplný i pro dny, kdy má svátek více lidí
# např. 29.6. - Petr a Pavel

# přetvoř výpisy do vlastních funkcí, které budou vracet příslušný výsledek,
# tak aby pak stačilo volat např. najdi_jmeno(datum) nebo najdi_datum(jmeno)


# funkce jsem uložila do samostatného modulu ve stejném adresáři
from svatky_api import zjisti_jmena, zjisti_data

# ukázka jejich použití
print(zjisti_jmena())
print(zjisti_jmena(den=29, mesic=6))

print(zjisti_data('Jan'))
print(zjisti_data('Petr'))
print(zjisti_data('Harry'))     # pro neznámé jméno vrací prázdný seznam

# a ukázka výpisu
data = [(1, 9), (1, 10), (1, 12)]
for datum in data:
    den, mesic = datum
    jmena = zjisti_jmena(den, mesic)
    print('Dne {}.{}. má svátek: {}'.format(den, mesic, ', '.join(jmena)))
