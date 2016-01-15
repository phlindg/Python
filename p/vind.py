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

    
