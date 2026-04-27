const provinceItalia = {
    "Valle d'Aosta": [
        { nome: "Aosta", sigla: "AO", abitanti: 122554, capoluogo: true }
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
        { nome: "Perugia", sigla: "PG", abitanti: 636147, capoluogo: true },
        { nome: "Terni", sigla: "TR", abitanti: 214734 }
    ],
    "Marche": [
        { nome: "Ancona", sigla: "AN", abitanti: 461685, capoluogo: true },
        { nome: "Ascoli Piceno", sigla: "AP", abitanti: 200202 },
        { nome: "Fermo", sigla: "FM", abitanti: 166827 },
        { nome: "Macerata", sigla: "MC", abitanti: 301668 },
        { nome: "Pesaro e Urbino", sigla: "PU", abitanti: 349578 }
    ],
    "Lazio": [
        { nome: "Frosinone", sigla: "FR", abitanti: 460598 },
        { nome: "Latina", sigla: "LT", abitanti: 567222 },
        { nome: "Rieti", sigla: "RI", abitanti: 149432 },
        { nome: "Roma", sigla: "RM", abitanti: 4227295, metropolitana: true, capoluogo: true },
        { nome: "Viterbo", sigla: "VT", abitanti: 307849 }
    ],
    "Abruzzo": [
        { nome: "Chieti", sigla: "CH", abitanti: 369311 },
        { nome: "L'Aquila", sigla: "AQ", abitanti: 286808, capoluogo: true },
        { nome: "Pescara", sigla: "PE", abitanti: 311668 },
        { nome: "Teramo", sigla: "TE", abitanti: 299919 }
    ],
    "Molise": [
        { nome: "Campobasso", sigla: "CB", abitanti: 207948, capoluogo: true },
        { nome: "Isernia", sigla: "IS", abitanti: 78282 }
    ],
    "Campania": [
        { nome: "Avellino", sigla: "AV", abitanti: 393292 },
        { nome: "Benevento", sigla: "BN", abitanti: 258105 },
        { nome: "Caserta", sigla: "CE", abitanti: 909469 },
        { nome: "Napoli", sigla: "NA", abitanti: 2955709, metropolitana: true, capoluogo: true },
        { nome: "Salerno", sigla: "SA", abitanti: 1053616 }
    ],
    "Puglia": [
        { nome: "Bari", sigla: "BA", abitanti: 1218345, metropolitana: true, capoluogo: true },
        { nome: "Barletta-Andria-Trani", sigla: "BT", abitanti: 376022 },
        { nome: "Brindisi", sigla: "BR", abitanti: 373790 },
        { nome: "Foggia", sigla: "FG", abitanti: 588112 },
        { nome: "Lecce", sigla: "LE", abitanti: 762300 },
        { nome: "Taranto", sigla: "TA", abitanti: 547928 }
    ],
    "Basilicata": [
        { nome: "Matera", sigla: "MT", abitanti: 187899 },
        { nome: "Potenza", sigla: "PZ", abitanti: 337858, capoluogo: true }
    ],
    "Calabria": [
        { nome: "Catanzaro", sigla: "CZ", abitanti: 338285, capoluogo: true },
        { nome: "Cosenza", sigla: "CS", abitanti: 667643 },
        { nome: "Crotone", sigla: "KR", abitanti: 161820 },
        { nome: "Reggio Calabria", sigla: "RC", abitanti: 510818, metropolitana: true },
        { nome: "Vibo Valentia", sigla: "VV", abitanti: 150041 }
    ],
    "Sicilia": [
        { nome: "Agrigento", sigla: "AG", abitanti: 407250, lbc: true },
        { nome: "Caltanissetta", sigla: "CL", abitanti: 243714, lbc: true },
        { nome: "Catania", sigla: "CT", abitanti: 1067993, metropolitana: true },
        { nome: "Enna", sigla: "EN", abitanti: 151621, lbc: true },
        { nome: "Messina", sigla: "ME", abitanti: 594412, metropolitana: true },
        { nome: "Palermo", sigla: "PA", abitanti: 1195772, metropolitana: true, capoluogo: true },
        { nome: "Ragusa", sigla: "RG", abitanti: 323144, lbc: true },
        { nome: "Siracusa", sigla: "SR", abitanti: 382529, lbc: true },
        { nome: "Trapani", sigla: "TP", abitanti: 410713, lbc: true }
    ],
    "Sardegna": [
        { nome: "Cagliari", sigla: "CA", abitanti: 542470, metropolitana: true, capoluogo: true },
        { nome: "Gallura Nord-Est Sardegna", sigla: "OT", abitanti: 158916 },
        { nome: "Medio Campidano", sigla: "VS", abitanti: 90694 },
        { nome: "Nuoro", sigla: "NU", abitanti: 194616 },
        { nome: "Ogliastra", sigla: "OG", abitanti: 53984 },
        { nome: "Oristano", sigla: "OR", abitanti: 147203 },
        { nome: "Sassari", sigla: "SS", abitanti: 470794, metropolitana: true },
        { nome: "Sulcis Iglesiente", sigla: "SU", abitanti: 131890 }
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
        titoloRegione.textContent = "Province della regione " + nomeRegione + ":";

        // Crea i punti elenco per ogni provincia
        let table = elencoProvince.innerHTML
        table = `<tr><th class="hel pointer" onclick="ordinaPerNome(flagAlfabetico)">Nome <i class="fa-solid fa-sort"></i></th><th class="hel">Sigla</th><th class="hel pointer" onclick="ordinaPerAbitanti(flagAbitanti)">Popolazione <i class="fa-solid fa-sort"></i></th></tr>`
        let popolazioneTotale = 0;

        for (let provincia of provinceTrovate) {
            // distinzione città metropolitane, lbc e province autonome
            let index = '';
            if (provincia.metropolitana) {
                index = '<sup>[1]</sup>'
            }
            if (provincia.lbc) {
                index = '<sup>[2]</sup>'
            }
            if (provincia.autonoma) {
                index = '<sup>[3]</sup>'
            }
            if (provincia.eddr) {
                index = '<sup>[4]</sup>'
            }
            // creazione tabella
            if (provincia.capoluogo) {
                table += `<tr><td class="el nome"><strong>${provincia.nome} ${index}</strong></td><td class="el sigla"><strong>${provincia.sigla}</strong></td><td class="el abitanti"><strong>${provincia.abitanti.toLocaleString('it-IT')}</strong></td></tr>`;
            }
            else {
                table += `<tr><td class="el nome">${provincia.nome} ${index}</td><td class="el sigla">${provincia.sigla}</td><td class="el abitanti">${provincia.abitanti.toLocaleString('it-IT')}</td></tr>`;
            }
            // aggiornamento popolazione totale della regione
            popolazioneTotale += provincia.abitanti;
        }
        table += `<tr><td class="hel nome"><strong>Popolazione totale</strong></td><td class="hel sigla"><strong></strong></td><td class="hel abitanti"><strong>${popolazioneTotale.toLocaleString('it-IT')}</strong></td></tr>`
        elencoProvince.innerHTML = table

        // Legenda
        let legenda = legendaProvince.innerHTML
        if (nomeRegione === "Valle d'Aosta") {
            legenda = `<p><strong>La regione autonoma della Valle d'Aosta svolge anche le funzioni provinciali e, in elaborazioni statistiche, è considerata una provincia.</strong></p>`
        }
        legenda += `<h3 class="title-legend">Legenda</h3><ol><li>Città metropolitana</li><li>Libero consorzio comunale</li><li>Provincia autonoma</li><li>Ente di decentramento regionale</li></ol>`
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