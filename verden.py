from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        #lager et tomt rutenett i en instansvariabel
        self._rutenett = Rutenett(rader, kolonner)
        #setter den nulte generasjonen
        self._generasjonsnummer = 0
        #fyller det tomme rutenettet med celler, levende eller døde
        self._rutenett.fyll_med_tilfeldige_celler()
        #kobler sammen cellene slik at de får naboene sine
        self._rutenett.koble_celler()

    def tegn(self):
        #skriver ut alt infoen i terminalen. Rutenettet, generasjonsnummer og antall levende celler
        self._rutenett.tegn_rutenett()
        print("Generasjon: ", self._generasjonsnummer)
        print("Antall levende celler igjen: ", self._rutenett.antall_levende())

    def oppdatering(self):

        #lager en liste med alle cellene
        alle_cellene = self._rutenett.hent_alle_celler()
        for celle in alle_cellene:
            #går alle cellene, slik at de får antall levende naboer
            celle.tell_levende_naboer()

        for celle in alle_cellene:
            #går igjen gjennom alle cellene, og oppdaterer deres status
            celle.oppdater_status()
        
        #øker generasjonsnummeret med 1
        self._generasjonsnummer += 1             