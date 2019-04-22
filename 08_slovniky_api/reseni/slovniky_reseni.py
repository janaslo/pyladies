
narozeniny = {
    'Hanka': '20.03.',
    'Petr': '05.05.',
    'Jitka': '20.03.',
    'Adam': '15.11.',
}

# přidej do slovníku další podobnou položku
narozeniny['Jana'] = '14.03.'

# přidej do slovníku ještě další dvě položky najednou
narozeniny.update({'Pavel': '12.12.', 'Jirka': '10.10.'})
# nebo
narozeniny.update(Eva='09.11.', Lenka='30.06.')

# vypiš seřazený seznam jmen obsažených ve slovníku
print('seznam jmen:', sorted(narozeniny))

# můžeme použít i metodu keys, ale není to nutné, protože Python u slovníků
# vždy pracuje primárně s klíči (i při procházení slovníku for cyklem,
# hledání prvků operátorem in atd.)
print('seznam jmen:', sorted(narozeniny.keys()))


# pro všechny položky vypiš věty typu: Hanka má narozeniny 20.03.
for polozka in narozeniny.items():
    print(polozka[0], 'má narozeniny', polozka[1])
# nebo
for jmeno, datum in narozeniny.items():
    print('{} má narozeniny {}'.format(jmeno, datum))
# nebo
for jmeno in narozeniny:
    print(jmeno, 'má narozeniny', narozeniny[jmeno])

print('-' * 20)

# vymaž Adama
del narozeniny['Adam']

# vypiš, kdy mají narozeniny: Petr, Adam
# pokud se jméno ve slovníku nenachází, vypiš "nenalezeno"
for osoba in ('Petr', 'Adam'):
    if osoba in narozeniny:
        print(osoba, 'má narozeniny', narozeniny[osoba])
    else:
        print(osoba, '- nenalezeno')


# na závěr si vytiskni současnou podobu slovníku
print(narozeniny)

# ulož slovník s narozeninami do souboru narozeniny.json
import json
with open('narozeniny.json', 'w') as soubor:
    json.dump(narozeniny, soubor, indent=2)


# BONUS
# vytvoř ze stávajího slovníku nový "obrácený" slovník,
# kde klíčem bude vždy datum a hodnotou seznam jmen
# (tj. počítej s tím, že jich může být u jednoho data více)
narozeniny_opacne = {}  # prázdný slovník, který postupně naplníme
for jmeno, datum in narozeniny.items():
    if datum in narozeniny_opacne:  # datum tam už je -> stačí přidat jméno
        narozeniny_opacne[datum].append(jmeno)
    else:   # vytvoříme novou položku, hodnotou je seznam obsahující první jméno
        narozeniny_opacne[datum] = [jmeno]
print('obrácený slovník:', narozeniny_opacne)
