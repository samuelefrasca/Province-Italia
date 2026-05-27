# CONVERTITORE CSV per il caso speciale della Sardegna, che dal 2026 ha una nuova struttura delle province,
#   ma nel sito Istat non è aggiornato
# Mettere il csv con tutti i comuni d'italia aggiornato (istat ha aggiornato solo quello) nello stesso percorso di questo file,
#   e i csv delle vecchie 5 province in una cartella chiamata "vecchie-province", e questo script creerà una nuova
#   cartella chiamata nuove-province con i nuovi 8 csv

import csv
import os
import glob

mappa_province = {}

print("Fase 1: Leggo l'elenco dei comuni...")
with open("elenco_comuni.csv", mode="r", encoding="latin1") as f_elenco:
    lettore_elenco = csv.DictReader(f_elenco, delimiter=";")
    
    # Troviamo le colonne dinamicamente per evitare problemi di accenti o spazi strani
    col_reg = None
    col_nome = None
    col_prov = None
    
    for colonna in lettore_elenco.fieldnames:
        col_lower = colonna.lower()
        if "codice regione" in col_lower:
            col_reg = colonna
        elif "denominazione in italiano" in col_lower:
            col_nome = colonna
        elif "territoriale sovracomunale" in col_lower and "denominazione" in col_lower:
            col_prov = colonna

    for riga in lettore_elenco:
        if riga.get(col_reg) == "20":
            nome = riga[col_nome].strip().lower()
            # Rimuoviamo eventuali invii a capo nascosti nel nome della provincia
            provincia = riga[col_prov].replace("\n", "").strip()
            mappa_province[nome] = provincia

print(f"Comuni sardi trovati: {len(mappa_province)}")

nuovi_dati = {}
file_trovati = glob.glob("vecchie_province/*.csv")

print(f"Fase 2: Trovati {len(file_trovati)} file in 'vecchie_province'")

for file_csv in file_trovati:
    with open(file_csv, mode="r", encoding="latin1") as f_pop:
        lettore_pop = csv.DictReader(f_pop, delimiter=",")
        for riga in lettore_pop:
            nome_grezzo = riga.get("Comune")
            if nome_grezzo:
                nome_pop = nome_grezzo.strip().lower()
                if nome_pop in mappa_province:
                    prov_aggiornata = mappa_province[nome_pop]
                    if prov_aggiornata not in nuovi_dati:
                        nuovi_dati[prov_aggiornata] = []
                    
                    nuovi_dati[prov_aggiornata].append({
                        "Codice comune": riga["Codice comune"],
                        "Comune": riga["Comune"],
                        "Totale maschi": riga["Totale maschi"],
                        "Totale femmine": riga["Totale femmine"],
                        "Totale": riga["Totale"]
                    })

print(f"Fase 3: Comuni abbinati: {sum(len(lista) for lista in nuovi_dati.values())}")

os.makedirs("nuove_province", exist_ok=True)

for provincia, lista_comuni in nuovi_dati.items():
    nome_file = provincia.lower().replace(" ", "-").replace("'", "-") + ".csv"
    percorso = os.path.join("nuove_province", nome_file)
    
    with open(percorso, mode="w", encoding="utf-8", newline="") as f_out:
        campi = ["Codice comune", "Comune", "Totale maschi", "Totale femmine", "Totale"]
        scrittore = csv.DictWriter(f_out, fieldnames=campi)
        scrittore.writeheader()
        scrittore.writerows(lista_comuni)

print("Operazione conclusa con successo!")