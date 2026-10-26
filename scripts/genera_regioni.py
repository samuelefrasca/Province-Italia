#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
genera_regioni.py (generato con Claude Sonnet 4 e Gemini Argon 4)
Genera un file HTML per ognuna delle 20 regioni italiane dentro la cartella regioni/.
Legge tutti i file JSON dei comuni della regione da data/<regione>/<provincia>.json
e costruisce nell'HTML statico la tabella completa dei comuni con link alle province.
L'SVG viene copiato dal file svg/<regione>.svg (dalla riga 4 in poi).
"""

import json
import os
import re
import unicodedata

# ---------------------------------------------------------------------------
# Configurazione e caricamento dati delle regioni da data/province.json
# ---------------------------------------------------------------------------
BASE_URL = "https://samuelefrasca.github.io/Province-Italia"

with open("data/province.json", encoding="utf-8") as f:
    province = json.load(f)

REGIONI = list(province.keys())

# Dizionario di fallback per le sigle automobilistiche (usato se non presente nel JSON)
SIGLE_FALLBACK = {
    "Agrigento": "AG", "Alessandria": "AL", "Ancona": "AN", "Arezzo": "AR", "Ascoli Piceno": "AP",
    "Asti": "AT", "Avellino": "AV", "Bari": "BA", "Barletta-Andria-Trani": "BT", "Belluno": "BL",
    "Benevento": "BN", "Bergamo": "BG", "Biella": "BI", "Bologna": "BO", "Bolzano": "BZ",
    "Brescia": "BS", "Brindisi": "BR", "Cagliari": "CA", "Caltanissetta": "CL", "Campobasso": "CB",
    "Caserta": "CE", "Catania": "CT", "Catanzaro": "CZ", "Chieti": "CH", "Como": "CO",
    "Cosenza": "CS", "Cremona": "CR", "Crotone": "KR", "Cuneo": "CN", "Enna": "EN",
    "Fermo": "FM", "Ferrara": "FE", "Firenze": "FI", "Foggia": "FG", "Forlì-Cesena": "FC",
    "Frosinone": "FR", "Gallura Nord-Est Sardegna": "OT", "Genova": "GE", "Gorizia": "GO",
    "Grosseto": "GR", "Imperia": "IM", "Isernia": "IS", "L'Aquila": "AQ", "La Spezia": "SP",
    "Latina": "LT", "Lecce": "LE", "Lecco": "LC", "Livorno": "LI", "Lodi": "LO", "Lucca": "LU",
    "Macerata": "MC", "Mantova": "MN", "Massa-Carrara": "MS", "Matera": "MT", "Medio Campidano": "VS",
    "Messina": "ME", "Milano": "MI", "Modena": "MO", "Monza e Brianza": "MB", "Napoli": "NA",
    "Novara": "NO", "Nuoro": "NU", "Ogliastra": "OG", "Oristano": "OR", "Padova": "PD",
    "Palermo": "PA", "Parma": "PR", "Pavia": "PV", "Perugia": "PG", "Pesaro e Urbino": "PU",
    "Pescara": "PE", "Piacenza": "PC", "Pisa": "PI", "Pistoia": "PT", "Pordenone": "PN",
    "Potenza": "PZ", "Prato": "PO", "Ragusa": "RG", "Ravenna": "RA", "Reggio Calabria": "RC",
    "Reggio Emilia": "RE", "Rieti": "RI", "Rimini": "RN", "Roma": "RM", "Rovigo": "RO",
    "Salerno": "SA", "Sassari": "SS", "Savona": "SV", "Siena": "SI", "Siracusa": "SR",
    "Sondrio": "SO", "Sulcis Iglesiente": "CI", "Taranto": "TA", "Teramo": "TE", "Terni": "TR",
    "Torino": "TO", "Trapani": "TP", "Trento": "TN", "Treviso": "TV", "Trieste": "TS",
    "Udine": "UD", "Valle d'Aosta": "AO", "Varese": "VA", "Venezia": "VE",
    "Verbano-Cusio-Ossola": "VB", "Vercelli": "VC", "Verona": "VR", "Vibo Valentia": "VV",
    "Vicenza": "VI", "Viterbo": "VT"
}

NAV_REGIONI = """        <nav class="nav-invisibile">
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
        <li><a href="https://provinceitalia.it/province/gallura-nord-est-sardegna">Gallura Nord-Est Sardegna</a></li>
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


