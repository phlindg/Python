from panel import *
from vind import *
import tkinter as tk
import sys

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
                return
            elif valet == 2:
                danmark = Vind(rotor_dm_input())
                print("Utvunnen energi för rotordiametern", danmark.rotor_dm, ": ", danmark.genomsnitt())
                return
            else:
                continue
        except ValueError:
            continue

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
def pyvar_test():
    t = [1, 2, 3, 4, 5]
    s = [2, 8, 4, 1, 6]
    pylab.plot(t, s)

    pylab.show()
def avsluta():
    while True:
        try:
            print("1: Ja")
            print("2: Nej")
            valet = int(input("Vill du välja ännu en gång? ja eller nej: "))
        except ValueError:
            print("Du måste skriva 1 eller 2")
            continue
        if valet == 2:
            print("Tack för denna gång!")
            break
        elif valet == 1:
            val()

if __name__ == "__main__":
#    pyvar_test()
    val()
    #rita()
    avsluta()


