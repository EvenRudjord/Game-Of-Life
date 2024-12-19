from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        #Definerer instansvariablene
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        #Definerer _rutenett til å være et rutenett av None
        self._rutenett = self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        #Lager en tom liste
        tomNett = []
        for i in range(self._ant_rader):
            #løkke som lager rutenett ut i fra brukens input om hvor mange rader som skal bli lagd
            #ved å hente mange rader
            tomNett.append(self._lag_tom_rad())
        #returnerer det tomme rutenettet
        return tomNett

    def _lag_tom_rad(self):
        #lager en tom rad
        rad = []
        for i in range(self._ant_kolonner):
            #legger rader til ut ifra hvor mange kolonner brukeren har sagt han vil ha
            rad.append(None)
        
        #returnerer en tom rad
        return rad

    def fyll_med_tilfeldige_celler(self):
        for x in range(self._ant_rader):
            for y in range(self._ant_kolonner):
                #Går gjennom alle elementene i det tomme rutenettet og gjør dem til celler
                self.lag_celle(x, y)

    def lag_celle(self, rad, kol):
        #lager en enkel celle
        cellen = Celle()
        #lager et tilfeldig tall fra og med 1, til og med 3
        randen = randint(1, 3)
        if randen == 1:
            #setter cellen til levende 1/3 sjanse
            cellen.sett_levende()
        
        #gjør det tomme, elementet (fra en spesifik rad og kolonne) til en celle, enten levende eller dø
        self._rutenett[rad][kol] = cellen
            

    def hent_celle(self, rad, kol):
        #henter en spesifik celle fra kolonne og rad
        if rad > self._ant_rader - 1 or rad < 0 or kol > self._ant_kolonner - 1 or kol < 0:
            #sjekker om kordinatene er utenfor eller innenfor rutenettet
            #returnerer None hvis cellen er utenfor
            return None
        else:
            #returnerer en celle inni rutenettet
            return self._rutenett[rad][kol]

    def tegn_rutenett(self):
        #Skriver ut 10 tomme linjer for å skille generasjonene
        for i in range(10):
            print("")
            
        for x in range(self._ant_rader):
            for y in range(self._ant_kolonner):
                #Går gjennom alle cellene og skriver ut et tegn ut fra deres status
                print(self.hent_celle(x, y).hent_status_tegn(), end="")
            print("\n", end="")

    def _sett_naboer(self, rad, kol):
        #lager en tom liste med naboer
        naboer = []
        #Får "offset" til cellen
        startRad = -1
        startKol = -1
        while startRad < 2:
            startKol = -1
            #går gjennom begge "offset" variablene får å dekke alle naboene
            while startKol < 2:              
                #lager en midlertidig celle variabel ut ifra "offset" som skal bli brukt til
                #å sjekke om cellen lever eller ikke
                tempCelle = self.hent_celle(rad + startRad, kol + startKol)
                if tempCelle != None and not(startRad == 0 and startKol == 0):
                    #sjekker at det får en ekte celle (at det ikke er utenfor rutenettet)
                    #sjekker også at det ikke er egen celle som blir lagt til som nabo
                    #legger så til en gyldig nabo
                    self.hent_celle(rad, kol).legg_til_nabo(tempCelle)
                    #øker "offsettet"
                startKol += 1
            startRad += 1

    def koble_celler(self):
        for x in range(self._ant_rader):
            for y in range(self._ant_kolonner):
                #Går gjennom alle celler i rutenettet, og gir dem deres naboer
                self._sett_naboer(x, y)

    def hent_alle_celler(self):
        #lager en tom liste
        alle_celler = []
        for x in range(self._ant_rader):
            for y in range(self._ant_kolonner):
                #går gjennom alle elementene i rutenettet
                #legger så til en celle til listen
                alle_celler.append(self.hent_celle(x,y))
        #returnerer en liste med alle cellene
        return alle_celler

    def antall_levende(self):
        #lager et start telle variabel som skal telle antall levende celler
        anttall_levende_celler = 0
        #lager en liste som har alle cellene
        alleCeller = self.hent_alle_celler()
        for celle in alleCeller:
            if celle.er_levende():
                #går gjennom alle cellene i listen
                #sjekker så om cellen er levende, og legger til 1 i antallet
                anttall_levende_celler += 1
        #returnerer et tall som sier hvor mange celler som er levende
        return anttall_levende_celler
