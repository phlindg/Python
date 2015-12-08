# W(t) = area * soltal * solighets faktor * f(t, latitud)
#area = solfångarens area
#soltal = proportionalitetskonstant, energi / ytenhet
#solighetsfaktor = slumpas mellan 0 till 1, ny för varje dag och latitud.
#f(t, latitud) Energifunktion, latituden avges av användaren, t varierar mellan 1 till 360 (dagar under ett år)
#standardavvikelsen kan ses som så:
#
import math
import random
from tkinter import *
class Panel:
    
    def __init__(self, area, soltal, latitud):
        self.area = area
        self.soltal = soltal
        self.solighetsfaktor = random.random()
        self.latitud = latitud
    
    def energifunktion(self, dag, latitud, error=""):
        v = (23.5 * math.sin((math.pi*(dag-80))/180) + 90 - latitud)/90
        if v > 0 and v < 1:
            return v**2
        elif v >= 1:
            return 1
        elif v <= 0:
            return 0
    
    def genomsnitt(self):
        dag_list = list(range(1,361))
        total = 0
        for dag in dag_list:
            self.solighetsfaktor = random.random()
            w = (self.area * self.soltal * self.solighetsfaktor * self.energifunktion(dag, self.latitud))
            total += w
        g = total/360
        return g

    def standardavvikelse(self):
        dag_list = list(range(1, 361))
        k = 0
        for dag in dag_list:
            self.solighetsfaktor = random.random()
            s = (self.area * self.soltal * self.solighetsfaktor * self.energifunktion(dag, self.latitud) - self.genomsnitt())**2
            k+=s
        sa = k/359
        return sa**(1/2)

    def riktig(self):
        netto = self.genomsnitt() - self.standardavvikelse()
        return netto

    def dag_for_dag(self, dag):
        self.solighetsfaktor = random.random()
        e = self.area * self.soltal * self.solighetsfaktor * self.energifunktion(dag, self.latitud)
        return round(e, 1)
    
    def rita(self):
        tk = Tk()

        
        b_vind = Button(tk, text="Vindkraftverk")
        b_sol = Button(tk, text="Solkraftverk!")
        
        text = Text(tk)
        tk.geometry("1200x600")
        tk.title("P-uppgift!!!!!!!!!!!") 
        text.pack()
        b_sol.pack()
        b_vind.pack()
        tk.mainloop()

    def spara(self):
        daglista = []
        try:
            textfil = open("daglista.txt", "w+")
            dag_list = list(range(1,31))
            månad_list = list(range(12))
            månads_namn = ["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "September", "Oktober", "November", "December"]
            textfil.read()
            for månad in månad_list:
                textfil.write("Area, soltal, latitud, dag, solighetsfaktor, f(t, latitud), W(t)"+ "\n")
                textfil.write("==========================================================="+"\n")
                textfil.write(månads_namn[månad] + "\n")
                for dag in dag_list:
                    textfil.write(str(self.area) + ", "+
                    str(self.soltal) + ", "+
                    str(self.latitud)+ ", "+
                    str(dag) +  ", "+
                    str(round(self.solighetsfaktor, 1))+ ", "+
                    str(round(self.energifunktion(dag + 30*månad, self.latitud), 3)) +  ", "+
                    str(self.dag_for_dag(dag + 30*månad))+"\n"
                    )
            textfil.read()
            textfil.close()
        except IOError:
            textfil = open("daglista.txt", "w+")
