# Grafische Rekenmachine - GUI met Tkinter en Matplotlib

Welkom bij mijn Python-project waarin ik een grafische rekenmachine heb gemaakt met behulp van Tkinter en Matplotlib. Dit project werd ontwikkeld voor mijn onderzoekscompetentie. De rekenmachine laat je zowel standaard wiskundige berekeningen uit voeren als grafieken te visualiseren van functies als de programmeurs instelling te gebruiken.

## Bestanden

- **startscherm.py**  
  Dit bestand opent het startscherm van de applicatie. Het is het eerste venster dat verschijnt bij het opstarten van het programma.

- **hoofdscherm.py**  
  Dit is het hoofdscherm van de rekenmachine. Hierin bevindt zich de standaard rekenmachine, de grafische rekenmachine en de programmeurversie. Er is ook een menukolom voorzien waarin de gebruiker kan wisselen tussen de verschillende soorten rekenmachines.

- **grafiek.py**  
  Dit bestand wordt opgeroepen wanneer de gebruiker in de grafische rekenmachine op "PLOT" drukt. De ingevoerde functies worden geplot met Matplotlib. Extra functies zoals het berekenen van nulpunten, het opvragen van een y-waarde voor een bepaalde x-waarde, het bepalen van snijpunten en het leegmaken van de grafiek zijn inbegrepen.

- **placeholder.py**
  Dit bestand bevat mijn eigen functie dat in Entry's waar gebruikers input kunnen geven een backgroundtekst wordt weergegeven. 

## Functionaliteiten

-  Standaard rekenmachine met +, -, ×, ÷, √ en machtsverheffing
-  Grafieken tekenen op basis van functies 
-  Interactieve analyse: nulpunten, y-waarden, snijpunten tussen functies
-  Programmeur-rekenmachine voor binaire en decimale conversies

## Installatie

1. Zorg ervoor dat Python is geïnstalleerd.
2. Installeer de nodige packages met pip:
   - tkinter
   - numpy
   - matplotlib
   - sympy
