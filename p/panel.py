# W(t) = area * soltal * solighets faktor * f(t, latitud)
#area = solfångarens area
#soltal = proportionalitetskonstant, energi / ytenhet
#solighetsfaktor = slumpas mellan 0 till 1, ny för varje dag och latitud.
#f(t, latitud) Energifunktion, latituden avges av användaren, t varierar mellan 1 till 360 (dagar under ett år)
#standardavvikelsen kan ses som så:
#
import math
import random
try:
    latitud = int(input("Ange latitud: "))
except ValueError:
    latitud = int(input("Försök igen: "))
def f(t, latitud, error=""):
    if latitud < 90 and latitud > 0:
        v = (23.5 * math.sin((math.pi*(t-80))/180) + 90 - latitud)/90
        if v > 0 and v < 1:
            return v**2
        elif v >= 1:
            return 1
        elif v <= 0:
            return 0
    else:
        error = "Ange en latitud mellan 0-90"
        return error

class Panel(object):
    
    def __init__(self, area, soltal):
        self.area = area
        self.soltal = soltal
        self.solighetsfaktor = random.random()
    
    def genomsnitt(self):
        t_list = list(range(361))
        k = 0
        for t in t_list:
            self.solighetsfaktor = random.random()
            try:
                w = (1/t)*(self.area * self.soltal * self.solighetsfaktor * f(t, latitud))
            except ZeroDivisionError:
                w = 0
            k += w
        g = k/360
        return g

    def standardavvikelse(self):
        t_list = list(range(361))
        for t in t_list:
            self.solighetsfaktor = random.random()
            try:
                s = ((1/(t-1)) * (self.area * self.soltal * self.solighetsfaktor * f(t, latitud) - self.genomsnitt()))**2
            except ZeroDivisionError:
                t=0
        return s**(1/2)

    def riktig(self):
        netto = self.genomsnitt() - self.standardavvikelse()
        return netto

    def dag_for_dag(self, t):
        self.solighetsfaktor = random.random()
        e = self.area * self.soltal * self.solighetsfaktor * f(t, latitud)
        return e
    
    

    def spara(self):
        daglista = []
        textfil = open("daglista.txt", "r+")
        day_list = list(range(31))
        month_list = list(range(12))
        month_names = ["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "September", "Oktober", "November", "December"]
        for month in month_list:
            textfil.write("Area, soltal, latitud, dag, solighetsfaktor, f(t, latitud), W(t)"+ "\n")
            textfil.write("==========================================================="+"\n")
            textfil.write(month_names[month] + "\n")
            for day in day_list:
                textfil.write(str(self.area) + ", "+
                str(self.soltal) + ", "+
                str(latitud)+ ", "+
                str(day) +  ", "+
                str(self.solighetsfaktor)+ ", "+
                str(f(day + 30*month, latitud)) +  ", "+
                str(self.dag_for_dag(day + 30*month))+"\n"
                )

        daglista = str(daglista)
        textfil.close()