# CONVERTITORE DA CSV A JSON creato da Gemini
# Per utilizzarlo, i csv che hanno il nome della provincia con dominio .csv devono trovarsi nella cartella Download del computer
# I file csv verranno salvati nel percorso data e nella cartella col nome della regione corretta

import csv
import json
import os

provincia = input("Inserisci il nome della provincia: ")
sigla = input("Inserisci la sigla della provincia: ").upper()
regione = input("Inserisci il nome della regione: ")

nome_file_provincia = provincia.lower().replace(" ", "-").replace("'", "-")
cartella_regione = regione.lower().replace(" ", "-").replace("'", "-")

file_csv = f"{nome_file_provincia}.csv"

cartella_download = os.path.join(os.path.expanduser("~"), "Downloads")
percorso_completo_csv = os.path.join(cartella_download, file_csv)

risultato = []

with open(percorso_completo_csv, mode='r', encoding='utf-8') as f_csv:
    lettore = csv.DictReader(f_csv)
    
    for riga in lettore:
        risultato.append({
            "codice_istat": riga["Codice comune"],
            "comune": riga["Comune"],
            "provincia": provincia,
            "sigla": sigla,
            "regione": regione,
            "popolazione_maschile": int(riga["Totale maschi"]),
            "popolazione_femminile": int(riga["Totale femmine"]),
            "popolazione_totale": int(riga["Totale"])
        })

percorso_file = os.path.join("..", "data", cartella_regione, f"{nome_file_provincia}.json")

with open(percorso_file, mode='w', encoding='utf-8') as f_json:
    json.dump(risultato, f_json, indent=2, ensure_ascii=False)

print(f"Operazione completata! Creato il file in {percorso_file}")