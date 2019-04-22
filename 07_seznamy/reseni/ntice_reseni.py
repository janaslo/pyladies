
ovoce = "jahody", "maliny", "třešně", "meruňky"


# vypiš poslední dva druhy ovoce
print('poslední 2:', ovoce[-2:])

# zjisti (pomocí operátoru in), jestli se mezi ovocem nachází: maliny, švestky
# a pokud ano, vypiš jejich pozici (index), jinak vypiš "nenalezeno"
for hledane_ovoce in ('maliny', 'švestky'):
    print('hledám', hledane_ovoce)
    if hledane_ovoce in ovoce:
        print(hledane_ovoce, 'jsou na pozici', ovoce.index(hledane_ovoce))
else:
    print(hledane_ovoce, 'nenalezeny')


# vypiš očíslovaný seznam ovoce (ve tvaru: 1. jahody ...), použij funkci enumerate
for poradi, druh_ovoce in enumerate(ovoce, start=1):
    print('{}. {}'.format(poradi, druh_ovoce))




# BONUS
# vytvoř novou ntici obsahující čtyři jména a s pomocí funkce zip
# ji zkombinuj s ovocem a vypiš věty typu: "Adam má rád jahody", ...
jmena = 'Adam', 'Bohouš', 'Ctibor', 'David'

for jmeno, druh_ovoce in zip(jmena, ovoce):
    print('{} má rád {}'.format(jmeno, druh_ovoce))
