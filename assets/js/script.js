const provinceItalia = {
    "Valle d'Aosta": [
        { nome: "Aosta", sigla: "AO", abitanti: 122554, capoluogo: true, vda: true }
    ],
    "Piemonte": [
        { nome: "Alessandria", sigla: "AL", abitanti: 408063 },
        { nome: "Asti", sigla: "AT", abitanti: 207059 },
        { nome: "Biella", sigla: "BI", abitanti: 168223 },
        { nome: "Cuneo", sigla: "CN", abitanti: 582109 },
        { nome: "Novara", sigla: "NO", abitanti: 365930 },
        { nome: "Torino", sigla: "TO", abitanti: 2204779, metropolitana: true, capoluogo: true },
        { nome: "Verbano-Cusio-Ossola", sigla: "VB", abitanti: 152677 },
        { nome: "Vercelli", sigla: "VC", abitanti: 166166 }
    ],
    "Liguria": [
        { nome: "Genova", sigla: "GE", abitanti: 820691, metropolitana: true, capoluogo: true },
        { nome: "Imperia", sigla: "IM", abitanti: 209848 },
        { nome: "La Spezia", sigla: "SP", abitanti: 214539 },
        { nome: "Savona", sigla: "SV", abitanti: 266910 }
    ],
    "Lombardia": [
        { nome: "Bergamo", sigla: "BG", abitanti: 1119233 },
        { nome: "Brescia", sigla: "BS", abitanti: 1271759 },
        { nome: "Como", sigla: "CO", abitanti: 598562 },
        { nome: "Cremona", sigla: "CR", abitanti: 355134 },
        { nome: "Lecco", sigla: "LC", abitanti: 334211 },
        { nome: "Lodi", sigla: "LO", abitanti: 231481 },
        { nome: "Milano", sigla: "MI", abitanti: 3253111, metropolitana: true, capoluogo: true },
        { nome: "Mantova", sigla: "MN", abitanti: 408715 },
        { nome: "Monza e Brianza", sigla: "MB", abitanti: 883396 },
        { nome: "Pavia", sigla: "PV", abitanti: 546023 },
        { nome: "Sondrio", sigla: "SO", abitanti: 179268 },
        { nome: "Varese", sigla: "VA", abitanti: 884801 }
    ],
    "Trentino-Alto Adige": [
        { nome: "Bolzano", sigla: "BZ", abitanti: 542134, autonoma: true },
        { nome: "Trento", sigla: "TN", abitanti: 548684, autonoma: true, capoluogo: true }
    ],
    "Veneto": [
        { nome: "Belluno", sigla: "BL", abitanti: 197265 },
        { nome: "Padova", sigla: "PD", abitanti: 934540 },
        { nome: "Rovigo", sigla: "RO", abitanti: 227183 },
        { nome: "Treviso", sigla: "TV", abitanti: 878341 },
        { nome: "Venezia", sigla: "VE", abitanti: 834077, metropolitana: true, capoluogo: true },
        { nome: "Verona", sigla: "VR", abitanti: 930842 },
        { nome: "Vicenza", sigla: "VI", abitanti: 855212 }
    ],
    "Friuli Venezia Giulia": [
        { nome: "Gorizia", sigla: "GO", abitanti: 138717, eddr: true },
        { nome: "Pordenone", sigla: "PN", abitanti: 311114, eddr: true },
        { nome: "Trieste", sigla: "TS", abitanti: 227840, eddr: true, capoluogo: true },
        { nome: "Udine", sigla: "UD", abitanti: 515825, eddr: true }
    ],
    "Emilia-Romagna": [
        { nome: "Bologna", sigla: "BO", abitanti: 1024290, metropolitana: true, capoluogo: true },
        { nome: "Ferrara", sigla: "FE", abitanti: 340482 },
        { nome: "Forlì-Cesena", sigla: "FC", abitanti: 394337 },
        { nome: "Modena", sigla: "MO", abitanti: 711502 },
        { nome: "Parma", sigla: "PR", abitanti: 457509 },
        { nome: "Piacenza", sigla: "PC", abitanti: 287745 },
        { nome: "Ravenna", sigla: "RA", abitanti: 387743 },
        { nome: "Reggio Emilia", sigla: "RE", abitanti: 532157 },
        { nome: "Rimini", sigla: "RN", abitanti: 341244 }
    ],
    "Toscana": [
        { nome: "Arezzo", sigla: "AR", abitanti: 333269 },
        { nome: "Firenze", sigla: "FI", abitanti: 988494, metropolitana: true, capoluogo: true },
        { nome: "Grosseto", sigla: "GR", abitanti: 214863 },
        { nome: "Livorno", sigla: "LI", abitanti: 324893 },
        { nome: "Lucca", sigla: "LU", abitanti: 379957 },
        { nome: "Massa-Carrara", sigla: "MS", abitanti: 186637 },
        { nome: "Pisa", sigla: "PI", abitanti: 419588 },
        { nome: "Pistoia", sigla: "PT", abitanti: 290867 },
        { nome: "Prato", sigla: "PO", abitanti: 261152 },
        { nome: "Siena", sigla: "SI", abitanti: 259502 }
    ],
    "Umbria": [
        { nome: "Perugia", sigla: "PG", abitanti: 635988, capoluogo: true },
        { nome: "Terni", sigla: "TR", abitanti: 214639 }
    ],
    "Marche": [
        { nome: "Ancona", sigla: "AN", abitanti: 461613, capoluogo: true },
        { nome: "Ascoli Piceno", sigla: "AP", abitanti: 200202 },
        { nome: "Fermo", sigla: "FM", abitanti: 166772 },
        { nome: "Macerata", sigla: "MC", abitanti: 301689 },
        { nome: "Pesaro e Urbino", sigla: "PU", abitanti: 349556 }
    ],
    "Lazio": [
        { nome: "Frosinone", sigla: "FR", abitanti: 460266 },
        { nome: "Latina", sigla: "LT", abitanti: 567130 },
        { nome: "Rieti", sigla: "RI", abitanti: 149335 },
        { nome: "Roma", sigla: "RM", abitanti: 4224901, metropolitana: true, capoluogo: true },
        { nome: "Viterbo", sigla: "VT", abitanti: 307812 }
    ],
    "Abruzzo": [
        { nome: "Chieti", sigla: "CH", abitanti: 369059 },
        { nome: "L'Aquila", sigla: "AQ", abitanti: 286765, capoluogo: true },
        { nome: "Pescara", sigla: "PE", abitanti: 311563 },
        { nome: "Teramo", sigla: "TE", abitanti: 299835 }
    ],
    "Molise": [
        { nome: "Campobasso", sigla: "CB", abitanti: 207723, capoluogo: true },
        { nome: "Isernia", sigla: "IS", abitanti: 78217 }
    ],
    "Campania": [
        { nome: "Avellino", sigla: "AV", abitanti: 393093 },
        { nome: "Benevento", sigla: "BN", abitanti: 257968 },
        { nome: "Caserta", sigla: "CE", abitanti: 909493 },
        { nome: "Napoli", sigla: "NA", abitanti: 2954847, metropolitana: true, capoluogo: true },
        { nome: "Salerno", sigla: "SA", abitanti: 1053302 }
    ],
    "Puglia": [
        { nome: "Bari", sigla: "BA", abitanti: 1218073, metropolitana: true, capoluogo: true },
        { nome: "Barletta-Andria-Trani", sigla: "BT", abitanti: 375933 },
        { nome: "Brindisi", sigla: "BR", abitanti: 373631 },
        { nome: "Foggia", sigla: "FG", abitanti: 587785 },
        { nome: "Lecce", sigla: "LE", abitanti: 761927 },
        { nome: "Taranto", sigla: "TA", abitanti: 547928 }
    ],
    "Basilicata": [
        { nome: "Matera", sigla: "MT", abitanti: 187754 },
        { nome: "Potenza", sigla: "PZ", abitanti: 337527, capoluogo: true }
    ],
    "Calabria": [
        { nome: "Catanzaro", sigla: "CZ", abitanti: 338160, capoluogo: true },
        { nome: "Cosenza", sigla: "CS", abitanti: 667134 },
        { nome: "Crotone", sigla: "KR", abitanti: 161765 },
        { nome: "Reggio Calabria", sigla: "RC", abitanti: 510590, metropolitana: true },
        { nome: "Vibo Valentia", sigla: "VV", abitanti: 149922 }
    ],
    "Sicilia": [
        { nome: "Agrigento", sigla: "AG", abitanti: 407041, lbc: true },
        { nome: "Caltanissetta", sigla: "CL", abitanti: 243501, lbc: true },
        { nome: "Catania", sigla: "CT", abitanti: 1067550, metropolitana: true },
        { nome: "Enna", sigla: "EN", abitanti: 151525, lbc: true },
        { nome: "Messina", sigla: "ME", abitanti: 594074, metropolitana: true },
        { nome: "Palermo", sigla: "PA", abitanti: 1195307, metropolitana: true, capoluogo: true },
        { nome: "Ragusa", sigla: "RG", abitanti: 323144, lbc: true },
        { nome: "Siracusa", sigla: "SR", abitanti: 382450, lbc: true },
        { nome: "Trapani", sigla: "TP", abitanti: 410602, lbc: true }
    ],
    "Sardegna": [
        { nome: "Cagliari", sigla: "CA", abitanti: 536245, metropolitana: true, capoluogo: true },
        { nome: "Gallura Nord-Est Sardegna", sigla: "OT", abitanti: 159222 },
        { nome: "Medio Campidano", sigla: "VS", abitanti: 90045 },
        { nome: "Nuoro", sigla: "NU", abitanti: 143262 },
        { nome: "Ogliastra", sigla: "OG", abitanti: 53984 },
        { nome: "Oristano", sigla: "OR", abitanti: 148005 },
        { nome: "Sassari", sigla: "SS", abitanti: 312735, metropolitana: true },
        { nome: "Sulcis Iglesiente", sigla: "SU", abitanti: 118883 }
    ]
};

