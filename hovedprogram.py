from verden import Verden

def hovedprogram():
    #Får brukerens input på hvor mange rader og kolonner det skal være
    #Gjør tallene om til int fra string
    rader = int(input("Hvor mange rader vil du ha: "))
    kolonner = int(input("Hvor mange kolonner vil du ha: "))

    #lager et objekt "verden"
    verden = Verden(rader, kolonner)
    #skriver ut all info til terminalen
    verden.tegn()

    #Ber brukeren om å gi en operasjon
    #"" fortsetter programmer, mens "q" avslutter det
    brukerInput = input("Tom input for å gå videre. Skriv q for å avslutte: ")

    while brukerInput == "":
        #Oppdaterer programmet om og om igjen fram til brukeren ikke skriver ""
        verden.oppdatering()
        verden.tegn()
        brukerInput = input("Tom input for å gå videre. Skriv q for å avslutte: ")

# starte hovedprogrammet
hovedprogram()