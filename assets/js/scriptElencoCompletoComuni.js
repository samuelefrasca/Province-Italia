// La variabile `tuttiComuni` viene definita inline in comuni.html tramite genera_comuni.py

let comuniFiltrati = [...tuttiComuni];
let flagAlfabetico = true;
let flagAbitanti = false;
let flagProvincia = false;
let flagRegione = false;

const regioniCapoluoghi = {
    'Abruzzo': "L'Aquila",
    'Basilicata': 'Potenza',
    'Calabria': 'Catanzaro',
    'Campania': 'Napoli',
    'Emilia-Romagna': 'Bologna',
    'Friuli-Venezia Giulia': 'Trieste',
    'Lazio': 'Roma',
    'Liguria': 'Genova',
    'Lombardia': 'Milano',
    'Marche': 'Ancona',
    'Molise': 'Campobasso',
    'Piemonte': 'Torino',
    'Puglia': 'Bari',
    'Sardegna': 'Cagliari',
    'Sicilia': 'Palermo',
    'Toscana': 'Firenze',
    'Trentino-Alto Adige': 'Trento',
    'Umbria': 'Perugia',
    'Valle d\'Aosta': 'Aosta',
    'Veneto': 'Venezia'
};

function getClassiRiga(c) {
    const classi = [];
    if (c.capoluogo) {
        classi.push('capoluogo-provincia');
    }
    if (c.comune === regioniCapoluoghi[c.regione]) {
        classi.push('capoluogo-regione');
    }
    return classi;
}

function formattaNumero(n) {
    return n.toLocaleString('it-IT', { useGrouping: 'always' });
}

function slugifyTesto(valore) {
    return String(valore)
        .normalize('NFKD')
        .replace(/[\u0300-\u036f]/g, '')
        .toLowerCase()
        .trim()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/(^-|-$)/g, '');
}

function getSlugProvincia(nomeProvincia) {
    return nomeProvincia ? slugifyTesto(nomeProvincia) : '';
}

function getSlugRegione(nomeRegione) {
    if (!nomeRegione) {
        return '';
    }

    const slugRegioni = {
        'Abruzzo': 'abruzzo',
        'Basilicata': 'basilicata',
        'Calabria': 'calabria',
        'Campania': 'campania',
        'Emilia-Romagna': 'emilia-romagna',
        'Friuli-Venezia Giulia': 'friuli-venezia-giulia',
        'Lazio': 'lazio',
        'Liguria': 'liguria',
        'Lombardia': 'lombardia',
        'Marche': 'marche',
        'Molise': 'molise',
        'Piemonte': 'piemonte',
        'Puglia': 'puglia',
        'Sardegna': 'sardegna',
        'Sicilia': 'sicilia',
        'Toscana': 'toscana',
        'Trentino-Alto Adige': 'trentino-alto-adige',
        'Umbria': 'umbria',
        'Valle d\'Aosta': 'valle-d-aosta',
        'Veneto': 'veneto'
    };

    return slugRegioni[nomeRegione] || slugifyTesto(nomeRegione);
}