const regioni = document.querySelectorAll('path');
const titoloRegione = document.getElementById('titolo-regione');
const elencoProvince = document.getElementById('elenco-province');
const legendaProvince = document.getElementById('legenda');

function scritturaProvince(nomeRegione, provinceTrovate) {
    elencoProvince.innerHTML = ''; // Svuota la lista vecchia
    legendaProvince.innerHTML = '';
    if (elencoProvince.innerHTML == '') {
        elencoProvince.style.border = 'none'
    }
    else {
        elencoProvince.style.border = "1px solid black"
    }

    if (provinceTrovate) {
        // Se trova i dati, cambia il titolo
        if(nomeRegione == "Italia"){     
            titoloRegione.textContent = "Elenco completo delle province d'Italia";
        }
        else {
            titoloRegione.textContent = "Province della regione " + nomeRegione;
        }

        // Crea i punti elenco per ogni provincia
        let table = elencoProvince.innerHTML
        table = `<tr><th class="index"></th><th class="hel pointer select-none" onclick="ordinaPerNome(flagAlfabetico)">Nome <i class="fa-solid fa-sort"></i></th><th class="hel select-none">Sigla</th><th class="hel pointer select-none" onclick="ordinaPerAbitanti(flagAbitanti)">Popolazione <i class="fa-solid fa-sort"></i></th></tr>`
        let popolazioneTotale = 0;
        let index = 1; // indice
        for (let provincia of provinceTrovate) {
            // distinzione città metropolitane, lbc e province autonome
            let apex = '';
            if (provincia.metropolitana) {
                apex = '<sup class="pointer" title="Città metropolitana"><a class="sup" href="#legenda">[1]</a></sup>'
            }
            if (provincia.lbc) {
                apex = '<sup class="pointer" title="Libero consorzio comunale"><a class="sup" href="#legenda">[2]</a></sup>'
            }
            if (provincia.autonoma) {
                apex = '<sup class="pointer" title="Provincia autonoma"><a class="sup" href="#legenda">[3]</a></sup>'
            }
            if (provincia.eddr) {
                apex = '<sup class="pointer" title="Ente di decentramento regionale"><a class="sup" href="#legenda">[4]</a></sup>'
            }
            if (provincia.vda) {
                apex = '<sup class="pointer" title="Regione autonoma della Valle d\'Aosta (premi per vedere i dettagli)"><a class="sup" href="#legenda">[5]</a></sup>'
            }
            // creazione tabella
            if (provincia.capoluogo) {
                table += `<tr><td class="el index"><strong>${index}</strong></td><td class="el nome"><strong>${provincia.nome} ${apex}</strong></td><td class="el sigla"><strong>${provincia.sigla}</strong></td><td class="el abitanti"><strong>${provincia.abitanti.toLocaleString('it-IT')}</strong></td></tr>`;
            }
            else {
                table += `<tr><td class="el index">${index}</td><td class="el nome">${provincia.nome} ${apex}</td><td class="el sigla">${provincia.sigla}</td><td class="el abitanti">${provincia.abitanti.toLocaleString('it-IT')}</td></tr>`;
            }
            // aggiornamento popolazione totale della regione e l'indice
            popolazioneTotale += provincia.abitanti;
            index++;
        }
        table += `<tr><td class="index"></td><td class="hel nome"><strong>Popolazione totale</strong></td><td class="hel sigla"><strong></strong></td><td class="hel abitanti"><strong>${popolazioneTotale.toLocaleString('it-IT')}</strong></td></tr>`
        elencoProvince.innerHTML = table

        // Legenda
        let legenda = legendaProvince.innerHTML
        legenda += `<h3 class="title-legend">Legenda</h3><ol><li>Città metropolitana</li><li>Libero consorzio comunale</li><li>Provincia autonoma</li><li>Ente di decentramento regionale</li>`
        if (nomeRegione === "Valle d'Aosta" || nomeRegione === "Italia" ) {
            legenda += `<li><strong>La regione autonoma della Valle d'Aosta esercita anche le funzioni provinciali e, nelle elaborazioni statistiche, è considerata una provincia. Di conseguenza, Aosta è sede provinciale oltre che capoluogo di regione.</strong></li>`
        }
        legenda += `</ol>`
        legendaProvince.innerHTML = legenda;
    } else {
        // Se clicchi una regione non ancora presente nel database
        titoloRegione.textContent = nomeRegione + " (Dati da inserire)";
    }
}

