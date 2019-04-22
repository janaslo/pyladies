
def opakuj_hlasku(hlaska, kolikrat=3):
    for opakovani in range(kolikrat):
        print(hlaska)


# parametry se do funkce predavaji ve stejnem poradi jako v jeji definici
opakuj_hlasku('ahoj', 4)

# pokud jsou v jinem poradi, musime rict, ktery je ktery
opakuj_hlasku(kolikrat=5, hlaska='no nazdar')

# parametr kolikrat ma v definici vychozi hodnotu 3, takze ho nemusime zadavat
# hlaska se v tom pripade vytiskne 3x
opakuj_hlasku('cau pyladies')

# ale tohle uz fungovat nebude, nejakou hlasku zadat musime
opakuj_hlasku()
