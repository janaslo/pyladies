
heslo = input('Zadej heslo: ')

while heslo != 'pyladies':          # pokud je splnena podminka (heslo neni pyladies), 
    print('To neni spravne.')       # program vstoupi do cyklu
    heslo = input('Zadej heslo: ')  # odsud se vraci na zacatek ke kontrole podminky

print('Spravne!')   # pokud podminka neplati, program pokracuje dal


print('A jeste jednou: ')

# druha varianta while
while True:                 # tato podminka plati vzdy
    heslo = input('Zadej znovu heslo: ')
    if heslo == 'pyladies':
        print('Spravne!')
        break               # takze nekde musi byt cesta ven z cyklu
    print('To neni dobre.')

print('Konec programu.')

