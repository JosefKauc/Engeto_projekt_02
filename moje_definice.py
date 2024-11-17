import random

# definice funkcí

# Úvodní pozdrav
def pozdrav():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)


def generuj_cislo():

    cislo_PC = []
    cislo_PC.append(random.randint(1,9))    # první pozice z budoucího čísla nesmí začínat 0, proto náhodné číslo 1-9
    
    pocet_cislic = 1                # pomocna promenna pro pocitani cislic (mají být presně 4)      
    
    while pocet_cislic < 4:
        nahodna_cislice = random.randint(0,9)   # vygeneruj náhodnou cislici od 0 - 9
        if nahodna_cislice in cislo_PC:         # pokud je číslo již v seznamu jdi na začátek cyklu
            continue
        else:
            cislo_PC.append(nahodna_cislice)    # přiřaď do seznamu vygenerovanou číslici
            pocet_cislic += 1                   # navyš počítadlo počtu číslic
    
    # převod na řetězec
    cislo_PC_retezec = "" 
    for i in range(0,4):
        cislo_PC_retezec = cislo_PC_retezec + str(cislo_PC[i])

    return cislo_PC_retezec


def nacti_cislo_hrace():
    
    hotovo = False

    while not hotovo:
    
        cislo_hrace = input("Enter a number:")          # zadání čísla (řetezce!) od hráče

        if (len(cislo_hrace) != 4):
            print("Please enter a FOUR-digit number (no repetitions).")
            continue                                    # na začátek while cyklu

        elif not cislo_hrace.isdigit():
            print("Please enter a four-DIGIT number (digits only and no repetitions).")
            continue                                    # na začátek while cyklu

        elif (len(cislo_hrace) == 4) and cislo_hrace.isdigit():

            if cislo_hrace[0] == "0":
                print("Please enter a number NOT starting with a ZERO.")
                continue                                # na začátek while cyklu
            
            for i in cislo_hrace:
                pocet = cislo_hrace.count(i)   # zjisti počet výskytu číslice
                if pocet > 1:
                    print("Please enter a four-digit number WITHOUT REPETITION.")
                    break           # přeruší for cyklus
            
            if pocet > 1:
                continue            # na začátek while cyklu
            else:
                hotovo = True       # máme číslo od hráče, splňující podmínky

    return cislo_hrace              # cislo hrace je string o čtyřech číslicich!
    
def vyhodnot_cislo(cis_pocitac:str, cis_hrac:str) -> tuple:
    """
    Vstupem funkce jsou dva stringové parametry - čtyřmístné číslo počítače a hráče.

    Vyhodnocení probíhá přes vytvořené slovníky, obsahující jako klíče jednotlivé číslice 
    a jako hodnota daného klíče (tedy konkrétní číslice) je pozice číslice v zadaném stringu 

    Pro každou číslici hráče ověří zda je ve slovníku počítače a zjistí její pozici v obou slovnících.
    Porovnáním výsledku zjistí, zda pozice si jsou rovny, pak přičte hodnotu k bulls nebo si nejsou rovny, 
    pak přičte cows.

    Funkce Vrátí tuple o dvou hodnotách - na první pozici bude pocet trefených číslic na správnémmístě (bulls),
    na druhém místě počet trefených číslic, ale na jiných pozicích (cows)
    """
    
    slovnik_pocitac = dict()        # příprava slovníku pro znak a jeho pozici u čísla generovaného počítačem
    slovnik_hrac = dict()           # příprava slovníku pro znak a jeho pozici u čísla zadaného hráčem

    for p in cis_pocitac:                           # pro každý znak z cisla (řetězce) počítače
        slovnik_pocitac[p] = cis_pocitac.index(p)   # vytvoř slovník (číslice je klíč, hodnota je index - pozice v čísle)
    
    for h in cis_hrac:                              # pro každý znak z cisla (řetězce) hráče
        slovnik_hrac[h] = cis_hrac.index(h)         # vytvoř slovník (číslice je klíč, hodnota je index - pozice v čísle)
    """
    print(cis_pocitac)                              # pomocny prubezny tisk
    print(slovnik_pocitac)                          # pomocny prubezny tisk
    print(cis_hrac)                                 # pomocny prubezny tisk
    print(slovnik_hrac)                             # pomocny prubezny tisk
    """
    bulls = 0           # vynulovani počítadla pro každé vyhodnocení (bulls trefene císlo i pozice)
    cows = 0            # vynulovani počítadla pro každé vyhodnocení (cows trefene císlo ale ne pozice)

    for znak_hrac in slovnik_hrac:         # pro každou číslici ze slovníku hráče         
        
        if slovnik_pocitac.get(znak_hrac) in (0,1,2,3):  # jestliže číslice hráče je ve slovniku pocitače, pak ...

            pozice_znaku_ze_slovniku_hrace = slovnik_hrac.get(znak_hrac)
            pozice_znaku_hrace_ze_slovniku_pocitace = slovnik_pocitac.get(znak_hrac)
            """
            print("Ze slovniku počítače:", znak_hrac, pozice_znaku_hrace_ze_slovniku_pocitace) # pomocny prubezny tisk
            print("Ze slovniku hráče:",znak_hrac, pozice_znaku_ze_slovniku_hrace)              # pomocny prubezny tisk
            """
            if pozice_znaku_ze_slovniku_hrace == pozice_znaku_hrace_ze_slovniku_pocitace:
                bulls += 1
            else:
                cows += 1
           
    # print(bulls, "bulls", cows, "cows")         # pomocny tisk výsledku vyhodnoceni
              
    return (bulls, cows)

def vypis_vyhodnoceni(seznam:list):

    bulls = seznam[0]
    cows = seznam[1]

    if bulls > 1 and cows > 1:
        print(bulls, "bulls, ", cows, "cows")
    elif bulls > 1 and cows <= 1:
        print(bulls, "bulls, ", cows, "cow")
    elif bulls <= 1 and cows > 1:    
        print(bulls, "bull, ", cows, "cows")
    elif bulls <= 1 and cows <= 1:   
        print(bulls, "bull, ", cows, "cow")


 # fce preved_cas zpracována pouze do předpokladu maximálně 3600 s (tj.60 minut) na jednu hru 
def preved_cas(sekundy: float):      
    if sekundy <= 60:
        print("Time elapsed in this game: ", sekundy,"s")
    elif sekundy <= 3600:
        minuty = int(sekundy // 60)
        sekundy = int(abs((minuty - (sekundy / 60)) * 60))
        print("Time elapsed in this game: ", minuty,"m", sekundy,"s")
        

# tuto podmínkovou větev nyní při nahrávání knihovny nespustíš
if __name__ == "__main__":
    pozdrav()
    # print(generuj_cislo())
    # print(nacti_cislo_hrace())
    # print(vypis_vyhodnoceni(vyhodnot_cislo(generuj_cislo(), nacti_cislo_hrace())))
    # preved_cas(2750)  # test funkce s parametrem v sekundách
    
    