function scriviTabella(comuni) {
    const tabella = document.getElementById('elenco-comuni');
    const elementiTrovati = document.getElementById('elementi-trovati');

    let html = '<tr>'
        + '<th class="index"></th>'
        + '<th class="hel nome pointer select-none" onclick="ordinaPerNome(flagAlfabetico)">Comune <i class="fa-solid fa-sort"></i></th>'
        + '<th class="hel provincia pointer select-none" onclick="ordinaPerProvincia(flagProvincia)">Provincia <i class="fa-solid fa-sort"></i></th>'
        + '<th class="hel regione pointer select-none" onclick="ordinaPerRegione(flagRegione)">Regione <i class="fa-solid fa-sort"></i></th>'
        + '<th class="hel abitanti pointer select-none" onclick="ordinaPerAbitanti(flagAbitanti)">Popolazione <i class="fa-solid fa-sort"></i></th>'
        + '</tr>';

    let popolazioneTotale = 0;
    for (let i = 0; i < comuni.length; i++) {
        const c = comuni[i];
        const pop = formattaNumero(c.popolazione_totale);
        popolazioneTotale += c.popolazione_totale;
        const classi = getClassiRiga(c);
        const classiAttr = classi.length > 0 ? ' class="' + classi.join(' ') + '"' : '';
        const provinciaHtml = c.provincia
            ? '<a class="comunihref" href="/province/' + getSlugProvincia(c.provincia) + '.html">' + c.provincia + '</a>'
            : '';
        const regioneHtml = c.regione
            ? '<a class="comunihref" href="/regioni/' + getSlugRegione(c.regione) + '.html">' + c.regione + '</a>'
            : '';
        html += '<tr' + classiAttr + '>'
            + '<td class="el index' + (classi.includes('capoluogo-provincia') ? ' capoluogo-provincia-cell' : '') + '">' + (i + 1) + '</td>'
            + '<td class="el nome' + (classi.includes('capoluogo-provincia') ? ' capoluogo-provincia-cell' : '') + '">' + c.comune + '</td>'
            + '<td class="el provincia' + (classi.includes('capoluogo-provincia') ? ' capoluogo-provincia-cell' : '') + '">' + provinciaHtml + '</td>'
            + '<td class="el regione' + (classi.includes('capoluogo-provincia') ? ' capoluogo-provincia-cell' : '') + '">' + regioneHtml + '</td>'
            + '<td class="el abitanti' + (classi.includes('capoluogo-provincia') ? ' capoluogo-provincia-cell' : '') + '">' + pop + '</td>'
            + '</tr>';
    }

    html += '<tr>'
        + '<td class="index"></td>'
        + '<td class="fel nome"><strong>Popolazione totale</strong></td>'
        + '<td class="fel provincia"><strong></strong></td>'
        + '<td class="fel regione"><strong></strong></td>'
        + '<td class="fel abitanti"><strong>' + formattaNumero(popolazioneTotale) + '</strong></td>'
        + '</tr>';

    tabella.innerHTML = html;
    elementiTrovati.textContent = comuni.length + ' comuni';
}

// Ordinamento per nome comune
function ordinaPerNome(flag) {
    if (flag) {
        comuniFiltrati.sort((a, b) => b.comune.localeCompare(a.comune, 'it'));
        flagAlfabetico = false;
    } else {
        comuniFiltrati.sort((a, b) => a.comune.localeCompare(b.comune, 'it'));
        flagAlfabetico = true;
    }
    flagAbitanti = false;
    flagProvincia = false;
    flagRegione = false;
    scriviTabella(comuniFiltrati);
}

// Ordinamento per provincia
function ordinaPerProvincia(flag) {
    if (flag) {
        comuniFiltrati.sort((a, b) => b.provincia.localeCompare(a.provincia, 'it'));
        flagProvincia = false;
    } else {
        comuniFiltrati.sort((a, b) => a.provincia.localeCompare(b.provincia, 'it'));
        flagProvincia = true;
    }
    flagAlfabetico = false;
    flagAbitanti = false;
    flagRegione = false;
    scriviTabella(comuniFiltrati);
}

// Ordinamento per regione
function ordinaPerRegione(flag) {
    if (flag) {
        comuniFiltrati.sort((a, b) => b.regione.localeCompare(a.regione, 'it'));
        flagRegione = false;
    } else {
        comuniFiltrati.sort((a, b) => a.regione.localeCompare(b.regione, 'it'));
        flagRegione = true;
    }
    flagAlfabetico = false;
    flagAbitanti = false;
    flagProvincia = false;
    scriviTabella(comuniFiltrati);
}

// Ordinamento per abitanti
function ordinaPerAbitanti(flag) {
    if (flag) {
        comuniFiltrati.sort((a, b) => a.popolazione_totale - b.popolazione_totale);
        flagAbitanti = false;
    } else {
        comuniFiltrati.sort((a, b) => b.popolazione_totale - a.popolazione_totale);
        flagAbitanti = true;
    }
    flagAlfabetico = false;
    flagProvincia = false;
    flagRegione = false;
    scriviTabella(comuniFiltrati);
}

// Barra di ricerca
document.getElementById('barra-ricerca').addEventListener('keyup', function () {
    const filtro = this.value.toLowerCase();
    if (filtro === '') {
        comuniFiltrati = [...tuttiComuni];
    } else {
        comuniFiltrati = tuttiComuni.filter(c =>
            c.comune.toLowerCase().includes(filtro)
        );
    }
    flagAlfabetico = true;
    flagAbitanti = false;
    flagProvincia = false;
    flagRegione = false;
    scriviTabella(comuniFiltrati);
});