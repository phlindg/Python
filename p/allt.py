

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
    def genomsnitt(self):
        dag_list = list(range(1,361))
        total = 0
        for dag in dag_list:
            self.solighetsfaktor = random.random() 
            e_dag = (self.area * self.soltal * self.solighetsfaktor * self.energifunktion(dag, self.latitud))
            total += e_dag  
        snitt = total/360
        return snitt
    #Denna funktion skapar en standardavvikelse bereonde av funktionen genomsnitt och energifunktion.
    def standardavvikelse(self):
        dag_list = list(range(1, 361))
        total = 0
        for dag in dag_list:
            self.solighetsfaktor = random.random()
            s_dag = (self.area * self.soltal * self.solighetsfaktor * self.energifunktion(dag, self.latitud) - self.genomsnitt(self.latitud))**2
            total += s_dag
        snitt = total/359 
        return snitt**(1/2)
    #denna raknar ut nettot av energin genom att ta differensen av funktionerna genomsnitt och standardavvikelse
    def netto_funktion(self): 
        netto = self.genomsnitt(self.latitud) - self.standardavvikelse()
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

import random

class Vind:
    #Denna körs när man inialiserar klassen vind.
    def __init__(self, rotor_dm):
        self.rotor_dm = rotor_dm

    #Denna funktion räknar ut vind beroende på dag
    def vindfunktion(self, dag):
        if dag > 1 and dag <= 90 or dag > 180 and dag < 360: 
            vind = 15
        else:
            vind = 12 
        return vind

    #denna tar värdet av funktion vindfunktion och delar på antal dagar
    def genomsnitt(self, rotor_dm):
        dag_list =  list(range(1,361))
        total = 0
        for dag in dag_list:
            energi = self.vindfunktion(dag) * rotor_dm
            total += energi
        g = total/360
        return g

    
from panel import *
from vind import *
import tkinter as tk
import sys


#Denna funktion tar värdet av en input som man får av användaren och använder som latitud.
def latitud_input():
    while True:
        try:
            latitud = int(input("Ange den latitud där du avser att placera solkraftverket. Latituden måste vara mellan 1 och 90. Klicka sedan på enter: "))
            if latitud >= 0 and latitud <= 90:  
                return latitud
            else:
                print("Du måste skriva en siffra mellan 1-90")
                continue 
        except ValueError:
            print("Du måste skriva en siffra mellan 1-90.")
            continue

#Denna funtkion tar värdet av en input på rotor diametern som man får av användaren.
def rotor_dm_input():
    while True:
        try:
            rotor_dm = int(input("Ange en rotor diameter mellan 25 och 50. Klicka sedan på enter: ")) 
            if rotor_dm >= 25 and rotor_dm <= 50: 
                return rotor_dm
            else:
                print("Du måste skriva en siffra mellan 25-50")
                continue
        except ValueError:
            print("Du måste skriva en siffra mellan 25-50")
            continue
#Den här funktionnen kollar om användaren vill välja ytterligare data, alltså fler latituder eller rotor diametrar.
#Om de vill det så returnar den True och respektive input funktion körs igen. Annars returnerar den false och programmet går vidare.
def en_till_input():
    print("1. Ja")
    print("2. Nej")
    while True:
        try:
            en_till = int(input("Vill du välja ytterligare data? Välj 1 eller 2 och klicka sedan på enter."))
            if en_till == 2:
                return False
            if en_till == 1:
                return True
            else:
                print("Du måste välja en siffra mellan 1 och 2.")
                continue
        except ValueError:
            print("Du måste välja en siffra mellan 1 och 2.")
            continue
