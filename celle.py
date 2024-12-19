class Celle:
    # Konstruktør
    def __init__(self):
        #definerer instansvariablene
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0
    
    def sett_doed(self):
        #Foradrer statusen til denne cellen som "doed"
        self._status = "doed"

    def sett_levende(self):
        #Forandrer statusen til denne cellen som "levende"
        self._status = "levende"

    def er_levende(self):
        #returnerer True dersom cellen er levende, og False hvis ikke
        return self._status == "levende"

    def hent_status_tegn(self):
        #Returnerer symbol for om cellen er levende (O) eller død (.)
        if self._status == "levende":
            return "O"
        elif self._status == "doed":
            return "."

    def legg_til_nabo(self, nabo):
        #legger til en nabo fra parameteren til listen _naboer
        self._naboer.append(nabo)

    def tell_levende_naboer(self):
        teller = 0
        #går gjennom alle naboene, og teller opp en variabel for hver nabo som er levende
        for nabo in self._naboer:
            if nabo.er_levende():
                teller += 1
        #Forandrer instansvariabelen til antall levende celler fra variabelen "teller"
        self._ant_levende_naboer = teller

    def oppdater_status(self):
        if self._status == "levende":
            #Hvis statusen er levende så skjekker den om det er 2 eller 3 naboer
            #hvis det er dette fortsetter den og leve, ellers dør den
            if self._ant_levende_naboer > 1 and self._ant_levende_naboer < 4:
                self.sett_levende()
            else:
                self.sett_doed()
        
        elif self._status == "doed":
            #Setter cellen sin status til levende hvis det er nøyaktig 3 naboer
            if self._ant_levende_naboer == 3:
                self.sett_levende()
        

        