#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
genera_province.py
Genera un file HTML per ognuna delle 110 province italiane dentro la cartella province/.
L'SVG viene copiato dal file svg/<regione>.svg (dalla riga 4 in poi),
e alla provincia di riferimento viene aggiunto un fill chiaro per evidenziarla.
"""

import json
import os
import re
import unicodedata

# ---------------------------------------------------------------------------
# Dati: province italiane → regione di appartenenza
# id SVG = nome esatto dell'attributo id del <g> corrispondente nel file SVG
# ---------------------------------------------------------------------------
PROVINCE = [
    # (nome_provincia, id_svg, regione, slug_file_html)
    # Abruzzo
    ("L'Aquila",        "L'Aquila",             "Abruzzo",              "l-aquila"),
    ("Chieti",          "Chieti",               "Abruzzo",              "chieti"),
    ("Pescara",         "Pescara",              "Abruzzo",              "pescara"),
    ("Teramo",          "Teramo",               "Abruzzo",              "teramo"),
    # Basilicata
    ("Matera",          "Matera",               "Basilicata",           "matera"),
    ("Potenza",         "Potenza",              "Basilicata",           "potenza"),
    # Calabria
    ("Catanzaro",       "Catanzaro",            "Calabria",             "catanzaro"),
    ("Cosenza",         "Cosenza",              "Calabria",             "cosenza"),
    ("Crotone",         "Crotone",              "Calabria",             "crotone"),
    ("Reggio Calabria", "Reggio Calabria",      "Calabria",             "reggio-calabria"),
    ("Vibo Valentia",   "Vibo Valentia",        "Calabria",             "vibo-valentia"),
    # Campania
    ("Avellino",        "Avellino",             "Campania",             "avellino"),
    ("Benevento",       "Benevento",            "Campania",             "benevento"),
    ("Caserta",         "Caserta",              "Campania",             "caserta"),
    ("Napoli",          "Napoli",               "Campania",             "napoli"),
    ("Salerno",         "Salerno",              "Campania",             "salerno"),
    # Emilia-Romagna
    ("Bologna",         "Bologna",              "Emilia-Romagna",       "bologna"),
    ("Ferrara",         "Ferrara",              "Emilia-Romagna",       "ferrara"),
    ("Forlì-Cesena",    "Forlì-Cesena",         "Emilia-Romagna",       "forli-cesena"),
    ("Modena",          "Modena",               "Emilia-Romagna",       "modena"),
    ("Parma",           "Parma",                "Emilia-Romagna",       "parma"),
    ("Piacenza",        "Piacenza",             "Emilia-Romagna",       "piacenza"),
    ("Ravenna",         "Ravenna",              "Emilia-Romagna",       "ravenna"),
    ("Reggio Emilia",   "Reggio Emilia",        "Emilia-Romagna",       "reggio-emilia"),
    ("Rimini",          "Rimini",               "Emilia-Romagna",       "rimini"),
    # Friuli-Venezia Giulia
    ("Gorizia",         "Gorizia",              "Friuli-Venezia Giulia","gorizia"),
    ("Pordenone",       "Pordenone",            "Friuli-Venezia Giulia","pordenone"),
    ("Trieste",         "Trieste",              "Friuli-Venezia Giulia","trieste"),
    ("Udine",           "Udine",                "Friuli-Venezia Giulia","udine"),
    # Lazio
    ("Frosinone",       "Frosinone",            "Lazio",                "frosinone"),
    ("Latina",          "Latina",               "Lazio",                "latina"),
    ("Rieti",           "Rieti",                "Lazio",                "rieti"),
    ("Roma",            "Roma",                 "Lazio",                "roma"),
    ("Viterbo",         "Viterbo",              "Lazio",                "viterbo"),
    # Liguria
    ("Genova",          "Genova",               "Liguria",              "genova"),
    ("Imperia",         "Imperia",              "Liguria",              "imperia"),
    ("La Spezia",       "La Spezia",            "Liguria",              "la-spezia"),
    ("Savona",          "Savona",               "Liguria",              "savona"),
    # Lombardia
    ("Bergamo",         "Bergamo",              "Lombardia",            "bergamo"),
    ("Brescia",         "Brescia",              "Lombardia",            "brescia"),
    ("Como",            "Como",                 "Lombardia",            "como"),
    ("Cremona",         "Cremona",              "Lombardia",            "cremona"),
    ("Lecco",           "Lecco",                "Lombardia",            "lecco"),
    ("Lodi",            "Lodi",                 "Lombardia",            "lodi"),
    ("Mantova",         "Mantova",              "Lombardia",            "mantova"),
    ("Milano",          "Milano",               "Lombardia",            "milano"),
    ("Monza e Brianza", "Monza e Brianza",      "Lombardia",            "monza-e-brianza"),
    ("Pavia",           "Pavia",                "Lombardia",            "pavia"),
    ("Sondrio",         "Sondrio",              "Lombardia",            "sondrio"),
    ("Varese",          "Varese",               "Lombardia",            "varese"),
    # Marche
    ("Ancona",          "Ancona",               "Marche",               "ancona"),
    ("Ascoli Piceno",   "Ascoli Piceno",        "Marche",               "ascoli-piceno"),
    ("Fermo",           "Fermo",                "Marche",               "fermo"),
    ("Macerata",        "Macerata",             "Marche",               "macerata"),
    ("Pesaro e Urbino", "Pesaro e Urbino",      "Marche",               "pesaro-e-urbino"),
    # Molise
    ("Campobasso",      "Campobasso",           "Molise",               "campobasso"),
    ("Isernia",         "Isernia",              "Molise",               "isernia"),
    # Piemonte
    ("Alessandria",     "Alessandria",          "Piemonte",             "alessandria"),
    ("Asti",            "Asti",                 "Piemonte",             "asti"),
    ("Biella",          "Biella",               "Piemonte",             "biella"),
    ("Cuneo",           "Cuneo",                "Piemonte",             "cuneo"),
    ("Novara",          "Novara",               "Piemonte",             "novara"),
    ("Torino",          "Torino",               "Piemonte",             "torino"),
    ("Verbano-Cusio-Ossola", "Verbano-Cusio-Ossola", "Piemonte",        "verbano-cusio-ossola"),
    ("Vercelli",        "Vercelli",             "Piemonte",             "vercelli"),
    # Puglia
    ("Bari",            "Bari",                 "Puglia",               "bari"),
    ("Barletta-Andria-Trani", "Barletta-Andria-Trani", "Puglia",        "barletta-andria-trani"),
    ("Brindisi",        "Brindisi",             "Puglia",               "brindisi"),
    ("Foggia",          "Foggia",               "Puglia",               "foggia"),
    ("Lecce",           "Lecce",                "Puglia",               "lecce"),
    ("Taranto",         "Taranto",              "Puglia",               "taranto"),
    # Sardegna
    ("Cagliari",        "Cagliari",             "Sardegna",             "cagliari"),
    ("Gallura Nord-Est Sardegna", "Gallura Nord-Est Sardegna", "Sardegna", "gallura-nord-est-sardegna"),
    ("Medio Campidano", "Medio Campidano",      "Sardegna",             "medio-campidano"),
    ("Nuoro",           "Nuoro",                "Sardegna",             "nuoro"),
    ("Ogliastra",       "Ogliastra",            "Sardegna",             "ogliastra"),
    ("Oristano",        "Oristano",             "Sardegna",             "oristano"),
    ("Sassari",         "Sassari",              "Sardegna",             "sassari"),
    ("Sulcis Iglesiente", "Sulcis Iglesiente",  "Sardegna",             "sulcis-iglesiente"),
    # Sicilia
    ("Agrigento",       "Agrigento",            "Sicilia",              "agrigento"),
    ("Caltanissetta",   "Caltanissetta",        "Sicilia",              "caltanissetta"),
    ("Catania",         "Catania",              "Sicilia",              "catania"),
    ("Enna",            "Enna",                 "Sicilia",              "enna"),
    ("Messina",         "Messina",              "Sicilia",              "messina"),
    ("Palermo",         "Palermo",              "Sicilia",              "palermo"),
    ("Ragusa",          "Ragusa",               "Sicilia",              "ragusa"),
    ("Siracusa",        "Siracusa",             "Sicilia",              "siracusa"),
    ("Trapani",         "Trapani",              "Sicilia",              "trapani"),
    # Toscana
    ("Arezzo",          "Arezzo",               "Toscana",              "arezzo"),
    ("Firenze",         "Firenze",              "Toscana",              "firenze"),
    ("Grosseto",        "Grosseto",             "Toscana",              "grosseto"),
    ("Livorno",         "Livorno",              "Toscana",              "livorno"),
    ("Lucca",           "Lucca",                "Toscana",              "lucca"),
    ("Massa-Carrara",   "Massa-Carrara",        "Toscana",              "massa-carrara"),
    ("Pisa",            "Pisa",                 "Toscana",              "pisa"),
    ("Pistoia",         "Pistoia",              "Toscana",              "pistoia"),
    ("Prato",           "Prato",                "Toscana",              "prato"),
    ("Siena",           "Siena",                "Toscana",              "siena"),
    # Trentino-Alto Adige
    ("Bolzano",         "Bolzano",              "Trentino-Alto Adige",  "bolzano"),
    ("Trento",          "Trento",               "Trentino-Alto Adige",  "trento"),
    # Umbria
    ("Perugia",         "Perugia",              "Umbria",               "perugia"),
    ("Terni",           "Terni",                "Umbria",               "terni"),
    # Valle d'Aosta
    ("Valle d'Aosta",   "Valle d'Aosta",        "Valle d'Aosta",        "valle-d-aosta"),
    # Veneto
    ("Belluno",         "Belluno",              "Veneto",               "belluno"),
    ("Padova",          "Padova",               "Veneto",               "padova"),
    ("Rovigo",          "Rovigo",               "Veneto",               "rovigo"),
    ("Treviso",         "Treviso",              "Veneto",               "treviso"),
    ("Venezia",         "Venezia",              "Veneto",               "venezia"),
    ("Verona",          "Verona",               "Veneto",               "verona"),
    ("Vicenza",         "Vicenza",              "Veneto",               "vicenza"),
]

# Slug per i file SVG e HTML delle regioni
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

COLORE_EVIDENZIATO = "#a83232"  # più chiaro di #821f1f, più scuro di #a83232 (hover)

NAV_REGIONI = """            <nav class="nav-invisibile">
    <h3>Pagine Principali</h3>
    <ul>
        <li><a href="https://provinceitalia.it/">Home</a></li>
        <li><a href="https://provinceitalia.it/privacy">Privacy</a></li>
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


