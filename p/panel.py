# W(t) = area * soltal * solighets faktor * f(t, latitud)
#area = solfangarens area
#soltal = proportionalitetskonstant, energi / ytenhet
#solighetsfaktor = slumpas mellan 0 till 1, ny for varje dag och latitud.
#f(t, latitud) Energifunktion, latituden avges av anvandaren, t varierar mellan 1 till 360 (dagar under ett ar)
#standardavvikelsen kan ses som sa:
#
import math
import random
class Panel:
    
    #denna funktion kors nar klassen initialiseras
    def __init__(self, area, soltal, latitud):
        self.area = area
        self.soltal = soltal
        self.solighetsfaktor = random.random()
        self.latitud = latitud
    #Denna funktion raknar ut energin beroende pa dag och latitud
    def energifunktion(self, dag, latitud):
        e = (23.5 * math.sin((math.pi*(dag-80))/180) + 90 - latitud)/90
        if e > 0 and e < 1:
            return e**2
        elif e >= 1:
            return 1
        elif e <= 0:
            return 0
    #Denna funktion tar informationen fran energifunktion och skapar ett genomsnitt enligt formeln given i uppg.
    def genomsnitt(self, lat):
        dag_list = list(range(1,361))
        total = 0
        for dag in dag_list:
            self.solighetsfaktor = random.random() #SÄTTER DU INTE DENNA LÄGST UPP?
            e_dag = (self.area * self.soltal * self.solighetsfaktor * self.energifunktion(dag, lat))
            total += e_dag  
        snitt = total/360
        return snitt
    #Denna funktion skapar en standardavvikelse bereonde av funktionen genomsnitt och energifunktion.
    def standardavvikelse(self):
        dag_list = list(range(1, 361))
        total = 0
        for dag in dag_list:
            self.solighetsfaktor = random.random()
            s_dag = (self.area * self.soltal * self.solighetsfaktor * self.energifunktion(dag, self.latitud) - self.genomsnitt())**2
            total += s_dag
        snitt = total/359 
        return snitt**(1/2)
    #denna raknar ut nettot av energin genom att ta differensen av funktionerna genomsnitt och standardavvikelse
    def netto_funktion(self): #OKLART VARIABELNAMN 
        netto = self.genomsnitt() - self.standardavvikelse()
        return netto
    #Denna funktion ger värdet för en dag
    def dag_for_dag(self, dag):
        self.solighetsfaktor = random.random()
        e = self.area * self.soltal * self.solighetsfaktor * self.energifunktion(dag, self.latitud)
        return round(e, 1)
    #Denna funktion sparar ner allting i tabellform till filen daglista
    def spara(self):
        daglista = []
        try:
            textfil = open("daglista.txt", "w+")
            dag_list = list(range(1,31))
            manad_list = list(range(12)) 
            manads_namn = ["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "September", "Oktober", "November", "December"]
            for manad in manad_list:
                textfil.write("Area, soltal, latitud, dag, solighetsfaktor, f(t, latitud), W(t)"+ "\n")
                textfil.write("==========================================================="+"\n")
                textfil.write(manads_namn[manad] + "\n")
                for dag in dag_list: 
                    textfil.write(str(self.area) + ", "+ \
                    str(self.soltal) + ", "+ \
                    str(self.latitud)+ ", "+ \
                    str(dag) +  ", "+ \
                    str(round(self.solighetsfaktor, 1))+ ", "+ \
                    str(round(self.energifunktion(dag + 30*manad, self.latitud), 3)) +  ", "+ \
                    str(self.dag_for_dag(dag + 30*manad))+"\n" \
                    )
            textfil.close()
        except IOError:
            textfil = open("daglista.txt", "w+")
