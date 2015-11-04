"""
Klass, instans, metod och kontruktor

En klass är en mall för ett object t.ex. bil eller konto

Ett objekt är en instans av en klass, t.ex. den röda bilen, mitt lönekonto.


Definition av en klass
class Kurs(object):
    pass
skillnaden mellan pass och break är att pass körs under definitionen, alltså körs aldrig programmet. Break avslutar t.ex. loopen när den kommer till break.

Instansering
k1 = Kurs()
k1.bet = "prgi13"
print(k1.bet)
k2 = Kurs()
k2.bet = "datae12"
print(k2.bet)

Metod:
Metoer har samma syntax som funktion med den skillnadne att de definieras i en klass.
Tre metodtyper:
    Constructor
    Instansmetoder
    Klassmetoder
class Kurs(objceT):
    def antalStudenter(self):
        return self.antal

class Kurs(object):
    def __init__(self,b):
        self.bet = b
k1 = Kurs("prgi13") #detta kommer throwa ett error, den behöver b
print(k1) kommer att skriva ut "prgi13"
class Kurs(object):
    def __init__(self,b,n):
        self.bet=b
        self.n=namn
        self.antal=0
k1 = Kurs("prgi13", "tekniskt")
k1.antal #kommer att returna 0.



"""
