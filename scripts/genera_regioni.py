import json
import os
import re

BASE_URL = "https://samuelefrasca.github.io/Province-Italia"

with open("data/province.json", encoding="utf-8") as f:
    province = json.load(f)

def slugify(nome):
    s = nome.lower()
    s = s.replace("'", "-")
    s = s.replace(" ", "-")
    return s

REGIONI = list(province.keys())

TEMPLATE = """\
<!DOCTYPE html>
<html lang="it">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{NOME_REGIONE} | Elenco Comuni e Province d'Italia | Database Popolazione</title>
    <meta name="description"
        content="Elenco completo dei comuni e delle province {DELLA_REGIONE}. Dati demografici Istat aggiornati al 1° gennaio 2026.">
    <meta name="robots" content="index,follow">

    <meta property="og:site_name" content="Elenco Comuni e Province d'Italia | Database Popolazione">
    <meta property="og:title" content="{NOME_REGIONE} | Elenco Comuni e Province d'Italia | Database Popolazione">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://provinceitalia.it/regioni/{SLUG}">
    <meta property="og:image" content="https://provinceitalia.it/assets/img/pi_icon.png">

    <link rel="canonical" href="https://provinceitalia.it/regioni/{SLUG}">
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
            "name": "{NOME_REGIONE} | Elenco Comuni e Province d'Italia | Database Popolazione",
            "url": "https://provinceitalia.it/regioni/{SLUG}",
            "description": "Elenco completo dei comuni e delle province {DELLA_REGIONE}. Dati demografici Istat aggiornati al 1° gennaio 2026.",
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
                    "name": "{NOME_REGIONE}",
                    "item": "https://provinceitalia.it/regioni/{SLUG}"
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
                <h1 class="title">Regione {NOME_REGIONE}</h1>
                <div class="subtitle">
                    <p class="text-subtitle"><a class="a_link" href="https://demo.istat.it/app/?i=POS&l=it" target="_blank">Dati aggiornati al bilancio demografico Istat del 1° gennaio 2026</a></p>
                    <p class="text-subtitle">In <b>grassetto</b> i capoluoghi di provincia</p>
                    <p id="bottone-completo" class="text-subtitle button pointer select-none"><b>Premi qui per vedere
                            l'elenco completo dei comuni</b></p>
                </div>
            </div>
            <div class="header3"></div>
        </div>
    </header>
    <main>
        <div class="pannello-info">
            <div class="titolo-div" id="titolo-provincia-div">
                <h2 class="titolo" id="titolo-provincia">Clicca su una provincia</h2>
            </div>
            <h4 class="elementi-trovati" id="elementi-trovati"></h4>
            <table class="tabella" id="elenco-comuni"></table>
        </div>
        {SVG}
        <nav class="nav-invisibile">
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
</nav>
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
    <script> const nomeRegione = "{NOME_REGIONE}"; </script>
    <script src="../assets/js/scriptcomuni.js"></script>
    <script src="../assets/js/ordinamentocomuni.js"></script>
</body>

</html>"""

# Articolo per "della regione X" nella description
def della_regione(nome):
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

os.makedirs("regioni", exist_ok=True)

for regione in REGIONI:
    slug = slugify(regione)
    svg_path = f"svg/{slug}.svg"

    if not os.path.exists(svg_path):
        print(f"ATTENZIONE: SVG mancante per {regione} ({svg_path})")
        svg_content = "<!-- SVG mancante -->"
    else:
        with open(svg_path, encoding="utf-8") as f:
            righe = f.readlines()
        # dalla riga 4 in poi (indice 3)
        svg_content = "".join(righe[3:]).strip()

    html = TEMPLATE.format(
        NOME_REGIONE=regione,
        SLUG=slug,
        BASE_URL=BASE_URL,
        DELLA_REGIONE=della_regione(regione),
        SVG=svg_content,
    )

    out_path = f"regioni/{slug}.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generato: {out_path}")

print("Fatto.")
