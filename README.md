# DKB_to_GnuCash
Ich hatte folgendes Probleme beim Transfer von DKB Kontoumsätzen (CSV Download aus dem Online Banking) in GnuCash.

*Informationen die zu automatischen Erkennung der Kathegorie einer Überweisung benötigt werden, sind in unterschiedlichen spalten.*

Das Skript kopiert die Informationen aus dem Online Banking Export wie folgt in eine neue CSV Datei:

Wertstellung                                    -> Datum

Buchungstext + Auftraggeber + Verwendungszweck  -> Beschreibung

Betrag                                          -> Betrag

## Voraussetzung
Python 3.7

## Aufruf

*python3 BankingImport.py 123456789.csv*
