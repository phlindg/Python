"""
Att göra en egen modul är precis det jag gjort med tv classen.


"""
class Bil(object):
    def __init__(self, marke, ar, stolar, harTut):
        self.marke = marke
        self.ar = ar
        self.stolar = stolar
        self. harTut = harTut
#Det en __str__ gör är någt man gör för att få ut en sträng, annars skulle man ha behövt skriva print(b.function) på rad 20.
    def __str__(self):
        tut = "Nej"
        if self.harTut:
            tut="Ja"
        return "Märke: "+ self.marke+ " Årsmodel: "+str(self.ar)+ " Antal Bilstolar: "+str(self.stolar)+ " Har tut: "+tut

b = Bil("Volvo", 2015, 5, True)

"""
För att deklarera om en metod är privat eller inte använderm an sig av __namn__
t.ex. __init__ är privat

"""
import math
class Ellips:
    def __init__(self,a,b):
        self.lang = a
        self.kort = b

    def area(self):
        return math.pi*self.lang*self.kort

class Cirkel(Ellips):
    def __init__(self,r):
        super(Cirkel, self).__init__(r,r)

    def omrets(self):
        return 2 * math.pi * self.lang

c = Cirkel(10)
print(c.omrets())
print(c.area())
