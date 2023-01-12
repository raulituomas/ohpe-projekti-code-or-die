
import sys
import os.path


#tarkistaa onko tiedosto luotu
file_exists = os.path.isfile("loadfile.txt")

#lataa txt tiedosto
def load():
    """Funktio lataa pelin tilan ja asettaa pelaajaan siihen huoneeseen mihin jäi"""
    
    if file_exists:
        file=open("loadfile.txt","r")
        room=file.read()
        file.close()	
    else:
        room="startroom"
    
    roomchooser (room)
    
#tallenna tiedosto
def save(s):
    """ tallennus funktio tallentaa huoneen tilan loadfile.txt tiedostoon"""
    
    file=open("loadfile.txt","w")
    file.write(s)
    file.close()
    
    
#asettaa pelaajan tallennettuun huoneeseen
def roomchooser(room):
    """roomchooser funktio asettaa pelaajan tallennettuun huoneeseen"""
    
    if room=="startroom":
        startroom()
    if room=="secondroom":
        secondroom()
    if room=="thirdroom":
        thirdroom()
    if room=="fourthroom":
        fourthroom()
    if room=="fifthroom":
        fifthroom()

# lisää itemeitä inventoryyn
def add_to_inventory(item):
    """lisää valitut esineet listaan"""
    
    inventory.append(item)
    
#tulostaa inventoryn
def print_inventory():
    """tulostaa inventoryn"""
    
    for i in inventory:
        print(i)
        
#default inventory
inventory =["boneworks3.exe","protrack2.pdf"]


#huoneet tai scenet 1-5

def startroom():
    """aloitushuone funktio joka antaa ohjeet käyttäjälle antaa oikeanlainen syöte"""
    print("______________________________________________")
    while True: 
        s="startroom"
        save(s)
        
        
        
        #tarina
        print("Tervetuloa")
        
        print("koodaa tai kuole peliin")
        print("Olet huoneessa nro 1")
        #ohjeet/tehtävä
        print("Mihin suuntaan haluat kulkea? ")
        print("vasen,oikea,alas,ylös? ")
        
       
        direction = input()
        if direction =="oikea":
            secondroom()   
                
        if direction =="vasen":
            print("LÖYSIT OIKOTIEN!!!")
            thirdroom()
            
        if direction =="alas":
            print("umpikuja")
            startroom()  
        
        if direction =="ylös":
            print("Väärä suunta")
            startroom()
        else:
            print("Annoit väärän arvon syötteeksi")
            print("Syötä joko vasen, oikea, ylös tai alas")
    
            
        
def secondroom():
    """aloitushuone funktio joka antaa ohjeet käyttäjälle antaa oikeanlainen syöte"""
    print("______________________________________________")
    while True:
        s="secondroom"
        save(s)
        
        
        #tarina
        print("Olet huoneessa nro 2")
        
        #ohjeet/tehtävä
        print("Mihin suuntaan haluat kulkea? ")
        print("vasen,oikea,ylös,alas? ")
        
        direction=input()
        if direction=="oikea":
            print("Pyörit ympyrää!!!")
            startroom()
            
        if direction=="ylös":
            print("Pyörit ympyrää!!!")
            startroom()
            
        if direction=="vasen":
            print("KUOLIT!!!")
            print("Palasit lähtöruutuun")
            startroom()
        
        if direction=="alas":
            print("Oikea suunta")
            thirdroom()
        else:
            print("Annoit väärän arvon syötteeksi")
            print("Syötä joko vasen, oikea, ylös tai alas")
        
        
def thirdroom():
    """tämä funktio tallentaa käyttäjän syötteen perusteella listaan löydetyn esineen"""
    print("______________________________________________")
    while True:
        s="thirdroom"
        save(s)
        
        
        #tarina
        print("Olet huoneessa nro 3")
        print("löydät tekemättömät tutoriaalitehtävät")
        #ohjeet/tehtävä
        print("Haluatko poimia tutoriaalitehtävät? k/e")
        pickup=input()
        
        if pickup=="k":
            print("Poimit tutoriaalin talteen")
            add_to_inventory("tutoriaali.py")
            fourthroom()
            
        if pickup =="e":
            print("Et poiminut tutoriaalia")
            secondroom()
        else:
            print("Anna syötteen arvoksi joko k tai e kirjain")

        

def fourthroom():
    """funktio asettaa pelaajan käyttäjän syötteen perusteella seuraavaan huoneeseen"""
    print("______________________________________________")
    while True:
        s="fourthroom"
        save(s)
        
        #tarina
        print("Olet huoneessa 4")
        print("Sinun pitäisi suorittaa exam tentti")
        #ohjeet/tehtävä
        print("Haluatko palauttaa tutoriaali tehtävät")
        print("k/e?")
        
        look=input()
        if look == "k":
            
            print("tässä on inventory")
            print("____________________________")
            print_inventory()
            print("____________________________")
            print("palautit tutoriaalitehtävät joten pääsit tenttiin")
            fifthroom()
            

        if look == "e":  
            print("et pääse tenttiin")
            print("aloita alusta")
            startroom()
        else:
            print("Anna syötteen arvoksi joko k tai e kirjain")

def fifthroom():
    """funktio päättää pelin jos käyttäjä on antanut oikean syötteen"""
    print("______________________________________________")
    while True:
        s="fifthroom"
        save(s)
        
        #tarina
        print("Olet huoneessa nro 5")
        #ohjeet/tehtävä
        print("Tenttikysymyksesi on seuraavanlainen")
        print("Mitä binääriluku 10010 on desimaalilukuna?")
        print("valitse seuraavista vaihtoehdoista a,b,c tai d")
        print("a:128, b:18, c:64, d:32")
        
        vastaus = input()
        if vastaus == "b":
            finish()
        else:
            print("Vastauksesi oli: ", vastaus)
            print("väärä vastaus palaat lähtöruutuun")
            startroom()
            
        
        
    
def finish():
    """funktio joka tulostaa lopputekstit"""
    print("Onneksi olkoon")
    
    print("Et kuollut joten koodasit")
    print("Haluatko aloittaa pelin alusta k/e?")
    
    syöte=input()
    if syöte == "k":
        startroom()
    else:
        sys.exit()


        

load()