let regioneCorrente = "";
let provinceCorrenti = [];
let flagAbitanti = false;
let flagAlfabetico = true;

regioni.forEach(regione => {
    regione.addEventListener('click', () => {
        const nomeRegione = regione.getAttribute('name'); // Legge il nome dall'SVG
        regioneCorrente = nomeRegione;
        const provinceTrovate = provinceItalia[nomeRegione]; // Cerca il nome nel Database
        provinceCorrenti = provinceTrovate;
        scritturaProvince(regioneCorrente, provinceCorrenti);
        flagAlfabetico = true;
        flagAbitanti = false;
    })
});

function elencoCompleto() {
    let italia = "Italia"
    const elencoTotale = [];
    for (let el in provinceItalia) {
        for (let il of provinceItalia[el]) {
            elencoTotale.push(il);
        }
    }
    elencoTotale.sort((a, b) => {
        if(a.nome<b.nome)
            return -1;
        if(a.nome>b.nome)
            return 1;
        return 0;
    });
    provinceCorrenti = elencoTotale;
    regioneCorrente = italia;
    scritturaProvince(italia, elencoTotale);
    flagAlfabetico = true;
    flagAbitanti = false;
}

// Funzioni di ordinamento
function ordinaPerAbitantiDecrescente(provinceCorrenti) {
    let copiaProvince = [...provinceCorrenti];
    copiaProvince.sort((a, b) => {
        return a.abitanti - b.abitanti;
    })
    scritturaProvince(regioneCorrente, copiaProvince);
}

function ordinaPerAbitantiCrescente(provinceCorrenti) {
    let copiaProvince = [...provinceCorrenti];
    copiaProvince.sort((a, b) => {
        return b.abitanti - a.abitanti;
    })
    scritturaProvince(regioneCorrente, copiaProvince);
}

function ordinaPerAbitanti(flag) {
    if (flag) {
        ordinaPerAbitantiDecrescente(provinceCorrenti);
        flagAbitanti = false;
        flagAlfabetico = false;
    }
    if (!flag) {
        ordinaPerAbitantiCrescente(provinceCorrenti);
        flagAbitanti = true;
        flagAlfabetico = false;
    }
}

function ordinaPerNome(flag) {
    // parte dal presupposto che l'oggetto di riferimento sia già ordinato in ordine alfabetico
    if (flag) {
        scritturaProvince(regioneCorrente, provinceCorrenti.toReversed());
        flagAlfabetico = false;
        flagAbitanti = false;
    }
    if (!flag) {
        scritturaProvince(regioneCorrente, provinceCorrenti);
        flagAlfabetico = true;
        flagAbitanti = false;
    }
}