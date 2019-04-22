
from random import randrange
from turtle import *

def nakresli_zahradku(pocet_kytek=3):
    """Vykreslí zahrádku složenou z kytek, které mají náhodně vybrané
    vlastnosti.
    """
    posun = 300                                 # mezera mezi kytkami 
    x, y = -(pocet_kytek//2 * posun) , -250     # vychozi pozice vlevo dole 

    # kresleni kytek
    for k in range(pocet_kytek):        
        nastav_zelvu(x, y)
        nakresli_nahodnou_kytku()
        x += posun 

    # dokresleni zeme
    nastav_zelvu(x-posun/2, y)          
    left(90)
    forward(posun * pocet_kytek)

def nakresli_nahodnou_kytku():  
    """Náhodně vybere parametry kytky a pak ji vykreslí."""

    kvet_pocet_stran = randrange(3, 13)
    kvet_kolikrat = randrange(5, 21)
    pocet_pater_listu = randrange(2, 5)
    zdvih_listu = randrange(0, 50)
    stopka_listu = randrange(0, 20)

    nakresli_kytku(
        kvet_pocet_stran,
        kvet_kolikrat,
        pocet_pater_listu,
        zdvih_listu,
        stopka_listu
    )

def nakresli_kytku(kvet_pocet_stran, kvet_kolikrat,
        pocet_pater_listu, zdvih_listu, stopka_listu): 
    """Vykreslí celou kytku: stonek s lístky (odspodu) a květ.

    Parametry viz popis funkcí nakresli_stonek_listy a kvet.
    """
    nakresli_stonek_listy(pocet_pater_listu, zdvih_listu, stopka_listu)
    nakresli_kvet(kvet_pocet_stran, kvet_kolikrat)

def nakresli_kvet(pocet_stran, kolikrat):
    """Vykreslí květ složený z několika pootočených mnohoúhelníků.
    
    Parametry:
        pocet_stran: počet stran mnohoúhelníku
        kolikrat: z kolika mnohoúhelníků bude květ složen
    """
    for uhelnik in range(kolikrat):
        for strana in range(pocet_stran):   # n-uhelnik
            forward(200/pocet_stran)
            left(360/pocet_stran)
        left(360/kolikrat)      # otoceni

def nakresli_stonek_listy(pocet_pater, zdvih_listu=0, stopka=0):
    """Vykreslí odspodu stonek s lístky, které se postupně zmenšují.

    Parametry:
        pocet_pater: kolik pater (= dvojic) listů bude kytka mít
        zdvih_listu: úhel, o který jsou listy pootočeny od vodorovné polohy
        stopka: délka stopky listů
    """
    forward(50)
    for patro in range(pocet_pater, 0, -1): # od nejvetsiho k nejmensimu
        for smer in right, left:
            smer(90 - zdvih_listu)
            nakresli_listek(patro, stopka)
            smer(90 + zdvih_listu)
            forward(10 * patro)
    forward(100) 

def nakresli_listek(velikost=1, stopka=0):
    """Vykreslí jeden lístek, želva vychází ven v jeho ose.
    
    Parametry:
        velikost: malé celé číslo, cca 1-5
        stopka: délka stopky
    """
    forward(stopka * velikost)
    right(45)
    for strana in range(2):
        for krok in range(30):
            forward(velikost)
            left(3)
        left(90)
    right(135)
    forward(stopka * velikost)

def nastav_zelvu(x, y):
    """Pomocná funkce, nastaví želvu na zadané souřadnice a hlavou nahoru."""
    penup()
    setpos(x, y)
    setheading(90)
    pendown()


# az tady se spusti kresleni
shape('turtle')
speed('fastest')
nakresli_zahradku()
exitonclick()