# ---------------------------------------------------------------------------
# Funzioni di utilità, lettura JSON e generazione HTML
# ---------------------------------------------------------------------------
def slugify(nome: str) -> str:
    """Converte un testo in uno slug ASCII sicuro per file e URL."""
    normalized = unicodedata.normalize("NFKD", nome)
    ascii_text = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    ascii_text = ascii_text.lower()
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    return ascii_text


def formatta_numero(n: int) -> str:
    """Formatta un numero con il separatore delle migliaia italiano (punto)."""
    return f"{n:,}".replace(",", ".")


# Articolo per "della regione X" nella description
def della_regione(nome: str) -> str:
    """Restituisce la preposizione articolata corretta ('della', 'del', 'delle') per la regione."""
    vocali = "AEIOUaeiou"
    # casi speciali
    speciali = {
        "Valle d'Aosta": "della Valle d'Aosta",
        "Trentino-Alto Adige": "del Trentino-Alto Adige",
        "Friuli-Venezia Giulia": "del Friuli-Venezia Giulia",
        "Emilia-Romagna": "dell'Emilia-Romagna",
        "Marche": "delle Marche",
    }
    if nome in speciali:
        return speciali[nome]
    if nome[0] in vocali:
        return f"dell'{nome}"
    # maschile o femminile: le regioni italiane sono quasi tutte femminili
    maschili = ["Lazio", "Molise", "Piemonte", "Veneto", "Abruzzo"]
    if nome in maschili:
        return f"del {nome}"
    return f"della {nome}"


def leggi_comuni_regione(slug_regione: str) -> list[dict]:
    """
    Legge tutti i file JSON dei comuni dentro data/<slug_regione>/
    e restituisce la lista ordinata alfabeticamente per nome del comune.
    """
    cartella = os.path.join("data", slug_regione)
    if not os.path.isdir(cartella):
        print(f"  ATTENZIONE: cartella comuni mancante: {cartella}")
        return []

    comuni_regione = []
    for nome_file in sorted(os.listdir(cartella)):
        if not nome_file.endswith(".json"):
            continue
        percorso = os.path.join(cartella, nome_file)
        with open(percorso, encoding="utf-8") as f:
            comuni = json.load(f)
        for c in comuni:
            nome_prov = c.get("provincia", "")
            sigla = c.get("sigla") or SIGLE_FALLBACK.get(nome_prov, "")
            comuni_regione.append({
                "comune": c["comune"],
                "provincia": nome_prov,
                "sigla": sigla,
                "popolazione_totale": c["popolazione_totale"],
                "capoluogo": c.get("capoluogo", False),
            })

    # Ordina alfabeticamente per nome comune
    comuni_regione.sort(key=lambda x: x["comune"].lower())
    return comuni_regione