def leggi_svg(regione: str) -> str:
    """Legge il file svg/<regione>.svg e restituisce il contenuto dalla riga 4 in poi."""
    slug = REGIONE_SLUG[regione]
    percorso = os.path.join("svg", f"{slug}.svg")
    if not os.path.exists(percorso):
        print(f"  ATTENZIONE: SVG non trovato: {percorso}")
        return "<!-- SVG non trovato -->"
    with open(percorso, encoding="utf-8") as f:
        righe = f.readlines()
    # dalla riga 4 in poi (indice 3)
    return "".join(righe[3:]).rstrip()


def evidenzia_provincia(svg_contenuto: str, id_svg: str) -> str:
    """
    Aggiunge style="fill: <COLORE>" a tutti i <path> contenuti nel <g id="<id_svg>">.
    Il fill viene applicato direttamente ai <path> (non al <g>) per garantire
    che l'inline style abbia la precedenza sulle regole CSS come `path { fill: ... }`.
    """
    id_escaped = re.escape(id_svg)

    # Trova il blocco <g id="<id_svg>" ...> ... </g> (non-greedy, prende il primo </g>)
    pattern_g = rf'(<g\b[^>]*\bid="{id_escaped}"[^>]*>)(.*?)(</g>)'
    
    def sostituisci_gruppo(m):
        tag_apertura = m.group(1)
        contenuto_g = m.group(2)
        tag_chiusura = m.group(3)
        
        # Aggiunge fill inline a tutti i <path> dentro questo <g>
        def aggiungi_fill_path(pm):
            path_tag = pm.group(0)
            if 'style="' in path_tag:
                # Aggiunge fill: al blocco style esistente del <path>
                path_tag = re.sub(
                    r'style="([^"]*)"',
                    lambda s: f'style="{s.group(1)};fill:{COLORE_EVIDENZIATO}"',
                    path_tag
                )
            else:
                # Inserisce style prima della chiusura del tag <path>
                path_tag = re.sub(
                    r'(/?>)$',
                    f' style="fill:{COLORE_EVIDENZIATO}"\\1',
                    path_tag
                )
            return path_tag
        
        contenuto_modificato = re.sub(r'<path\b[^>]*/?>',  aggiungi_fill_path, contenuto_g)
        return tag_apertura + contenuto_modificato + tag_chiusura

    nuovo_svg, n = re.subn(pattern_g, sostituisci_gruppo, svg_contenuto, count=1, flags=re.DOTALL)
    if n == 0:
        print(f"  ATTENZIONE: id '{id_svg}' non trovato nell'SVG.")
    return nuovo_svg


