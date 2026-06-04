const titoloRegioneDiv = document.getElementById('titolo-regione-div');
const elencoProvince = document.getElementById('elenco-province');
const elementiTrovati = document.getElementById('elementi-trovati');
const legendaProvince = document.getElementById('legenda');

function scritturaProvince(nomeRegione, provinceTrovate) {
    elencoProvince.innerHTML = ''; // Svuota la lista vecchia
    legendaProvince.innerHTML = '';
    if (elencoProvince.innerHTML == '') {
        elencoProvince.style.border = 'none';
    }
    else {
        elencoProvince.style.border = "1px solid black";
    }

    if (nomeRegione == "Italia") {
        titoloRegioneDiv.innerHTML = `<h2 class="titolo" id="titolo-regione">Elenco completo delle province d'Italia</h2>`;
    }
    else {
        titoloRegioneDiv.innerHTML = `<h2 class="titolo" id="titolo-regione">Province della regione ${nomeRegione}</h2><a id="estendi" href="regioni/${nomeRegione.toLowerCase().replaceAll(" ", "-").replaceAll("'", "-")}.html">Estendi</a>`;
    }

    // Crea i punti elenco per ogni provincia
    let table = elencoProvince.innerHTML;
    if (nomeRegione == "Italia") {
        table = `<tr><th class="index"></th><th class="hel nome pointer select-none" onclick="ordinaPerNome(flagAlfabetico)">Provincia <i class="fa-solid fa-sort"></i></th><th class="hel sigla select-none">Sigla</th><th class="hel regione pointer select-none" onclick="ordinaPerRegione(flagRegione)">Regione <i class="fa-solid fa-sort"></i></th><th class="hel abitanti pointer select-none" onclick="ordinaPerAbitanti(flagAbitanti)">Popolazione <i class="fa-solid fa-sort"></i></th></tr>`;
    }
    else {
        table = `<tr><th class="index"></th><th class="hel nome pointer select-none" onclick="ordinaPerNome(flagAlfabetico)">Provincia <i class="fa-solid fa-sort"></i></th><th class="hel sigla select-none">Sigla</th><th class="hel abitanti pointer select-none" onclick="ordinaPerAbitanti(flagAbitanti)">Popolazione <i class="fa-solid fa-sort"></i></th></tr>`;
    }
    let popolazioneTotale = 0;
    let index = 1; // indice
    for (let provincia of provinceTrovate) {
        // distinzione città metropolitane, lbc e province autonome
        let apex = '';
        if (provincia.metropolitana) {
            apex = '<sup class="pointer" title="Città metropolitana"><a class="sup" href="#legenda">[1]</a></sup>';
        }
        if (provincia.lbc) {
            apex = '<sup class="pointer" title="Libero consorzio comunale"><a class="sup" href="#legenda">[2]</a></sup>';
        }
        if (provincia.autonoma) {
            apex = '<sup class="pointer" title="Provincia autonoma"><a class="sup" href="#legenda">[3]</a></sup>';
        }
        if (provincia.eddr) {
            apex = '<sup class="pointer" title="Ente di decentramento regionale"><a class="sup" href="#legenda">[4]</a></sup>';
        }
        if (provincia.vda) {
            apex = '<sup class="pointer" title="Regione autonoma della Valle d\'Aosta (premi per vedere i dettagli)"><a class="sup" href="#legenda">[5]</a></sup>';
        }
        // creazione tabella
        if (provincia.capoluogo) {
            if (nomeRegione == "Italia") {
                table += `<tr><td class="el index"><strong>${index}</strong></td><td class="el nome"><strong>${provincia.nome} ${apex}</strong></td><td class="el sigla"><strong>${provincia.sigla}</strong><td class="el regione"><strong>${provincia.regione}</strong></td></td><td class="el abitanti"><strong>${provincia.abitanti.toLocaleString('it-IT', { useGrouping: 'always' })}</strong></td></tr>`;
            }
            else {
                table += `<tr><td class="el index"><strong>${index}</strong></td><td class="el nome"><strong>${provincia.nome} ${apex}</strong></td><td class="el sigla"><strong>${provincia.sigla}</strong></td><td class="el abitanti"><strong>${provincia.abitanti.toLocaleString('it-IT', { useGrouping: 'always' })}</strong></td></tr>`;
            }
        }
        else {
            if (nomeRegione == "Italia") {
                table += `<tr><td class="el index">${index}</td><td class="el nome">${provincia.nome} ${apex}</td><td class="el sigla">${provincia.sigla}</td><td class="el regione">${provincia.regione}</td><td class="el abitanti">${provincia.abitanti.toLocaleString('it-IT', { useGrouping: 'always' })}</td></tr>`;
            }
            else {
                table += `<tr><td class="el index">${index}</td><td class="el nome">${provincia.nome} ${apex}</td><td class="el sigla">${provincia.sigla}</td><td class="el abitanti">${provincia.abitanti.toLocaleString('it-IT', { useGrouping: 'always' })}</td></tr>`;
            }
        }
        // aggiornamento popolazione totale della regione e l'indice
        popolazioneTotale += provincia.abitanti;
        index++;
    }
    if (nomeRegione == "Italia") {
        table += `<tr><td class="index"></td><td class="fel nome"><strong>Popolazione totale</strong></td><td class="fel sigla"><strong></strong></td><td class="fel regione"><strong></strong></td><td class="fel abitanti"><strong>${popolazioneTotale.toLocaleString('it-IT')}</strong></td></tr>`
    }
    else {
        table += `<tr><td class="index"></td><td class="fel nome"><strong>Popolazione totale</strong></td><td class="fel sigla"><strong></strong></td><td class="fel abitanti"><strong>${popolazioneTotale.toLocaleString('it-IT')}</strong></td></tr>`
    }
    elencoProvince.innerHTML = table

    // Numero elementi trovati
    elementiTrovati.textContent = `${index - 1} province`;

    // Legenda
    let legenda = legendaProvince.innerHTML;
    legenda += `<h3 class="title-legend">Legenda</h3><ol><li>Città metropolitana</li><li>Libero consorzio comunale</li><li>Provincia autonoma</li><li>Ente di decentramento regionale</li>`;
    if (nomeRegione === "Valle d'Aosta" || nomeRegione === "Italia") {
        legenda += `<li><strong>La regione autonoma della Valle d'Aosta esercita anche le funzioni provinciali e, nelle elaborazioni statistiche, è considerata una provincia. Aosta è sede provinciale oltre che capoluogo di regione.</strong></li>`;
    }
    legenda += `</ol>`;
    legendaProvince.innerHTML = legenda;
}

let regioneCorrente = "";
let provinceCorrenti = [];
let flagAlfabetico = true;
let flagAbitanti = false;

fetch('data/province.json')
    .then(res => res.json())
    .then(data => {
        provinceItalia = data;

        const regioni = document.querySelectorAll('path');
        regioni.forEach(regione => {
            regione.addEventListener('click', () => {
                const nomeRegione = regione.getAttribute('name');
                regioneCorrente = nomeRegione;
                const provinceTrovate = provinceItalia[nomeRegione];
                provinceCorrenti = provinceTrovate;
                scritturaProvince(regioneCorrente, provinceCorrenti);
                flagAlfabetico = true;
                flagAbitanti = false;
                flagRegione = false;
            });
        });
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
        if (a.nome < b.nome)
            return -1;
        if (a.nome > b.nome)
            return 1;
        return 0;
    });
    regioneCorrente = italia;
    provinceCorrenti = elencoTotale;
    scritturaProvince(italia, elencoTotale);
    flagAlfabetico = true;
    flagAbitanti = false;
    flagRegione = false;
}