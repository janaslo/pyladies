
def obvod_obdelniku(a, b):  # definice funkce
    "Tato funkce vrací obvod obdélníku o stranách a a b."
    obvod = 2 * (a + b)
    return obvod    # návratová hodnota - co se z funkce dostane ven jako výsledek

def obsah_obdelniku(a, b):
    "Tato funkce vrací obsah obdélníku o stranách a a b."
    obsah = a * b
    return obsah


x = 4   # definice proměnné
y = 5
z = 6

# až do tohoto místa se žádná funkce nespustila
# Python si pouze "zapamatoval" dvě nové funkce a tři proměnné

# a tady už funkci spustíme - tzv. zavoláme, a výsledek uložíme do proměnné
obsah_1 = obsah_obdelniku(5, 7)     # parametry mohou být přímo hodnoty - zde čísla
print(obsah_1)  # 35 

obsah_2 = obsah_obdelniku(x, y)     # nebo proměnné, ve kterých jsou hodnoty uložené
print(obsah_2)  # 20

kvadr = obsah_2 * z                 # s výsledkem můžeme dál pracovat    
print(kvadr)    # 120

# výpočet objemu kvádru lze zapsat i takto, bez ukládání mezivýsledku do proměnné
kvadr_jinak = obsah_obdelniku(x, y) * z
print(kvadr_jinak)  # 120

# stejně tak lze výsledek např. pouze vypsat
# pozor, aby byly správně uzavřeny všechny závorky :)
print(obvod_obdelniku(6, 7))    # 26
