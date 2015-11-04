from main import *
class TV(object):
    def __init__(self, kanal, volym):
        self.kanal = kanal
        self.volym = volym
    def byt_kanal(self):
        pass

        
    def sank_volym(self):
        #Här ska en variabel som heter volym sänkas
       self.volym = int(self.volym)
       self.volym-=1
       return self.volym

    def hoj_volym(self):
        #Här ska en variabel som heter volym höjas.
       self.volym = int(self.volym)
       self. volym+=1
       return self.volym
   
    def menyer(self):
        pass