def titolo_provincia(nome: str, regione: str) -> str:
    """Restituisce il titolo istituzionale corretto della provincia."""
    citta_metropolitane = {
        "Bari", "Bologna", "Cagliari", "Catania", "Firenze", "Genova",
        "Messina", "Milano", "Napoli", "Palermo", "Reggio Calabria",
        "Roma", "Sassari", "Torino", "Venezia"
    }
    if nome == "Roma":
        return "Città metropolitana di Roma Capitale"
    if nome == "Monza e Brianza":
        return "Provincia di Monza e della Brianza"
    if nome == "Bolzano":
        return "Provincia autonoma di Bolzano - Alto Adige"
    if nome == "Trento":
        return "Provincia autonoma di Trento"
    if nome == "L'Aquila":
        return "Provincia dell'Aquila"
    if nome == "La Spezia":
        return "Provincia della Spezia"
    if nome == "Gallura Nord-Est Sardegna":
        return "Provincia della Gallura Nord-Est Sardegna"
    if nome == "Medio Campidano":
        return "Provincia del Medio Campidano"
    if nome == "Ogliastra":
        return "Provincia dell'Ogliastra"
    if nome == "Sulcis Iglesiente":
        return "Provincia del Sulcis Iglesiente"
    if nome == "Verbano-Cusio-Ossola":
        return "Provincia del Verbano-Cusio-Ossola"
    if nome == "Valle d'Aosta":
        return "Regione autonoma Valle d'Aosta"
    if nome in citta_metropolitane:
        return f"Città metropolitana di {nome}"
    if regione == "Sicilia":
        return f"Libero consorzio comunale di {nome}"
    if regione == "Friuli-Venezia Giulia":
        return f"Ente di decentramento regionale di {nome}"
    if regione == "Trentino-Alto Adige":
        return f"Provincia autonoma di {nome}"
    return f"Provincia di {nome}"


