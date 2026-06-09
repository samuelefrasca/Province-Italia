const titoloProvincia = document.getElementById('titolo-provincia');
const elencoComuni = document.getElementById('elenco-comuni');
const province = document.querySelectorAll('g[id]');
const bottonecompleto = document.getElementById('bottone-completo');
const elementiTrovati = document.getElementById('elementi-trovati');

// nomeRegione è il nome del file html preso in considerazione
const percorsoFile = window.location.pathname;
const nomeRegioneHtmlDominio = percorsoFile.split('/').pop();
const nomeRegioneHtml = nomeRegioneHtmlDominio.split('.')[0];

let provinciaCorrente = "";
let comuniProvincia = [];
let flagAlfabetico = true;
let flagAbitanti = false;

bottonecompleto.addEventListener('click', () => {
    elencoCompleto(nomeRegione, nomeRegioneHtml, nomeRegione);
});

province.forEach(provincia => {
    provincia.addEventListener('click', () => {
        const nomeProvincia = provincia.id;
        const nomeProvinciaHtml = nomeProvincia.toLowerCase().replaceAll(" ", "-").replaceAll("'", "-");
        fetch('../data/' + nomeRegioneHtml + '/' + nomeProvinciaHtml + '.json')
            .then(res => res.json())
            .then(data => {
                comuniProvincia = data;
                provinciaCorrente = nomeProvincia;
                scritturaComuni(nomeProvincia, comuniProvincia, nomeRegione);
                flagAlfabetico = true;
                flagAbitanti = false;
            })
    });
});

const cittaMetropolitane = [
    "Bari",
    "Bologna",
    "Cagliari",
    "Catania",
    "Firenze",
    "Genova",
    "Messina",
    "Milano",
    "Napoli",
    "Palermo",
    "Reggio Calabria",
    "Roma",
    "Sassari",
    "Torino",
    "Venezia"
];

