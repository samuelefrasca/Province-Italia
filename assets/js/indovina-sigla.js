let start = document.getElementById("start");
let game = document.getElementById("game");

let numeroDomande;
let provinceDisponibili
let domandaCorrente = 0;
let risposteCorrette = 0;

document.getElementById("startbutton").addEventListener("click", () => {

    // sull'input è prestabilito che i numeri siano interi (step=1 di default), tuttavia si possono inserire anche numeri non interi,
    // quindi utilizziamo Math.floor per sistemare:
    numeroDomande = Math.floor(Number(numeroQuiz.value));

    // nonostante ci sia un min e un max prestabilito sull'input, si può mettere qualsiasi valore,
    // quindi nella seguente condizione questo caso viene sistemato:
    if (numeroDomande < 1) { numeroDomande = 1 }
    if (numeroDomande > 110) { numeroDomande = 110 }

    domandaCorrente = 0;
    risposteCorrette = 0;
    startQuiz();
});

const provinceSigle = {
    "Agrigento": "AG",
    "Alessandria": "AL",
    "Ancona": "AN",
    "Arezzo": "AR",
    "Ascoli Piceno": "AP",
    "Asti": "AT",
    "Avellino": "AV",
    "Bari": "BA",
    "Barletta-Andria-Trani": "BT",
    "Belluno": "BL",
    "Benevento": "BN",
    "Bergamo": "BG",
    "Biella": "BI",
    "Bologna": "BO",
    "Bolzano": "BZ",
    "Brescia": "BS",
    "Brindisi": "BR",
    "Cagliari": "CA",
    "Caltanissetta": "CL",
    "Campobasso": "CB",
    "Caserta": "CE",
    "Catania": "CT",
    "Catanzaro": "CZ",
    "Chieti": "CH",
    "Como": "CO",
    "Cosenza": "CS",
    "Cremona": "CR",
    "Crotone": "KR",
    "Cuneo": "CN",
    "Enna": "EN",
    "Fermo": "FM",
    "Ferrara": "FE",
    "Firenze": "FI",
    "Foggia": "FG",
    "Forlì-Cesena": "FC",
    "Frosinone": "FR",
    "Gallura Nord-Est Sardegna": "OT",
    "Genova": "GE",
    "Gorizia": "GO",
    "Grosseto": "GR",
    "Imperia": "IM",
    "Isernia": "IS",
    "L'Aquila": "AQ",
    "La Spezia": "SP",
    "Latina": "LT",
    "Lecce": "LE",
    "Lecco": "LC",
    "Livorno": "LI",
    "Lodi": "LO",
    "Lucca": "LU",
    "Macerata": "MC",
    "Mantova": "MN",
    "Massa-Carrara": "MS",
    "Matera": "MT",
    "Medio Campidano": "VS",
    "Messina": "ME",
    "Milano": "MI",
    "Modena": "MO",
    "Monza e Brianza": "MB",
    "Napoli": "NA",
    "Novara": "NO",
    "Nuoro": "NU",
    "Ogliastra": "OG",
    "Oristano": "OR",
    "Padova": "PD",
    "Palermo": "PA",
    "Parma": "PR",
    "Pavia": "PV",
    "Perugia": "PG",
    "Pesaro e Urbino": "PU",
    "Pescara": "PE",
    "Piacenza": "PC",
    "Pisa": "PI",
    "Pistoia": "PT",
    "Pordenone": "PN",
    "Potenza": "PZ",
    "Prato": "PO",
    "Ragusa": "RG",
    "Ravenna": "RA",
    "Reggio Calabria": "RC",
    "Reggio Emilia": "RE",
    "Rieti": "RI",
    "Rimini": "RN",
    "Roma": "RM",
    "Rovigo": "RO",
    "Salerno": "SA",
    "Sassari": "SS",
    "Savona": "SV",
    "Siena": "SI",
    "Siracusa": "SR",
    "Sondrio": "SO",
    "Sulcis Iglesiente": "SU",
    "Taranto": "TA",
    "Teramo": "TE",
    "Terni": "TR",
    "Torino": "TO",
    "Trapani": "TP",
    "Trento": "TN",
    "Treviso": "TV",
    "Trieste": "TS",
    "Udine": "UD",
    "Valle d'Aosta": "AO",
    "Varese": "VA",
    "Venezia": "VE",
    "Verbano-Cusio-Ossola": "VB",
    "Vercelli": "VC",
    "Verona": "VR",
    "Vibo Valentia": "VV",
    "Vicenza": "VI",
    "Viterbo": "VT"
};

