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
