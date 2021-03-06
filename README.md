## Archivierung_Korrektur_Umbenennung
##
### Wenn Nutzung der .py:
Please install via win+r "cmd" (Eingabeaufforderung):
- py -m pip install fitz
- py -m pip install walk
- py -m pip install tkinter

## Programm zur Umbenennung der PDF-Dateien aus dem LPLUS Export auf Basis der Prüflingsdaten

### Problembeschreibung
Bei einem LPLUS Reportmappenexport werden die Prüflingsdaten in folgendem Format ausgegeben:

### Ordnername:
  Prüflingsname, Prüflingsvorname - LPLUS-ID
  
  Beispiel:
  Mustermann, Max - 12345
  
### Dokumentenname:
  Reportmappe_LPLUS-ID_Nachname_Vorname_Fächername_Versuch.pdf
  
  Beispiel:
  Reportmappe_1234_Mustermann_Max_Musterprüfung_Sommersemester_2022_Versuch_1.pdf
  
Gerade für Lehrende ist die Verwendung der LPLUS-ID verwirrend, da diese der Matrikelnummer ähnelt und daher der Grad der Verwechslung hoch ist.

### Lösung
Das Skript iteriert über alle Ordner und die darin enthaltenen Dateien. Dabei liest es die PDF-Dateien aus und generiert aus diesen eine neue Benennung der Ordner und Archiv-Dateien.

### Muster
### Ordnername:
  Matrikelnummer_Nachname_Vorname_Lizenzname
  
  Beispiel:
  1234_Mustermann_Max_Beispiellizenz
  
### Dokumentenname:
  Matrikelnummer_Nachname_Vorname_Fach.pdf
  
  Beispiel:
  1234_Mustermann_Max_Beispielfach.pdf

### Hinweise:
Damit Ordner und Dateien umbenannt werden können, werden mögliche Schrägstriche entfernt und mit Bindestrichen ersetzt
Beispiel: WiSe21/22 ---> WiSe21-22

Einige Pfade können sehr lang sein, daher empfiehlt es sich, die Zeichenbegrenzung von 260 für Pfade aufzuheben. Eine Anleitung findet sich unter: https://ekiwi-blog.de/22934/zu-lange-datei-und-pfadnamen-unter-windows/