#Denna funktion innehåller nästan som en sammanfattning av hela programmet. 
#Den låter användaren välja vilken typ av kraftverk den vill använda, och skriver sedan ut värdet för de parametrar som valts.
#Samt så sparar den värderna för solkraft ner till en fil.
def val():
    print("Vilken typ av kraftverk vill du välja? Klicka på enter när du har gjort ditt val.")
    print("1: Solkraftverk") 
    print("2: Vindkraftverk")
    while True:
        try:
            valet = int(input("Klicka 1 eller 2 for att valja solkraftverk respektive vindkraftverk. Klicka sedan på enter: "))
            if valet == 1:
                latitud_lista = []
                igen = True
                while igen:
                    spanien = Panel(450, 7, latitud_input()) 
                    latitud_lista.append(spanien.latitud)
                    latitud_lista.sort()
                    igen = en_till_input()
                i = 0
                for lat in latitud_lista:
                    print("Utvunnen energi for latituden", latitud_lista[i], ": ", round(spanien.genomsnitt(latitud_lista[i]), 2), "kW")
                    i += 1
                spanien.spara()
                return
            elif valet == 2:
                rotor_dm_lista = []
                igen = True
                while igen:
                    danmark = Vind(rotor_dm_input())
                    rotor_dm_lista.append(danmark.rotor_dm)
                    rotor_dm_lista.sort()
                    igen = en_till_input()
                i = 0
                for dm in rotor_dm_lista:
                    print("Utvunnen energi for rotordiametern", rotor_dm_lista[i], ": ", round(danmark.genomsnitt(rotor_dm_lista[i]), 2), " kW")
                    i += 1
                return
            else:
                print("Du maste valja 1 eller 2")
                continue
        except ValueError:
            print("Du maste valja 1 eller 2")
            continue
#SKALL INTE GRANSKAS, EJ REDOVISNING FÖR A
def rita():
    root = tk.Tk()
    root.title("hejsan")
    data = [20, 15, 10, 7, 5, 4, 3, 2, 1, 1 ,0]
    C_WIDTH = 600
    C_HEIGHT = 400
    c = tk.Canvas(root, width=C_WIDTH, height=C_HEIGHT, bg="white")
    c.pack()

    y_streck = 15

    y_mellanrum = 20

    x_streck = 20
    x_width = 20

    x_mellanrum = 20
    
    for x, y in enumerate(data):
        x0 = x * x_streck + x * x_width + x_mellanrum
        y0 = C_HEIGHT - (y * y_streck + y_mellanrum)
        x1 = x * x_streck + x * x_width + x_width + x_mellanrum
        y1 = C_HEIGHT - y_mellanrum
        #rita rektangeln
        c.create_rectangle(x0, y0, x1, y1, fill="red")
        
        
        
        
        
        
        
        root.mainloop()
        #SKALL INTE GRANSKAS, EJ REDOVISNING FÖR A
def pyvar_test():
    t = [1, 2, 3, 4, 5]
    s = [2, 8, 4, 1, 6]
    pylab.plot(t, s)

    pylab.show()

#Denna funktion frågar användaren om den vill avsluta eller köra igen.
def avsluta():
    while True:
        try:
            print("1: Ja")
            print("2: Nej")
            valet = int(input("Vill du köra programmet en gång till? Tyck 1 eller 2 för att välja, tryck sedan på enter.")) 
        except ValueError:
            print("Du maste skriva 1 eller 2")
            continue
        if valet == 2:
            print("Tack for denna gang!")
            break
        elif valet == 1:
            val()
        else:
            print("Du måste välja mellan 1 och 2.")
            continue


def printfkn():
    print("Hej, välkommen till mitt program.")
    print("Här får du välja mellan 2 olika kraftverk, sedan knappa in lite data")
    print("Sen kommer du få en massa schysst information om hur mycket energi de utvinner för just din data.")
    print()

#huvudprogrammet, allt börjar här.
if __name__ == "__main__":
#    pyvar_test()
    
    printfkn()



    #Detta är det första som häneder, användaren får välja vilket kraftverk osv, se kommentarerna över funktionnen val().
    val()
    #rita()

    #Efter att funktionen val har kört så kallas funktionen avsluta(). Då kan man avsluta eller köra igen.
    avsluta()


