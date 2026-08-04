#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
genera_comuni.py
Genera il file comuni.html nella root del progetto.
Legge tutti i file JSON dei comuni da data/<regione>/<provincia>.json
e costruisce una tabella con colonne: Comune, Provincia, Regione, Popolazione.
Il JavaScript di ordinamento e ricerca è in un file esterno:
  assets/js/scriptElencoCompletoComuni.js
"""

import json
import os
import re
import unicodedata

# ---------------------------------------------------------------------------
# Mappa regione → slug cartella
# ---------------------------------------------------------------------------
REGIONE_SLUG = {
    "Abruzzo":              "abruzzo",
    "Basilicata":           "basilicata",
    "Calabria":             "calabria",
    "Campania":             "campania",
    "Emilia-Romagna":       "emilia-romagna",
    "Friuli-Venezia Giulia":"friuli-venezia-giulia",
    "Lazio":                "lazio",
    "Liguria":              "liguria",
    "Lombardia":            "lombardia",
    "Marche":               "marche",
    "Molise":               "molise",
    "Piemonte":             "piemonte",
    "Puglia":               "puglia",
    "Sardegna":             "sardegna",
    "Sicilia":              "sicilia",
    "Toscana":              "toscana",
    "Trentino-Alto Adige":  "trentino-alto-adige",
    "Umbria":               "umbria",
    "Valle d'Aosta":        "valle-d-aosta",
    "Veneto":               "veneto",
}

REGIONE_CAPOLUOGHI = {
    "Abruzzo": "L'Aquila",
    "Basilicata": "Potenza",
    "Calabria": "Catanzaro",
    "Campania": "Napoli",
    "Emilia-Romagna": "Bologna",
    "Friuli-Venezia Giulia": "Trieste",
    "Lazio": "Roma",
    "Liguria": "Genova",
    "Lombardia": "Milano",
    "Marche": "Ancona",
    "Molise": "Campobasso",
    "Piemonte": "Torino",
    "Puglia": "Bari",
    "Sardegna": "Cagliari",
    "Sicilia": "Palermo",
    "Toscana": "Firenze",
    "Trentino-Alto Adige": "Trento",
    "Umbria": "Perugia",
    "Valle d'Aosta": "Aosta",
    "Veneto": "Venezia",
}


def formatta_numero(n: int) -> str:
    """Formatta un numero con il separatore delle migliaia italiano (punto)."""
    return f"{n:,}".replace(",", ".")


def get_classi_riga(c: dict) -> list[str]:
    """Restituisce le classi CSS da applicare alla riga in base al ruolo del comune."""
    classi = []
    if c.get("capoluogo"):
        classi.append("capoluogo-provincia")
    if c.get("comune") and c.get("regione"):
        if c["comune"] == REGIONE_CAPOLUOGHI.get(c["regione"], ""):
            classi.append("capoluogo-regione")
    return classi


def carica_tutti_i_comuni() -> list[dict]:
    """
    Legge tutti i file JSON nelle sotto-cartelle di data/ e
    restituisce una lista di dict con chiavi: comune, provincia, regione, popolazione_totale.
    """
    tutti = []
    for regione, slug_regione in REGIONE_SLUG.items():
        cartella = os.path.join("data", slug_regione)
        if not os.path.isdir(cartella):
            print(f"  ATTENZIONE: cartella mancante {cartella}")
            continue
        for nome_file in sorted(os.listdir(cartella)):
            if not nome_file.endswith(".json"):
                continue
            percorso = os.path.join(cartella, nome_file)
            with open(percorso, encoding="utf-8") as f:
                comuni = json.load(f)
            for c in comuni:
                tutti.append({
                    "comune": c["comune"],
                    "provincia": c.get("provincia", ""),
                    "regione": c.get("regione", regione),
                    "popolazione_totale": c["popolazione_totale"],
                    "capoluogo": c.get("capoluogo", False),
                })
    # Ordina alfabeticamente per nome comune
    tutti.sort(key=lambda x: x["comune"].lower())
    return tutti


def slugify_testo(valore: str) -> str:
    """Converte un testo in uno slug adatto alle URL delle pagine del sito."""
    testo = unicodedata.normalize("NFKD", valore)
    testo = "".join(char for char in testo if not unicodedata.combining(char))
    testo = testo.lower()
    testo = re.sub(r"[^a-z0-9]+", "-", testo).strip("-")
    return testo


def get_slug_provincia(nome_provincia: str) -> str:
    """Restituisce lo slug della pagina della provincia."""
    return slugify_testo(nome_provincia)


def genera_righe_tabella(comuni: list[dict]) -> str:
    """Genera le righe HTML della tabella."""
    righe = []
    popolazione_totale = 0

    for i, c in enumerate(comuni, start=1):
        pop = c["popolazione_totale"]
        popolazione_totale += pop
        pop_str = formatta_numero(pop)

        classi = get_classi_riga(c)
        classi_attr = " ".join(classi) if classi else ""
        classe_cell = " capoluogo-provincia-cell" if "capoluogo-provincia" in classi else ""

        provincia = c["provincia"]
        regione = c["regione"]
        provincia_slug = get_slug_provincia(provincia) if provincia else ""
        regione_slug = REGIONE_SLUG.get(regione, slugify_testo(regione)) if regione else ""

        provincia_html = (
            f'<a class="comunihref" href="/province/{provincia_slug}.html">{provincia}</a>' if provincia_slug else provincia
        )
        regione_html = (
            f'<a class="comunihref" href="/regioni/{regione_slug}.html">{regione}</a>' if regione_slug else regione
        )

        righe.append(
            f'                    <tr class="{classi_attr}">'
            f'<td class="el index{classe_cell}">{i}</td>'
            f'<td class="el nome{classe_cell}">{c["comune"]}</td>'
            f'<td class="el provincia{classe_cell}">{provincia_html}</td>'
            f'<td class="el regione{classe_cell}">{regione_html}</td>'
            f'<td class="el abitanti{classe_cell}">{pop_str}</td>'
            f'</tr>'
        )

    # Riga totale
    righe.append(
        f'                    <tr>'
        f'<td class="index"></td>'
        f'<td class="fel nome"><strong>Popolazione totale</strong></td>'
        f'<td class="fel provincia"><strong></strong></td>'
        f'<td class="fel regione"><strong></strong></td>'
        f'<td class="fel abitanti"><strong>{formatta_numero(popolazione_totale)}</strong></td>'
        f'</tr>'
    )

    return "\n".join(righe)


# ---------------------------------------------------------------------------
# Navigazione SEO (copiata dagli altri generatori)
# ---------------------------------------------------------------------------
NAV_INVISIBILE = """\
        <nav class="nav-invisibile">
            <h3>Pagine Principali</h3>
            <ul>
                <li><a href="https://provinceitalia.it/">Home</a></li>
                <li><a href="https://provinceitalia.it/privacy">Privacy</a></li>
                <li><a href="https://provinceitalia.it/comuni">Comuni</a></li>
            </ul>

            <h3>Elenco Regioni</h3>
            <ul>
                <li><a href="https://provinceitalia.it/regioni/abruzzo">Abruzzo</a></li>
                <li><a href="https://provinceitalia.it/regioni/basilicata">Basilicata</a></li>
                <li><a href="https://provinceitalia.it/regioni/calabria">Calabria</a></li>
                <li><a href="https://provinceitalia.it/regioni/campania">Campania</a></li>
                <li><a href="https://provinceitalia.it/regioni/emilia-romagna">Emilia-Romagna</a></li>
                <li><a href="https://provinceitalia.it/regioni/friuli-venezia-giulia">Friuli-Venezia Giulia</a></li>
                <li><a href="https://provinceitalia.it/regioni/lazio">Lazio</a></li>
                <li><a href="https://provinceitalia.it/regioni/liguria">Liguria</a></li>
                <li><a href="https://provinceitalia.it/regioni/lombardia">Lombardia</a></li>
                <li><a href="https://provinceitalia.it/regioni/marche">Marche</a></li>
                <li><a href="https://provinceitalia.it/regioni/molise">Molise</a></li>
                <li><a href="https://provinceitalia.it/regioni/piemonte">Piemonte</a></li>
                <li><a href="https://provinceitalia.it/regioni/puglia">Puglia</a></li>
                <li><a href="https://provinceitalia.it/regioni/sardegna">Sardegna</a></li>
                <li><a href="https://provinceitalia.it/regioni/sicilia">Sicilia</a></li>
                <li><a href="https://provinceitalia.it/regioni/toscana">Toscana</a></li>
                <li><a href="https://provinceitalia.it/regioni/trentino-alto-adige">Trentino-Alto Adige</a></li>
                <li><a href="https://provinceitalia.it/regioni/umbria">Umbria</a></li>
                <li><a href="https://provinceitalia.it/regioni/valle-d-aosta">Valle d'Aosta</a></li>
                <li><a href="https://provinceitalia.it/regioni/veneto">Veneto</a></li>
            </ul>

            <h3>Elenco Province</h3>
            <ul>
                <li><a href="https://provinceitalia.it/province/agrigento">Agrigento</a></li>
                <li><a href="https://provinceitalia.it/province/alessandria">Alessandria</a></li>
                <li><a href="https://provinceitalia.it/province/ancona">Ancona</a></li>
                <li><a href="https://provinceitalia.it/province/arezzo">Arezzo</a></li>
                <li><a href="https://provinceitalia.it/province/ascoli-piceno">Ascoli Piceno</a></li>
                <li><a href="https://provinceitalia.it/province/asti">Asti</a></li>
                <li><a href="https://provinceitalia.it/province/avellino">Avellino</a></li>
                <li><a href="https://provinceitalia.it/province/bari">Bari</a></li>
                <li><a href="https://provinceitalia.it/province/barletta-andria-trani">Barletta-Andria-Trani</a></li>
                <li><a href="https://provinceitalia.it/province/belluno">Belluno</a></li>
                <li><a href="https://provinceitalia.it/province/benevento">Benevento</a></li>
                <li><a href="https://provinceitalia.it/province/bergamo">Bergamo</a></li>
                <li><a href="https://provinceitalia.it/province/biella">Biella</a></li>
                <li><a href="https://provinceitalia.it/province/bologna">Bologna</a></li>
                <li><a href="https://provinceitalia.it/province/bolzano">Bolzano</a></li>
                <li><a href="https://provinceitalia.it/province/brescia">Brescia</a></li>
                <li><a href="https://provinceitalia.it/province/brindisi">Brindisi</a></li>
                <li><a href="https://provinceitalia.it/province/cagliari">Cagliari</a></li>
                <li><a href="https://provinceitalia.it/province/caltanissetta">Caltanissetta</a></li>
                <li><a href="https://provinceitalia.it/province/campobasso">Campobasso</a></li>
                <li><a href="https://provinceitalia.it/province/caserta">Caserta</a></li>
                <li><a href="https://provinceitalia.it/province/catania">Catania</a></li>
                <li><a href="https://provinceitalia.it/province/catanzaro">Catanzaro</a></li>
                <li><a href="https://provinceitalia.it/province/chieti">Chieti</a></li>
                <li><a href="https://provinceitalia.it/province/como">Como</a></li>
                <li><a href="https://provinceitalia.it/province/cosenza">Cosenza</a></li>
                <li><a href="https://provinceitalia.it/province/cremona">Cremona</a></li>
                <li><a href="https://provinceitalia.it/province/crotone">Crotone</a></li>
                <li><a href="https://provinceitalia.it/province/cuneo">Cuneo</a></li>
                <li><a href="https://provinceitalia.it/province/enna">Enna</a></li>
                <li><a href="https://provinceitalia.it/province/fermo">Fermo</a></li>
                <li><a href="https://provinceitalia.it/province/ferrara">Ferrara</a></li>
                <li><a href="https://provinceitalia.it/province/firenze">Firenze</a></li>
                <li><a href="https://provinceitalia.it/province/foggia">Foggia</a></li>
                <li><a href="https://provinceitalia.it/province/forli-cesena">Forlì-Cesena</a></li>
                <li><a href="https://provinceitalia.it/province/frosinone">Frosinone</a></li>
                <li><a href="https://provinceitalia.it/province/gallura-nord-est-sardegna">Gallura Nord-Est Sardegna</a>
                </li>
                <li><a href="https://provinceitalia.it/province/genova">Genova</a></li>
                <li><a href="https://provinceitalia.it/province/gorizia">Gorizia</a></li>
                <li><a href="https://provinceitalia.it/province/grosseto">Grosseto</a></li>
                <li><a href="https://provinceitalia.it/province/imperia">Imperia</a></li>
                <li><a href="https://provinceitalia.it/province/isernia">Isernia</a></li>
                <li><a href="https://provinceitalia.it/province/l-aquila">L'Aquila</a></li>
                <li><a href="https://provinceitalia.it/province/la-spezia">La Spezia</a></li>
                <li><a href="https://provinceitalia.it/province/latina">Latina</a></li>
                <li><a href="https://provinceitalia.it/province/lecce">Lecce</a></li>
                <li><a href="https://provinceitalia.it/province/lecco">Lecco</a></li>
                <li><a href="https://provinceitalia.it/province/livorno">Livorno</a></li>
                <li><a href="https://provinceitalia.it/province/lodi">Lodi</a></li>
                <li><a href="https://provinceitalia.it/province/lucca">Lucca</a></li>
                <li><a href="https://provinceitalia.it/province/macerata">Macerata</a></li>
                <li><a href="https://provinceitalia.it/province/mantova">Mantova</a></li>
                <li><a href="https://provinceitalia.it/province/massa-carrara">Massa-Carrara</a></li>
                <li><a href="https://provinceitalia.it/province/matera">Matera</a></li>
                <li><a href="https://provinceitalia.it/province/medio-campidano">Medio Campidano</a></li>
                <li><a href="https://provinceitalia.it/province/messina">Messina</a></li>
                <li><a href="https://provinceitalia.it/province/milano">Milano</a></li>
                <li><a href="https://provinceitalia.it/province/modena">Modena</a></li>
                <li><a href="https://provinceitalia.it/province/monza-e-brianza">Monza e Brianza</a></li>
                <li><a href="https://provinceitalia.it/province/napoli">Napoli</a></li>
                <li><a href="https://provinceitalia.it/province/novara">Novara</a></li>
                <li><a href="https://provinceitalia.it/province/nuoro">Nuoro</a></li>
                <li><a href="https://provinceitalia.it/province/ogliastra">Ogliastra</a></li>
                <li><a href="https://provinceitalia.it/province/oristano">Oristano</a></li>
                <li><a href="https://provinceitalia.it/province/padova">Padova</a></li>
                <li><a href="https://provinceitalia.it/province/palermo">Palermo</a></li>
                <li><a href="https://provinceitalia.it/province/parma">Parma</a></li>
                <li><a href="https://provinceitalia.it/province/pavia">Pavia</a></li>
                <li><a href="https://provinceitalia.it/province/perugia">Perugia</a></li>
                <li><a href="https://provinceitalia.it/province/pesaro-e-urbino">Pesaro e Urbino</a></li>
                <li><a href="https://provinceitalia.it/province/pescara">Pescara</a></li>
                <li><a href="https://provinceitalia.it/province/piacenza">Piacenza</a></li>
                <li><a href="https://provinceitalia.it/province/pisa">Pisa</a></li>
                <li><a href="https://provinceitalia.it/province/pistoia">Pistoia</a></li>
                <li><a href="https://provinceitalia.it/province/pordenone">Pordenone</a></li>
                <li><a href="https://provinceitalia.it/province/potenza">Potenza</a></li>
                <li><a href="https://provinceitalia.it/province/prato">Prato</a></li>
                <li><a href="https://provinceitalia.it/province/ragusa">Ragusa</a></li>
                <li><a href="https://provinceitalia.it/province/ravenna">Ravenna</a></li>
                <li><a href="https://provinceitalia.it/province/reggio-calabria">Reggio Calabria</a></li>
                <li><a href="https://provinceitalia.it/province/reggio-emilia">Reggio Emilia</a></li>
                <li><a href="https://provinceitalia.it/province/rieti">Rieti</a></li>
                <li><a href="https://provinceitalia.it/province/rimini">Rimini</a></li>
                <li><a href="https://provinceitalia.it/province/roma">Roma</a></li>
                <li><a href="https://provinceitalia.it/province/rovigo">Rovigo</a></li>
                <li><a href="https://provinceitalia.it/province/salerno">Salerno</a></li>
                <li><a href="https://provinceitalia.it/province/sassari">Sassari</a></li>
                <li><a href="https://provinceitalia.it/province/savona">Savona</a></li>
                <li><a href="https://provinceitalia.it/province/siena">Siena</a></li>
                <li><a href="https://provinceitalia.it/province/siracusa">Siracusa</a></li>
                <li><a href="https://provinceitalia.it/province/sondrio">Sondrio</a></li>
                <li><a href="https://provinceitalia.it/province/sulcis-iglesiente">Sulcis Iglesiente</a></li>
                <li><a href="https://provinceitalia.it/province/taranto">Taranto</a></li>
                <li><a href="https://provinceitalia.it/province/teramo">Teramo</a></li>
                <li><a href="https://provinceitalia.it/province/terni">Terni</a></li>
                <li><a href="https://provinceitalia.it/province/torino">Torino</a></li>
                <li><a href="https://provinceitalia.it/province/trapani">Trapani</a></li>
                <li><a href="https://provinceitalia.it/province/trento">Trento</a></li>
                <li><a href="https://provinceitalia.it/province/treviso">Treviso</a></li>
                <li><a href="https://provinceitalia.it/province/trieste">Trieste</a></li>
                <li><a href="https://provinceitalia.it/province/udine">Udine</a></li>
                <li><a href="https://provinceitalia.it/province/valle-d-aosta">Valle d'Aosta</a></li>
                <li><a href="https://provinceitalia.it/province/varese">Varese</a></li>
                <li><a href="https://provinceitalia.it/province/venezia">Venezia</a></li>
                <li><a href="https://provinceitalia.it/province/verbano-cusio-ossola">Verbano-Cusio-Ossola</a></li>
                <li><a href="https://provinceitalia.it/province/vercelli">Vercelli</a></li>
                <li><a href="https://provinceitalia.it/province/verona">Verona</a></li>
                <li><a href="https://provinceitalia.it/province/vibo-valentia">Vibo Valentia</a></li>
                <li><a href="https://provinceitalia.it/province/vicenza">Vicenza</a></li>
                <li><a href="https://provinceitalia.it/province/viterbo">Viterbo</a></li>
            </ul>
        </nav>"""


def genera_html(comuni: list[dict]) -> str:
    """Genera l'intero file comuni.html."""
    num_comuni = len(comuni)
    tabella_html = genera_righe_tabella(comuni)

    # Serializziamo i dati dei comuni in JSON per il JavaScript
    comuni_json = json.dumps(comuni, ensure_ascii=False)

    html = f"""\
<!DOCTYPE html>
<html lang="it">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Elenco completo dei comuni d'Italia | Database Popolazione</title>
    <meta name="description"
        content="Elenco completo di tutti i comuni d'Italia suddivisi per provincia e per regione. Dati demografici Istat aggiornati al 2026.">
    <meta name="robots" content="index,follow">

    <link rel="canonical" href="https://provinceitalia.it/comuni">
    <script>
        if (window.location.hostname === 'samuelefrasca.github.io' || window.location.hostname === 'province-italia.pages.dev') {{
            const path = window.location.pathname
                .replace('/Province-Italia', '')
                .replace(/\\.html$/, '');
            window.location.replace('https://provinceitalia.it' + path + window.location.search);
        }}
    </script>

    <meta property="og:site_name" content="Elenco Comuni e Province d'Italia | Database Popolazione">
    <meta property="og:title" content="Elenco completo dei comuni d'Italia | Database Popolazione">
    <meta property="og:description"
        content="Elenco completo di tutti i comuni d'Italia suddivisi per provincia e per regione. Dati demografici Istat aggiornati al 2026.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://provinceitalia.it/comuni">
    <meta property="og:image" content="https://provinceitalia.it/assets/img/pi_icon.png">

    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="Elenco completo dei comuni d'Italia | Database Popolazione">
    <meta name="twitter:description"
        content="Elenco completo di tutti i comuni d'Italia suddivisi per provincia e per regione. Dati demografici Istat aggiornati al 2026.">
    <meta name="twitter:image" content="https://provinceitalia.it/assets/img/pi_icon.png">

    <link rel="icon" type="image/png" href="assets/img/pi_icon.png">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        tr.capoluogo-provincia td,
        td.capoluogo-provincia-cell {{
            font-weight: 700;
        }}
        tr.capoluogo-regione,
        tr.capoluogo-regione td {{
            background-color: #fff8c5 !important;
        }}
    </style>

    <script type="application/ld+json">
        {{
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": "Elenco completo dei comuni d'Italia | Database Popolazione",
            "url": "https://provinceitalia.it/comuni",
            "description": "Elenco completo di tutti i comuni d'Italia suddivisi per provincia e per regione. Dati demografici Istat aggiornati al 2026."
        }}
    </script>
</head>

<body>
    <header>
        <div class="header container">
            <div class="header1">
                <a href="index.html"><img class="logo" src="assets/img/pi_image.png" alt="pi_image" height="220px"></a>
            </div>
            <div class="header2">
                <h1 class="title">Elenco completo dei comuni d'Italia</h1>
                <div class="subtitle">
                    <p class="text-subtitle"><a class="a_link" href="https://demo.istat.it/app/?i=POS&l=it"
                            target="_blank">Dati aggiornati al bilancio demografico Istat del 1° gennaio 2026</a></p>
                    <p class="text-subtitle">In <b>grassetto</b> i capoluoghi di provincia, con sfondo giallo i capoluoghi di regione</p>
                    <p class="text-subtitle"><a class="a_link button pointer select-none" href="index.html"><b>Torna
                                alla home</b></a></p>
                </div>
            </div>
            <div class="header3"></div>
        </div>
    </header>

    <main>
        <div class="pannello-info" style="width: 80%; margin-left: auto; margin-right: auto;">
            <div class="titolo-div" id="titolo-provincia-div">
                <h2 class="titolo" id="titolo-provincia">Elenco completo dei comuni d'Italia</h2>
            </div>
            <h4 class="elementi-trovati" id="elementi-trovati">{num_comuni} comuni</h4>
            <input type="text" id="barra-ricerca" class="barra-ricerca" placeholder="Cerca un comune...">
            <table class="tabella" id="elenco-comuni"
                style="border-width: medium; border-style: none; border-color: currentcolor; border-image: initial;">
                <tbody>
                    <tr>
                        <th class="index"></th>
                        <th class="hel nome pointer select-none" onclick="ordinaPerNome(flagAlfabetico)">Comune <i
                                class="fa-solid fa-sort"></i></th>
                        <th class="hel provincia pointer select-none" onclick="ordinaPerProvincia(flagProvincia)">Provincia <i
                                class="fa-solid fa-sort"></i></th>
                        <th class="hel regione pointer select-none" onclick="ordinaPerRegione(flagRegione)">Regione <i
                                class="fa-solid fa-sort"></i></th>
                        <th class="hel abitanti pointer select-none" onclick="ordinaPerAbitanti(flagAbitanti)">
                            Popolazione <i class="fa-solid fa-sort"></i></th>
                    </tr>
{tabella_html}
                </tbody>
            </table>
        </div>
{NAV_INVISIBILE}
    </main>

    <footer>
        <div class="subfooter">
            <p>&copy; 2026 -
                <a class="a_link" href="https://samuelefrasca.github.io/" target="_blank"
                    rel="noopener noreferrer">Samuele Frasca</a>
            </p>
            <p>
                <a class="a_link github" href="https://github.com/samuelefrasca" target="_blank"
                    rel="noopener noreferrer">
                    <img class="github-logo" src="assets/img/GitHub_Invertocat_White.png" alt="github-logo">GitHub
                </a>
            </p>
        </div>
        <div class="subfooter">
            <p>Fonte mappe:
                <a href="https://simplemaps.com" class="a_link" target="_blank" rel="noopener noreferrer">Simplemaps</a>
                &middot;
                <a class="a_link" href="http://www.inkscape.org" target="_blank" rel="noopener noreferrer">Inkscape</a>
            </p>
            <p><a class="a_link" href="index.html">Torna alla home</a></p>
            <p><a class="a_link" href="sitemap.xml">Mappa del sito</a></p>
            <p><a class="a_link" href="mailto:info@provinceitalia.it">Contattaci</a></p>
        </div>
    </footer>

    <script> const tuttiComuni = {comuni_json}; </script>
    <script src="assets/js/scriptElencoCompletoComuni.js"></script>
</body>

</html>"""
    return html


def main():
    print("Caricamento comuni da data/...")
    comuni = carica_tutti_i_comuni()
    print(f"  Trovati {len(comuni)} comuni.")

    html = genera_html(comuni)

    out_path = "comuni.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generato: {out_path}")


if __name__ == "__main__":
    main()
