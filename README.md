## Archivierung_Korrektur_Umbenennung
##
Please install via win+r "cmd" (Eingabeaufforderung):
- py -m pip install fitz
- py -m pip install walk

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
