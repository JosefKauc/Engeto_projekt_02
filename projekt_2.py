"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Josef Kauc
email: kauc@email.cz
discord: joska_82262
"""

# program pozdraví užitele a vypíše úvodní text  (viz. níže v ukázkách),

# program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)

# hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, 
# pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky,

# program vyhodnotí tip uživatele,

# program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), 
# příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). 
# Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. 
# Tedy 1 bull a 2 bulls (stejně pro cow/cows),

# zápis organizovaný do krátkých a přehledných funkcí.



# Úvodní text:
"""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
"""

# Příklad hry pro číslo 2017:
"""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
>>> 1234
0 bulls, 2 cows
-----------------------------------------------
>>> 6147
1 bull, 1 cow
-----------------------------------------------
>>> 2417
3 bulls, 0 cows
-----------------------------------------------
>>> 2017
Correct, you've guessed the right number
in 4 guesses!
-----------------------------------------------
That's amazing!
"""

# Program toho může umět víc. Můžeš přidat například:

# 1. počítání času, za jak dlouho uživatel uhádne tajné číslo
# 2. uchovávat statistiky počtu odhadů jednotlivých her

import moje_definice
import time

# generování náhodného čísla počítačem:
pocitac_cislo = moje_definice.generuj_cislo()

# pocitac_cislo = "3021"      # cislo natvrdo pro testovací účely
# print(pocitac_cislo)        # pomocny tisk

# Úvodní informace po startu programu:
moje_definice.pozdrav()

start_time = time.time()       # spuštění počítání času   
# print("The start time is", start_time)    # pomocné zobrazení času počítání

dohrano = False
pocitadlo_pokusu = 0

while not dohrano :
    # zadání čísla od hráče s kontrolou podmínek:
    hrac_cislo = moje_definice.nacti_cislo_hrace()
    vysledek = moje_definice.vyhodnot_cislo(pocitac_cislo, hrac_cislo)

    moje_definice.vypis_vyhodnoceni(vysledek)

    pocitadlo_pokusu += 1

    if vysledek[0] != 4:    # bulls není 4, tj. nejsou všechny číslice na spravne pozici
        continue
    else:
        dohrano = True


end_time = time.time()
# print("The end time is", end_time) # pomocné zobrazení času počítání

celkem_cas = end_time - start_time # celkový čas trvání hry v sekundách

moje_definice.preved_cas(celkem_cas)

print("Correct, you've guessed the right number\nin",pocitadlo_pokusu, "guesses!")
print("-" * 47)
print("That's amazing!")
