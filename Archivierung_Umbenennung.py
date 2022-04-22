import fitz  # this is pymupdf
from os import walk
import os
import tkinter as tk
from tkinter.filedialog import askdirectory

#Datei-Picker
path0=askdirectory()

#Erfassen der bestehenden Ordner
ordner = []
for (dirpath, dirnames, filenames) in walk(path0):
    ordner.extend(dirnames)
    break


####Beginn der eigentlichen Operation###

#Hochzählen zur Iteration der Ordner-Liste
x=-1

#Liste der in den jeweiligen Ordnern vorliegenden Dateien
datei=[]
for i in ordner:
    x=x+1
    #Konstruktion des Pfadnamens des Ordners
    path1=path0+"/"+ordner[x]

    for (dirpath, dirnames, filenames) in walk(path1):

        #Konstruktion des Pfadnamens der Datei
        path2=path1+"/"+filenames[0]

        #Einlesen der PDF-Inhalte
        with fitz.open(path2) as doc:
            text = ""
            for page in doc:
                text += page.get_text()

            #Trennen des eingelesenen Texts in eine Liste
            text=text.split()

            #Extraktion des Indexes für Geburtsdatum und Teilnehmer, da zwischen diesen Indexen der Name der Kandidat:innen angeordnet ist
            geburtsdatum_liste = [i for i, s in enumerate(text) if 'Geburtsdatum:' in s]
            teilnehmer_liste = [i for i, s in enumerate(text) if 'Teilnehmer:' in s]

            #Berechnung der zwischen den beiden Randindexen befindlichen Listeneinträge, dies ist der Name der Person
            #Die Range muss daher definiert werden, damit auch längere Namen korrekt eingelesen werden
            differenz=(teilnehmer_liste[0]-geburtsdatum_liste[0])-1

            hochzählen=0

            #tracking_index wird initialisiert, um die Indexe zwischen den Randindexen zu berechnen
            tracking_index=int(geburtsdatum_liste[0])

            name=""

            #Hier wird über alle Indexe zwischen den beiden Randindexen iteriert und die darin befindlichen Items dem Namen angehangen
            while hochzählen < differenz:
                tracking_index=tracking_index+1
                hochzählen=hochzählen+1
                name=name+"_"+text[tracking_index]
                #Komma wird aus dem Namen entfernt
                name=name.replace(",","")
            
            #Die Matrikelnummer befindet sich im Login, dieser wird immer nach der zweiten Erscheinung des Items "Geburtsdatum:" geschrieben
            #Daher wird hier der Index aller Iterationen von "Geburtsdatum:" gebildet
            liste_matrikelnummer = [i for i, s in enumerate(text) if 'Geburtsdatum:' in s]

            #Hier wird der Index des Items nach der zweiten Iteration von "Geburtsdatum:" definiert, welcher den Login enthält
            Matrikelnummer=text[liste_matrikelnummer[1]+1]

            #Da die Matrikelnummer in unserem Login ist, werden alle restlichen Bestandteile des Logins entfernt, diese sind mit "-" getrennt, welcher daher als Markierung dient
            sep="-"
            while sep in Matrikelnummer:
                Matrikelnummer=Matrikelnummer[1:]
            
            #Hier wird das Fach aus dem Gesamtindex gefiltert und aus den beiden Items zusammengefügt
            fach_liste = [i for i, s in enumerate(text) if 'Fach:' in s]
            p= fach_liste[0]
            fach=text[p+1]+" "+text[p+2]

            #Hier wird der String zur Umbenennung der Datei gebildet
            string=Matrikelnummer+name+"_"+fach+".pdf"

            #Hier wird der Pfad zur umzubennenden Datei gebildet
            path_file_new=path1+"/"+string

            #Hier wird der Pfad zum umzubennenden Ordner gebildet
            ordner_neu=path0+"/"+Matrikelnummer+name

        #Umbenennung der Datei und des Ordners    
        os.rename(path2, path_file_new)
        os.rename(path1, ordner_neu)

        #Ausgabe der Iteration
        print("Datei Nr. " + str(x) +" aktualisiert")