def genera_tabella_regione(comuni: list[dict]) -> tuple[str, int]:
    """
    Genera l'HTML della tabella dei comuni della regione (con link cliccabile
    sulla provincia) e restituisce anche la popolazione totale della regione.
    """
    if not comuni:
        return "", 0

    righe = []
    righe.append(
        '<tr>'
        '<th class="index"></th>'
        '<th class="hel nome pointer select-none" onclick="ordinaPerNome(flagAlfabetico)">Comune <i class="fa-solid fa-sort"></i></th>'
        '<th class="hel provincia pointer select-none" onclick="ordinaPerProvincia(flagProvincia)">Provincia <i class="fa-solid fa-sort"></i></th>'
        '<th class="hel sigla pointer select-none" onclick="ordinaPerSigla(flagSigla)">Sigla <i class="fa-solid fa-sort"></i></th>'
        '<th class="hel abitanti pointer select-none" onclick="ordinaPerAbitanti(flagAbitanti)">Popolazione <i class="fa-solid fa-sort"></i></th>'
        '</tr>'
    )

    popolazione_totale = 0
    for i, c in enumerate(comuni, start=1):
        nome_comune = c["comune"]
        nome_prov = c["provincia"]
        sigla = c["sigla"]
        pop = c["popolazione_totale"]
        popolazione_totale += pop
        pop_str = formatta_numero(pop)

        prov_slug = slugify(nome_prov) if nome_prov else ""
        prov_link = f'<a class="comunihref" href="/province/{prov_slug}">{nome_prov}</a>' if prov_slug else nome_prov

        if c.get("capoluogo"):
            righe.append(
                f'<tr>'
                f'<td class="el index"><strong>{i}</strong></td>'
                f'<td class="el nome"><strong>{nome_comune}</strong></td>'
                f'<td class="el provincia"><strong>{prov_link}</strong></td>'
                f'<td class="el sigla"><strong>{sigla}</strong></td>'
                f'<td class="el abitanti"><strong>{pop_str}</strong></td>'
                f'</tr>'
            )
        else:
            righe.append(
                f'<tr>'
                f'<td class="el index">{i}</td>'
                f'<td class="el nome">{nome_comune}</td>'
                f'<td class="el provincia">{prov_link}</td>'
                f'<td class="el sigla">{sigla}</td>'
                f'<td class="el abitanti">{pop_str}</td>'
                f'</tr>'
            )

    # Riga totale
    righe.append(
        f'<tr>'
        f'<td class="index"></td>'
        f'<td class="fel nome"><strong>Popolazione totale</strong></td>'
        f'<td class="fel provincia"></td>'
        f'<td class="fel sigla"></td>'
        f'<td class="fel abitanti"><strong>{formatta_numero(popolazione_totale)}</strong></td>'
        f'</tr>'
    )

    return "\n".join(righe), popolazione_totale


def leggi_svg(slug: str, regione: str) -> tuple[str, bool]:
    """Legge il file svg/<slug>.svg e restituisce il contenuto dalla riga 4 in poi."""
    percorso = os.path.join("svg", f"{slug}.svg")
    if not os.path.exists(percorso):
        print(f"  ATTENZIONE: SVG mancante per {regione} ({percorso})")
        return "<!-- SVG mancante -->", False
    with open(percorso, encoding="utf-8") as f:
        righe = f.readlines()
    # dalla riga 4 in poi (indice 3)
    return "".join(righe[3:]).strip(), True


