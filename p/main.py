from panel import *
from vind import *
def latitud_input():
    while True:
        try:
            latitud = int(input("Ange en latitud: "))
            if latitud >= 0 and latitud <= 90:
                return latitud
            else:
                continue
        except ValueError:
            continue
def rotor_dm_input():
    while True:
        try:
            rotor_dm = int(input("Ange en rotor diameter: "))
            if rotor_dm >= 25 and rotor_dm <= 50:
                return rotor_dm
            else:
                continue
        except ValueError:
            continue
def val():
    print("Klicka på vad du vill välja")
    print("1: Solkraftverk")
    print("2: Vindkraftverk")
    while True:
        try:
            valet = int(input("Klicka 1 eller 2 för att välja: "))
            if valet == 1:
                spanien = Panel(450, 7, latitud_input())
                print("Utvunnen energi för latituden", spanien.latitud, ": ", spanien.genomsnitt())
                spanien.spara()
                spanien.rita()
                return
            elif valet == 2:
                danmark = Vind(rotor_dm_input())
                print("Utvunnen energi för rotordiametern", danmark.rotor_dm, ": ", danmark.genomsnitt())
                return
            else:
                continue
        except ValueError:
            continue

if __name__ == "__main__":
    val()
   #danmark = Vind(rotor_dm_input())
    #print(danmark.genomsnitt())

   # spanien = Panel(450, 7, latitud_input())
   # print("Utvunnen energi för latituden", spanien.latitud,": ",  spanien.genomsnitt())
   # spanien.spara()
