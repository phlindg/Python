import random

class Vind:
    def __init__(self, rotor_dm):
        self.rotor_dm = rotor_dm

    def energi(self, dag):
        if dag > 1 and dag <= 90 and dag > 180 and dag < 360:
            vind = 15
        else:
            vind = 12
        energi = vind * self.rotor_dm
        return energi
    def genomsnitt(self):
        dag_list =  list(range(1,361))
        total = 0
        for dag in dag_list:
            total += self.energi(dag)
        g = total/360
        return g
