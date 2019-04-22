
# pocitac si vylosuje nahodne cislo a uzivatel jej pak ma uhodnout,
# pocitac mu napovida, kterym smerem posunout svuj odhad

from random import randrange

horni_mez = 101
cislo = randrange(horni_mez)
#print(cislo)        # jen pro testovaci ucely! :)

print('Hadej cislo od nuly do', horni_mez-1)

while True:
    tip = int(input('Tvuj tip? '))  # pozor, vstup je potreba prevest na int
    if tip > cislo:                 # protoze nelze takto porovnavat str a int
        print('To je moc! Uber.')
    elif tip < cislo:
        print('To je malo! Pridej.')
    else:       # kdyz neni mensi ani vetsi, tak to musi byt ono
        print('Spravne!')
        break
    