def genera_html(nome_regione: str, slug: str, svg_content: str) -> str:
    """Genera l'HTML completo per la pagina della singola regione."""
    prep_regione = della_regione(nome_regione)

    # Leggi tutti i comuni della regione e genera la tabella statica per la SEO
    comuni = leggi_comuni_regione(slug)
    tabella_html, pop_totale = genera_tabella_regione(comuni)
    num_comuni = len(comuni)
    pop_tot_str = formatta_numero(pop_totale)
    num_province = len(province.get(nome_regione, []))

    # Title e Description ottimizzati per le query su Google (es. "province umbria", "province liguria")
    seo_title = f"Province {prep_regione}: Elenco Completo e {num_comuni} Comuni per Popolazione | ProvinceItalia"
    seo_desc = (
        f"Elenco completo delle {num_province} province e dei {num_comuni} comuni {prep_regione} "
        f"({pop_tot_str} abitanti totali). Classifica per popolazione, sigle e mappa interattiva Istat 2026."
    )

    html = f"""<!DOCTYPE html>
<html lang="it">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{seo_title}</title>
    <meta name="description"
        content="{seo_desc}">
    <meta name="robots" content="index,follow">

    <meta property="og:site_name" content="ProvinceItalia | Province e Comuni d'Italia per Popolazione">
    <meta property="og:title" content="{seo_title}">
    <meta property="og:description" content="{seo_desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://provinceitalia.it/regioni/{slug}">
    <meta property="og:image" content="https://provinceitalia.it/assets/img/pi_icon.png">

    <link rel="canonical" href="https://provinceitalia.it/regioni/{slug}">
    <script>
        if (window.location.hostname === 'samuelefrasca.github.io' || window.location.hostname === 'province-italia.pages.dev') {{
            const path = window.location.pathname
                .replace('/provinceitalia', '')
                .replace(/\.html$/, '');
            window.location.replace('https://provinceitalia.it' + path + window.location.search);
        }}
    </script>

    <link rel="icon" type="image/png" href="../assets/img/pi_icon.png">
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="stylesheet" href="../assets/css/regioni.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

    <script type="application/ld+json">
        {{
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": "{seo_title}",
            "url": "https://provinceitalia.it/regioni/{slug}",
            "description": "{seo_desc}",
            "breadcrumb": {{
                "@type": "BreadcrumbList",
                "itemListElement": [{{
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": "https://provinceitalia.it/"
                }},{{
                    "@type": "ListItem",
                    "position": 2,
                    "name": "{nome_regione}",
                    "item": "https://provinceitalia.it/regioni/{slug}"
                }}]
            }}
        }}
    </script>
</head>

<body>
    <header>
        <div class="header container">
            <div class="header1">
                <a href="../"><img class="logo" src="../assets/img/pi_image.png" alt="pi_image" height="220px"></a>
            </div>
            <div class="header2">
                <h1 class="title">Regione {nome_regione}</h1>
                <div class="subtitle">
                    <p class="text-subtitle"><a class="a_link" href="https://demo.istat.it/app/?i=POS&l=it" target="_blank">Dati aggiornati al bilancio demografico Istat del 1° gennaio 2026</a></p>
                    <p class="text-subtitle">In <b>grassetto</b> i capoluoghi di provincia</p>
                    <p class="text-subtitle"><a class="a_link text-subtitle button pointer select-none" href="/"><b>← Torna alla home</b></a></p>
                </div>
            </div>
            <div class="header3">
                <p class="text-subtitle"><a class="a_link text-subtitle button pointer select-none" href="https://quiz.provinceitalia.it"><b>Gioca ai Quiz</b></a></p>
            </div>
        </div>
    </header>
    <main>
        <div class="pannello-info">
            <div class="titolo-div" id="titolo-provincia-div">
                <h2 class="titolo" id="titolo-provincia">Elenco completo dei comuni</h2>
            </div>
            <h4 class="elementi-trovati" id="elementi-trovati">{num_comuni} comuni</h4>
            <input type="text" id="barra-ricerca" class="barra-ricerca" placeholder="Cerca un comune...">
            <table class="tabella" id="elenco-comuni" style="border-width: medium; border-style: none; border-color: currentcolor; border-image: initial;">
                <tbody>
                    {tabella_html}
                </tbody>
            </table>
        </div>
        {svg_content}
{NAV_REGIONI}
    </main>
    <footer>
        <div class="subfooter">
            <p>&copy; 2026 ProvinceItalia ·
                <a class="a_link" href="https://samuelefrasca.github.io/" target="_blank"
                    rel="noopener noreferrer">Samuele Frasca</a>
            </p>
            <p>
                <a class="a_link github" href="https://github.com/samuelefrasca" target="_blank"
                    rel="noopener noreferrer">
                    <i class="fa-brands fa-github"></i> GitHub
                </a>
            </p>
        </div>
        <div class="subfooter">
            <p>Mappe:
                <a href="https://simplemaps.com" class="a_link" target="_blank" rel="noopener noreferrer">Simplemaps</a>
                &middot;
                <a class="a_link" href="http://www.inkscape.org" target="_blank" rel="noopener noreferrer">Inkscape</a>
            </p>
            <p><a class="a_link" href="../about">About</a></p>
            <p><a class="a_link" href="../privacy">Privacy Policy</a></p>
            <p><a class="a_link" href="../sitemap.xml">Sitemap</a></p>
            <p><a class="a_link" href="mailto:info@provinceitalia.it">Contattaci</a></p>
        </div>
    </footer>
    <script> const nomeRegione = "{nome_regione}"; </script>
    <script src="../assets/js/scriptregioni.js"></script>
    <script src="../assets/js/ordinamentoregioniprovince.js"></script>
    <script src="../assets/js/ricercaregioniprovince.js"></script>
</body>

</html>"""
    return html


def main():
    os.makedirs("regioni", exist_ok=True)

    generati = 0
    errori = 0

    for regione in REGIONI:
        slug = slugify(regione)
        svg_content, trovato = leggi_svg(slug, regione)
        if not trovato:
            errori += 1

        html = genera_html(regione, slug, svg_content)

        percorso_out = os.path.join("regioni", f"{slug}.html")
        with open(percorso_out, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"  ✓ {percorso_out}")
        generati += 1

    print(f"\nGenerati {generati} file HTML nella cartella regioni/.")
    if errori:
        print(f"Errori: {errori} (controlla i messaggi ATTENZIONE sopra).")


if __name__ == "__main__":
    main()