function scritturaComuni(provincia, comuniProvincia, nomeRegione) {
    elencoComuni.innerHTML = '';
    if (elencoComuni.innerHTML == '') {
        elencoComuni.style.border = 'none';
    }
    else {
        elencoComuni.style.border = "1px solid black";
    }

    let cittaMetropolitana = false;
    for (let el of cittaMetropolitane) {
        if (provincia == el) {
            cittaMetropolitana = true;
            break;
        }
    }

    if (provincia == nomeRegione) {
        titoloProvincia.textContent = "Elenco completo dei comuni della regione " + provincia;
    }
    // In questo punto trattiamo i casi particolari in cui il nome della provincia non si limita a "Provincia di"
    else if (provincia == "Roma") {
        titoloProvincia.textContent = "Città metropolitana di " + provincia + " Capitale";
    }
    else if (provincia == "Monza e Brianza") {
        titoloProvincia.textContent = "Provincia di Monza e della Brianza";
    }
    else if (provincia == "Bolzano") {
        titoloProvincia.textContent = "Provincia autonoma di Bolzano - Alto Adige";
    }
    else if (provincia == "L'Aquila") {
        titoloProvincia.textContent = "Provincia dell'Aquila";
    }
    else if (provincia == "La Spezia") {
        titoloProvincia.textContent = "Provincia della Spezia";
    }
    else if (provincia == "Gallura Nord-Est Sardegna") {
        titoloProvincia.textContent = "Provincia della Gallura Nord-Est Sardegna";
    }
    else if (provincia == "Medio Campidano") {
        titoloProvincia.textContent = "Provincia del Medio Campidano";
    }
    else if (provincia == "Ogliastra") {
        titoloProvincia.textContent = "Provincia dell'Ogliastra";
    }
    else if (provincia == "Sulcis Iglesiente") {
        titoloProvincia.textContent = "Provincia del Sulcis Iglesiente";
    }
    else if (provincia == "Verbano-Cusio-Ossola") {
        titoloProvincia.textContent = "Provincia del Verbano-Cusio-Ossola";
    }
    // Qui si distinguono i casi restanti, divisi nei vari enti regionali d'Italia
    else if (cittaMetropolitana) {
        titoloProvincia.textContent = "Città metropolitana di " + provincia;
    }
    else if (nomeRegione == "Sicilia") {
        titoloProvincia.textContent = "Libero consorzio comunale di " + provincia;
    }
    else if (nomeRegione == "Friuli-Venezia Giulia") {
        titoloProvincia.textContent = "Ente di decentramento regionale di " + provincia;
    }
    else if (nomeRegione == "Trentino-Alto Adige") {
        titoloProvincia.textContent = "Provincia autonoma di " + provincia;
    }
    else {
        titoloProvincia.textContent = "Provincia di " + provincia;
    }

    // Crea i punti elenco per ogni provincia
    let table = elencoComuni.innerHTML;
    table = `<tr><th class="index"></th><th class="hel nome pointer select-none" onclick="ordinaPerNome(flagAlfabetico)">Comune <i class="fa-solid fa-sort"></i></th><th class="hel select-none">Provincia</th><th class="hel sigla select-none">Sigla</th><th class="hel abitanti pointer select-none" onclick="ordinaPerAbitanti(flagAbitanti)">Popolazione <i class="fa-solid fa-sort"></i></th></tr>`;
    let popolazioneTotale = 0;
    let index = 1; // indice
    for (let comune of comuniProvincia) {
        // creazione tabella
        if (comune.capoluogo) {
            table += `<tr><td class="el index"><strong>${index}</strong></td><td class="el nome"><strong>${comune.comune}</strong></td><td class="el"><strong>${comune.provincia}</strong></td><td class="el sigla"><strong>${comune.sigla}</strong></td><td class="el abitanti"><strong>${comune.popolazione_totale.toLocaleString('it-IT', { useGrouping: 'always' })}</strong></td></tr>`;
        }
        else {
            table += `<tr><td class="el index">${index}</td><td class="el nome">${comune.comune}</td><td class="el">${comune.provincia}</td><td class="el sigla">${comune.sigla}</td><td class="el abitanti">${comune.popolazione_totale.toLocaleString('it-IT', { useGrouping: 'always' })}</td></tr>`;
        }
        // aggiornamento popolazione totale della regione e l'indice
        popolazioneTotale += comune.popolazione_totale;
        index++;
    }
    table += `<tr><td class="index"></td><td class="fel nome"><strong>Popolazione totale</strong></td><td class="fel"><strong></strong></td><td class="fel sigla"><strong></strong></td><td class="fel abitanti"><strong>${popolazioneTotale.toLocaleString('it-IT')}</strong></td></tr>`;
    elencoComuni.innerHTML = table;

    // Numero elementi trovati
    elementiTrovati.textContent = `${index - 1} comuni`;
}

function elencoCompleto(nomeRegione, nomeRegioneHtml) {
    fetch('../data/province.json')
        .then(res => res.json())
        .then(data => {
            let elencoProvince = data[nomeRegione];
            let elencoTotale = [];
            let contatore = 0;

            elencoProvince.forEach(el => {
                fetch('../data/' + nomeRegioneHtml.toLowerCase().replaceAll(" ", "-").replaceAll("'", "-") + '/' + el.nome.toLowerCase().replaceAll(" ", "-").replaceAll("'", "-") + '.json')
                    .then(res => res.json())
                    .then(dataComuni => {
                        elencoTotale.push(...dataComuni);
                        contatore++;

                        // Scrivi solo quando hai ricevuto tutti i file
                        if (contatore === elencoProvince.length) {
                            elencoTotale.sort((a, b) => a.comune.localeCompare(b.comune));
                            provinciaCorrente = nomeRegione;
                            comuniProvincia = elencoTotale;
                            scritturaComuni(nomeRegione, elencoTotale, nomeRegione);
                            flagAlfabetico = true;
                            flagAbitanti = false;
                        }
                    });
            });
        });
}

// Se siamo in Valle d'Aosta, essendoci un solo elenco possibile, lo facciamo partire direttamente senza dover selezionare la provincia
if (nomeRegione == "Valle d'Aosta") {
    fetch("../data/valle-d-aosta/valle-d-aosta.json")
        .then(res => res.json())
        .then(data => {
            scritturaComuni("Valle d'Aosta", data, "Valle d'Aosta");
        })
}