const province = Object.keys(provinceSigle);

function random(num) {
    return Math.floor(Math.random() * num) + 1;
}

function randomRemove(list) {
    return list.splice(random(list.length) - 1, 1)[0];
}

function generaRisposte(provinciaCorrente) {
    let opzioni = [];
    let indexProvinciaCorrente = random(4) - 1;
    for (let i = 0; i < 4; i++) {
        if (indexProvinciaCorrente == i) {
            opzioni.push(provinciaCorrente);
        }
        else {
            let provinciaRandom = randomRemove(provinceDisponibili);
            while (provinciaRandom == provinciaCorrente) {
                provinciaRandom = randomRemove(provinceDisponibili);
            }
            opzioni.push(provinciaRandom);
        }
    }
    let risposte = "";
    for (let i = 0; i < opzioni.length; i++) {
        let opzione = `<li class="opzione" onclick="verificaRisposta(${indexProvinciaCorrente}, ${i})">${i + 1} - ${opzioni[i]}</li>`
        risposte += opzione
    }
    return risposte
}

function verificaRisposta(indexProvinciaCorrente, indexOpzione) {
    let risposte = document.querySelectorAll("#game li");

    risposte.forEach((risposta, i) => {
        if (i == indexProvinciaCorrente) {
            risposta.style.backgroundColor = "green";
        }
        else {
            risposta.style.backgroundColor = "red";
        }
        risposta.style.color = "white";
    });

    // la seguente funzione forEach evita che si possano premere nuovamente le opzioni dopo aver dato la risposta
    risposte.forEach((risposta) => {
        risposta.style.pointerEvents = "none";
    });

    // se la risposta è corretta:
    if (indexOpzione == indexProvinciaCorrente) {
        game.innerHTML += `<p class="esito" style="color: green;">Risposta corretta!</p>`
        risposteCorrette++;
    }
    // se la risposta è errata
    else {
        game.innerHTML += `<p class="esito" style="color: red;">Risposta sbagliata!</p>`
    }

    game.innerHTML += `<button class="continuabutton" onclick="quiz()">Continua</button>`;
}

function quiz() {
    domandaCorrente++;
    if (domandaCorrente > numeroDomande) {
        // quiz finito
        game.innerHTML = `<h2 class="giocofinito">Gioco finito</h2><p class="esitofinale">Hai risposto correttamente a ${risposteCorrette} domande su ${numeroDomande}</p>`
        game.innerHTML += `<button class="startelement startbutton" onclick="window.location.href='javascript:location.reload()'">Rigioca</button>`
        return;
    }
    let provinciaCorrente = randomRemove(provinceDisponibili);
    let siglaCorrente = provinceSigle[provinciaCorrente];
    let question = "";
    question += `<p class="conteggiodomande">Domanda ${domandaCorrente}/${numeroDomande} - Risposte corrette ${risposteCorrette}/${domandaCorrente - 1}</p>`
    question += `<h2 class="domanda">Che provincia è la sigla ${siglaCorrente}?</h2>`;
    question += `<ul>${generaRisposte(provinciaCorrente)}</ul>`;
    game.innerHTML = question;
}

function startQuiz() {
    start.innerHTML = "";
    provinceDisponibili = [...province];
    quiz();
}