def slugify(nome: str) -> str:
    """Converte un testo in uno slug ASCII sicuro per file e URL."""
    normalized = unicodedata.normalize('NFKD', nome)
    ascii_text = ''.join(ch for ch in normalized if not unicodedata.combining(ch))
    ascii_text = ascii_text.replace(" ", "-").replace("'", "-")
    return ascii_text.lower()


def leggi_comuni(regione: str, nome: str) -> list:
    """Legge il file JSON dei comuni per una data provincia."""
    slug_regione = REGIONE_SLUG[regione]
    slug_provincia = slugify(nome)
    percorso = os.path.join("data", slug_regione, f"{slug_provincia}.json")
    if not os.path.exists(percorso):
        print(f"  ATTENZIONE: JSON comuni non trovato: {percorso}")
        return []
    with open(percorso, encoding="utf-8") as f:
        return json.load(f)


def formatta_numero(n: int) -> str:
    """Formatta un numero con il separatore delle migliaia italiano (punto)."""
    return f"{n:,}".replace(",", ".")


def genera_tabella_comuni(comuni: list) -> str:
    """Genera l'HTML della tabella dei comuni (senza colonne Provincia e Sigla)."""
    if not comuni:
        return ""

    righe = []
    righe.append('<tr>'
                 '<th class="index"></th>'
                 '<th class="hel nome pointer select-none" onclick="ordinaPerNome(flagAlfabetico)">Comune <i class="fa-solid fa-sort"></i></th>'
                 '<th class="hel abitanti pointer select-none" onclick="ordinaPerAbitanti(flagAbitanti)">Popolazione <i class="fa-solid fa-sort"></i></th>'
                 '</tr>')

    popolazione_totale = 0
    for i, comune in enumerate(comuni, start=1):
        nome_comune = comune["comune"]
        pop = comune["popolazione_totale"]
        popolazione_totale += pop
        pop_str = formatta_numero(pop)

        if comune.get("capoluogo"):
            righe.append(f'<tr>'
                         f'<td class="el index"><strong>{i}</strong></td>'
                         f'<td class="el nome"><strong>{nome_comune}</strong></td>'
                         f'<td class="el abitanti"><strong>{pop_str}</strong></td>'
                         f'</tr>')
        else:
            righe.append(f'<tr>'
                         f'<td class="el index">{i}</td>'
                         f'<td class="el nome">{nome_comune}</td>'
                         f'<td class="el abitanti">{pop_str}</td>'
                         f'</tr>')

    # Riga totale
    righe.append(f'<tr>'
                 f'<td class="index"></td>'
                 f'<td class="fel nome"><strong>Popolazione totale</strong></td>'
                 f'<td class="fel abitanti"><strong>{formatta_numero(popolazione_totale)}</strong></td>'
                 f'</tr>')

    return "\n".join(righe)


