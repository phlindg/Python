from tv import *


if __name__ == "__main__":
    textfil = open("textfil.txt", "r")

    rader = textfil.readlines()
   #här vill jag ha att man ska välja tv osv.
    n = True
    print("*** Välkommen till TV simulatorn ***")
    while n:
	    print("1. Vardagsrums TV")
	    print("2. Köks TV")
	    print("3. Avsluta")
	    try:
		    val_1 = int(input("Välj: "))
	    except ValueError:
	        print("En siffra mellan 1-3 ")
	        val_1 = int(input("Välj igen: "))
	    if val_1 == 1:
	        kanal = rader[2]
	        volym = rader[3]
	        vardagsrum = TV(kanal, volym)
	        print("1. Byt Kanal")
	        print("2. Sänk ljudvolym")
	        print("3. Höj ljudvolym")
	        print("4. Gå till huvudvolym")
	        val_2 = int(input("Välj 2: "))
	        if val_2 == 1:
	            ny_kanal = int(input("Välj kanal: "))
	            rader[2] = ny_kanal
	        if val_2 == 2:
	            vardagsrum.sank_volym()
	            rader[3] = int(volym)
	        if val_2 == 3:
	            print("1: ", volym)
	            vardagsrum.hoj_volym()
	            rader[3] = int(volym)
	            print("2: ", volym)

	        if val_2 == 4:
	            val_1 == int(input("välj sista: "))
	    elif val_1 == 2:
	        kanal = rader[5]
	        volym = rader[6]
	        kok = TV(kanal, volym)
	        print("1. Byt Kanal")
	        print("2. Sänk ljudvolym")
	        print("3. Höj ljudvolym")
	        print("4. Gå till huvudprogram")
	        val_2 = int(input("Välj 2: "))
	        while val_2 != 4:
		        if val_2 == 1:
		            ny_kanal = int(input("Välj kanal: "))
		            rader[5] = ny_kanal
		            val_2 = int(input("Välj 2 igen: "))
		        if val_2 == 2:
		            kok.sank_volym()
		            rader[6] = int(volym)
		            val_2 = int(input("Välj 2 igen: "))
		        if val_2 == 3:
		            kok.hoj_volym()
		            rader[6] = int(volym)
		            val_2 = int(input("Välj 2 igen: "))
		        if val_2 == 4:
		            print("huvudmeny")
		        
	    elif val_1 == 3:
	        n = False
	        textfil.close()
	        textfil = open("textfil.txt", "w")
	        rader.reverse()
	        for i in range(len(rader)):
	        	rad = str(rader.pop())
	        	textfil.write(rad)
	        #textfil.write(rader)
	        textfil.close()
	    else:
	        print("En siffra mellan 1-3")
