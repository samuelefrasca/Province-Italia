# I file del CONVERTITORE SARDEGNA 1 non danno i csv in ordine alfabetico e con i codici comune corretti, quindi
#   questo file si occupa di sistemare questo problema

import csv
import os
import glob

mappa_codici = {}

# Qui ho rimesso latin1 per leggere correttamente il file ISTAT
with open("elenco_comuni.csv", mode="r", encoding="latin1") as f_elenco:
    lettore_elenco = csv.reader(f_elenco, delimiter=";")
    next(lettore_elenco) 
    
    for riga in lettore_elenco:
        codice_regione = riga[0]
        if codice_regione == "20":
            nome_comune = riga[6].strip().lower()
            nuovo_codice = riga[4] 
            mappa_codici[nome_comune] = nuovo_codice

cartella_province = "nuove_province"
file_csv = glob.glob(os.path.join(cartella_province, "*.csv"))

for file in file_csv:
    dati_corretti = []
    
    # I file che abbiamo creato noi prima sono in utf-8, quindi qui va bene
    with open(file, mode="r", encoding="utf-8") as f_in:
        lettore = csv.DictReader(f_in)
        campi = lettore.fieldnames
        
        for riga in lettore:
            nome_attuale = riga["Comune"].strip().lower()
            
            if nome_attuale in mappa_codici:
                riga["Codice comune"] = mappa_codici[nome_attuale]
            
            dati_corretti.append(riga)
    
    dati_corretti = sorted(dati_corretti, key=lambda x: x["Comune"])
    
    with open(file, mode="w", encoding="utf-8", newline="") as f_out:
        scrittore = csv.DictWriter(f_out, fieldnames=campi)
        scrittore.writeheader()
        scrittore.writerows(dati_corretti)

print("Fatto! File aggiornati con i nuovi codici e riordinati alfabeticamente.")