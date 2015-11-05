from panel import *
if __name__ == "__main__":

    def latitud_input():
        try:
            latitud = int(input("Ange en latitud: "))
        except ValueError:
            latitud = int(input("Oj, försök igen: "))
        return latitud

  

    spanien = Panel(450, 7, latitud_input())
    spanien.spara()