def genera_html(nome: str, id_svg: str, regione: str, slug: str, svg_raw: str) -> str:
    slug_regione = REGIONE_SLUG[regione]
    svg_evidenziato = evidenzia_provincia(svg_raw, id_svg)
    titolo_ist = titolo_provincia(nome, regione)

    # Leggi i comuni dal JSON e genera la tabella
    comuni = leggi_comuni(regione, nome)
    tabella_html = genera_tabella_comuni(comuni)
    num_comuni = len(comuni)

    html = f"""<!DOCTYPE html>
<html lang="it">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{nome} | Elenco Comuni e Province d'Italia | Database Popolazione</title>
    <meta name="description"
        content="Elenco completo dei comuni della {titolo_ist}. Dati demografici Istat aggiornati al 1° gennaio 2026.">

    <meta property="og:site_name" content="Elenco Comuni e Province d'Italia | Database Popolazione">
    <meta property="og:title" content="{nome} | Elenco Comuni e Province d'Italia | Database Popolazione">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://provinceitalia.it/province/{slug}">
    <meta property="og:image" content="https://provinceitalia.it/assets/img/pi_icon.png">

    <link rel="canonical" href="https://provinceitalia.it/province/{slug}">
    <script>
        if (window.location.hostname === 'samuelefrasca.github.io' || window.location.hostname === 'province-italia.pages.dev') {{
            const path = window.location.pathname
                .replace('/Province-Italia', '')
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
            "name": "{nome} | Elenco Comuni e Province d'Italia | Database Popolazione",
            "url": "https://provinceitalia.it/province/{slug}",
            "description": "Elenco completo dei comuni della {titolo_ist}. Dati demografici Istat aggiornati al 1° gennaio 2026.",
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
                    "name": "{regione}",
                    "item": "https://provinceitalia.it/regioni/{slug_regione}"
                }},{{
                    "@type": "ListItem",
                    "position": 3,
                    "name": "{nome}",
                    "item": "https://provinceitalia.it/province/{slug}"
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
                <h1 class="title">{titolo_ist}</h1>
                <div class="subtitle">
                    <p class="text-subtitle"><a class="a_link" href="https://demo.istat.it/app/?i=POS&l=it" target="_blank">Dati aggiornati al bilancio demografico Istat del 1° gennaio 2026</a></p>
                    <p class="text-subtitle">In <b>grassetto</b> il capoluogo di provincia</p>
                    <p class="text-subtitle"><a class="a_link text-subtitle button pointer select-none" href="../regioni/{slug_regione}.html"><b>← Torna alla regione {regione}</b></a></p>
                </div>
            </div>
            <div class="header3"></div>
        </div>
    </header>
    <main>
        <div class="pannello-info">
            <div class="titolo-div" id="titolo-provincia-div">
                <h2 class="titolo" id="titolo-provincia">{titolo_ist}</h2>
            </div>
            <h4 class="elementi-trovati" id="elementi-trovati">{num_comuni} comuni</h4>
            <input type="text" id="barra-ricerca" class="barra-ricerca" placeholder="Cerca un comune...">
            <table class="tabella" id="elenco-comuni" style="border-width: medium; border-style: none; border-color: currentcolor; border-image: initial;">
                <tbody>
                    {tabella_html}
                </tbody>
            </table>
        </div>
        {svg_evidenziato}
{NAV_REGIONI}
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
                    <img class="github-logo" src="../assets/img/GitHub_Invertocat_White.png" alt="github-logo">GitHub
                </a>
            </p>
        </div>
        <div class="subfooter">
            <p>Fonte mappe:
                <a href="https://simplemaps.com" class="a_link" target="_blank" rel="noopener noreferrer">Simplemaps</a>
                &middot;
                <a class="a_link" href="http://www.inkscape.org" target="_blank" rel="noopener noreferrer">Inkscape</a>
            </p>
            <p><a class="a_link" href="privacy.html">Privacy Policy</a></p>
            <p><a class="a_link" href="sitemap.xml">Mappa del sito</a></p>
            <p><a class="a_link" href="mailto:info@provinceitalia.it">Contattaci</a></p>
        </div>
    </footer>
    <script>
        const nomeRegione = "{regione}";
        const nomeProvincia = "{nome}";
        const slugRegione = "{slug_regione}";
        const slugProvincia = "{slug}";
        let provinciaCorrente = "{nome}";
        let comuniProvincia = [];
        let flagAlfabetico = true;
        let flagAbitanti = false;
    </script>
    <script src="../assets/js/scriptSingolaProvincia.js"></script>
    <script src="../assets/js/ordinamentocomuni.js"></script>
    <script src="../assets/js/ricercacomuni.js"></script>
</body>

</html>"""
    return html


def main():
    os.makedirs("province", exist_ok=True)

    # Cache SVG per regione (ogni SVG viene letto una volta sola)
    cache_svg: dict[str, str] = {}

    generati = 0
    errori = 0

    for nome, id_svg, regione, slug in PROVINCE:
        if regione not in cache_svg:
            cache_svg[regione] = leggi_svg(regione)

        svg_raw = cache_svg[regione]
        contenuto = genera_html(nome, id_svg, regione, slug, svg_raw)

        percorso_out = os.path.join("province", f"{slug}.html")
        with open(percorso_out, "w", encoding="utf-8") as f:
            f.write(contenuto)

        print(f"  ✓ {percorso_out}")
        generati += 1

    print(f"\nGenerati {generati} file HTML nella cartella province/.")
    if errori:
        print(f"Errori: {errori} (controlla i messaggi ATTENZIONE sopra).")


if __name__ == "__main__":
    main()
