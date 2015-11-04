"""
Grafisk användargränssnitt
Med tkinter

Användargränssnitt = den ytan användaren kan komma åt.
Det finns också nått som heter teknikergränssnitt, de e typ ett admin system.

Widgets som finns i tkinter
Button
Canvas
Checkbutton
entry = <input>
frame = den är som <div>
label = samma som html, beskrivande text framför entry
listbox = en lista av t.ex. text som man kan scrolla igenom
menu = typ olika tabs
message = som en label fast man kan skriva flera rader
radiobutton
scale = en scroll som går från 0-100
scrollbar = finns vid sidan av fönster för att kunna scrolla
text = samma som entry fast flera rader, <textarea>


"""
from tkinter import *

t = Tk()
t.geometry("300x800") #detta bestämmer storleken på fönstret


"""
Threads använder man i parallell-programmering
det använder man när man vill göra flera olika saker samtidigt

anledningen till att Button har t som första parameter är att det är i den t som den ska läggas.
"""
def wumwum(wum):#här kan man inte ha paramterar
    print(wum)#en lamdba funktion har inget namn, den kallas anonym.
    #tanken med den är att man ska skriva korta satser.
    #lamdba kör kroppen av funktionen, utan att kalla på själva funktionen.
"""
b = Button(t, text="click here!", command= lambda: wumwum("wumwum"))
b.pack()
duk = Canvas(t, bg="red", width=300, height = 800)
duk.create_rectangle(100,100, 150, 250, fill="yellow")
duk.create_line(10,40,100,100)
duk.pack()

t.mainloop()

"""

def check():
    print(var.get())
var = StringVar()
c = Checkbutton(
        t, text="Color image", variable=var, onvalue="RGB", offvalue="L", command=check
        )
c.pack()
t.mainloop()









