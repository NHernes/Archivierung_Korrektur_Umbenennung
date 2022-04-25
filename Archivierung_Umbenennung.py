import fitz  # this is pymupdf
from os import walk
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox
import time

#Aufbau Fenster
root = tk.Tk()
root.title('Umbenennung Archivdateien')
root.geometry("1100x400")

#GUI Design
S = Scrollbar(root)

#Hauptfenster
T = Text(root, height=4, width=100)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

#Seitenfenster
Side = Text(root, height=4, width=25)
Side.pack(side=TOP)
Side.config(state=NORMAL)


#Datei-Picker
path0=askdirectory()

####Beginn der eigentlichen Operation###

#Erfassen der bestehenden Ordner
ordner = []
for (dirpath, dirnames, filenames) in walk(path0):
    ordner.extend(dirnames)
    break

#Variable für die Ausgabe der veränderten Datei
zähler_datei=0
zähler_ordner=0

#Hochzählen zur Iteration der Ordner-Liste
x=-1

#Initieren der Tracking-Variablen für die Ersetzung mit Bindestrichen
fach_bindestrich=False
lizenz_bindestrich=False

#Liste der in den jeweiligen Ordnern vorliegenden Dateien
datei=[]
for i in ordner:
    x=x+1
    zähler_ordner=zähler_ordner+1
    #Variable zum Durchlaufen der Dateien in einem Ordner
    walker=-1

    #Konstruktion des Pfadnamens des Ordners
    path1=path0+"/"+ordner[x]
    
    for (dirpath, dirnames, filenames) in walk(path1):
        
        for i in filenames:
            
            zähler_datei=zähler_datei+1
            walker=walker+1
            #Konstruktion des Pfadnamens der Datei
            path2=path1+"/"+filenames[walker]

            #Einlesen der PDF-Inhalte
            with fitz.open(path2) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()

                #Trennen des eingelesenen Texts in eine Liste
                text=text.split()


                ############### Extraktion Name ###############
                #Extraktion des Indexes für Geburtsdatum und Teilnehmer, da zwischen diesen Indexen der Name der Kandidat:innen angeordnet ist
                geburtsdatum_liste = [i for i, s in enumerate(text) if 'Geburtsdatum:' in s]
                teilnehmer_liste = [i for i, s in enumerate(text) if 'Teilnehmer:' in s]

                #Berechnung der zwischen den beiden Randindexen befindlichen Listeneinträge, dies ist der Name der Person
                #Die Range muss daher definiert werden, damit auch längere Namen korrekt eingelesen werden
                differenz1=(teilnehmer_liste[0]-geburtsdatum_liste[0])-1

                hochzählen=0

                #tracking_index wird initialisiert, um die Indexe zwischen den Randindexen zu berechnen
                tracking_index=int(geburtsdatum_liste[0])

                name=""

                #Hier wird über alle Indexe zwischen den beiden Randindexen iteriert und die darin befindlichen Items dem Namen angehangen
                while hochzählen < differenz1:
                    tracking_index=tracking_index+1
                    hochzählen=hochzählen+1
                    name=name+"_"+text[tracking_index]
                    #Komma wird aus dem Namen entfernt
                    name=name.replace(",","")


                ############### Extraktion Fachname ###############
                #Extraktion des Indexes für Ergebnis und Fach, da zwischen den ersten Indexen der Fächername angeordnet ist
                ergebnis_liste = [i for i, s in enumerate(text) if 'Ergebnis:' in s]
                fach_liste = [i for i, s in enumerate(text) if 'Fach:' in s]


                #Berechnung der zwischen den beiden Randindexen befindlichen Listeneinträge, dies ist der Fächername
                #Die Range muss daher definiert werden, damit auch längere Fächernamen korrekt eingelesen werden
                differenz2=(fach_liste[0]-ergebnis_liste[0])-1

                hochzählen=0

                #tracking_index wird initialisiert, um die Indexe zwischen den Randindexen zu berechnen
                tracking_index=int(ergebnis_liste[0])

                fach=""

                #Hier wird über alle Indexe zwischen den beiden Randindexen iteriert und die darin befindlichen Items dem Fächernamen angehangen
                while hochzählen < differenz2:
                    tracking_index=tracking_index+1
                    hochzählen=hochzählen+1
                    fach=fach+"_"+text[tracking_index]

                    #Um die Dateien trotz Fächern mit Slash im Namen umzubenennen, werden diese hier mit einem Bindestrich ersetzt
                    if "/" in fach:
                        fach= fach.replace("/","-")
                        fach_bindestrich=True
                    

                ############### Extraktion Matrikelnummer ###############
                #Die Matrikelnummer befindet sich im Login, dieser wird immer nach der zweiten Erscheinung des Items "Geburtsdatum:" geschrieben
                #Daher wird hier der Index aller Iterationen von "Geburtsdatum:" gebildet
                liste_matrikelnummer = [i for i, s in enumerate(text) if 'Geburtsdatum:' in s]

                #Hier wird der Index des Items nach der zweiten Iteration von "Geburtsdatum:" definiert, welcher den Login enthält
                Matrikelnummer=text[liste_matrikelnummer[1]+1]

                #Da die Matrikelnummer in unserem Login ist, werden alle restlichen Bestandteile des Logins entfernt, diese sind mit "-" getrennt, welcher daher als Markierung dient
                sep="-"
                while sep in Matrikelnummer:
                    Matrikelnummer=Matrikelnummer[1:]


                ############### Extraktion Lizenzname ###############           
                #Extraktion des Indexes für Fach und Lizenz, da zwischen den ersten Indexen der Lizenzname angeordnet ist
                fach_liste = [i for i, s in enumerate(text) if 'Fach:' in s]
                lizenz_liste = [i for i, s in enumerate(text) if 'Lizenz:' in s]


                #Berechnung der zwischen den beiden Randindexen befindlichen Listeneinträge, dies ist der Lizenzname
                #Die Range muss daher definiert werden, damit auch längere Lizenznamen korrekt eingelesen werden
                differenz3=(lizenz_liste[0]-fach_liste[0])-1

                hochzählen=0

                #tracking_index wird initialisiert, um die Indexe zwischen den Randindexen zu berechnen
                tracking_index=int(fach_liste[0])

                lizenz=""

                #Hier wird über alle Indexe zwischen den beiden Randindexen iteriert und die darin befindlichen Items dem Lizenznamen angehangen
                while hochzählen < differenz3:
                    tracking_index=tracking_index+1
                    hochzählen=hochzählen+1
                    lizenz=lizenz+"_"+text[tracking_index]
                    lizenz=lizenz[1:]

                    #Um die Ordner trotz Fächern mit Slash im Namen umzubenennen, werden diese hier mit einem Bindestrich ersetzt
                    if "/" in lizenz:
                        lizenz=lizenz.replace("/","-")
                        lizenz_bindestrich=True


                ############### Generierung der Strings zur Umbenennung ###############
                #Hier wird der String zur Umbenennung der Datei gebildet
                string=Matrikelnummer+name+fach+".pdf"

                #Hier wird der Pfad zur umzubennenden Datei gebildet
                path_file_new=path1+"/"+string

                #Hier wird der Pfad zum umzubennenden Ordner gebildet
                ordner_neu=path0+"/"+Matrikelnummer+name+lizenz

            #Umbenennung der Datei und des Ordners    
            os.rename(path2, path_file_new)
            
            
            #Ausgabe der umbenannten Datei im Textfeld Hauptfeld
            T.insert(INSERT,filenames[walker]+"\n   ----->   "+ string +"\n\n")
            T.update()
            
            #Ausgabe des Index der umbenannten Datei im Textfeld Seitenfeld
            Side.delete(1.0, END)
            Side.insert(INSERT,"Datei Nr. "+ str(zähler_datei)+" umbenannt\n")
            Side.update()

            #Ausgabe der Iteration
            print("Datei Nr. " + str(zähler_datei) +" aktualisiert")

        os.rename(path1, ordner_neu)

        #Ausgabe des umbenannten Ordners im Textfeld Hauptfeld
        T.insert(END, ordner[x]+"\n   ----->   "+ Matrikelnummer+name+"_"+lizenz +"\n\n")
        T.update()
        T.see(END)

        #Ausgabe des Index des umbenannten Ordners im Textfeld Seitenfeld   
        Side.insert(INSERT,"Ordner Nr. "+ str(zähler_ordner)+" umbenannt")
        Side.update()

#Ausgabe der Zusammenfassung
T.insert(END, "---------------------------------\n"
"Umbenennung erfolgreich \n\n"
"Es wurden "+str(zähler_datei)+" Dateien umbenannt\n"
"Es wurden "+str(zähler_ordner) +" Ordner umbenannt")

#Ausgabe der Ersetzung mit Bindestrichen, falls aufgetreten
if fach_bindestrich==True:
    T.insert(END, "\n\nACHTUNG: Im Dateinamen wurden Schrägstriche mit Bindestrichen ersetzt") 

if lizenz_bindestrich==True:
    T.insert(END, "\nACHTUNG: Im Ordnernamen wurden Schrägstriche mit Bindestrichen ersetzt") 

T.update()

#Konstanter Sprung des Textfeldes an das Feldende Hauptfeld
T.see(END)

#Popup Dialog mit der Zusammenfassung
info = messagebox.showinfo('Zusammenfassung', "Umbenennung erfolgreich \n\n"
"Es wurden "+str(zähler_datei)+" Dateien umbenannt\n"
"Es wurden "+str(zähler_ordner) +" Ordner umbenannt", parent=root)

root.protocol("WM_DELETE_WINDOW", quit)
root.mainloop(  )   