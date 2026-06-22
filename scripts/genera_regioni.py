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
            <ul>
                <li><a href="abruzzo.html">Abruzzo</a></li>
                <li><a href="basilicata.html">Basilicata</a></li>
                <li><a href="calabria.html">Calabria</a></li>
                <li><a href="campania.html">Campania</a></li>
                <li><a href="emilia-romagna.html">Emilia-Romagna</a></li>
                <li><a href="friuli-venezia-giulia.html">Friuli-Venezia Giulia</a></li>
                <li><a href="lazio.html">Lazio</a></li>
                <li><a href="liguria.html">Liguria</a></li>
                <li><a href="lombardia.html">Lombardia</a></li>
                <li><a href="marche.html">Marche</a></li>
                <li><a href="molise.html">Molise</a></li>
                <li><a href="piemonte.html">Piemonte</a></li>
                <li><a href="puglia.html">Puglia</a></li>
                <li><a href="sardegna.html">Sardegna</a></li>
                <li><a href="sicilia.html">Sicilia</a></li>
                <li><a href="toscana.html">Toscana</a></li>
                <li><a href="trentino-alto-adige.html">Trentino-Alto Adige</a></li>
                <li><a href="umbria.html">Umbria</a></li>
                <li><a href="valle-d-aosta.html">Valle d'Aosta</a></li>
                <li><a href="veneto.html">Veneto</a></li>
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
            <p><a class="a_link" href="mailto:info@unidirectory.it">Contattaci</a></p>
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
