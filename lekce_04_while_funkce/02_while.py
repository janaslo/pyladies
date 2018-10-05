
odpoved = input('Řekni heslo: ')

while odpoved != '123':         # pokud platí podmínka mezi while a dvojtečkou ...
    print('To není správně.')   # ... provede se odsazený blok pod while
    odpoved = input('Řekni heslo: ')

print('Správně, konec programu.')    # (až) pokud podmínka neplatí, program jede dál
