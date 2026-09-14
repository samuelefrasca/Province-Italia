let start = document.getElementById("start");
let game = document.getElementById("game");

let numeroDomande;
let provinceDisponibili
let domandaCorrente = 0;
let risposteCorrette = 0;

const regioniProvince = {
    "Piemonte": ["Alessandria", "Asti", "Biella", "Cuneo", "Novara", "Torino", "Verbano-Cusio-Ossola", "Vercelli"],
    "Lombardia": ["Bergamo", "Brescia", "Como", "Cremona", "Lecco", "Lodi", "Mantova", "Milano", "Monza e Brianza", "Pavia", "Sondrio", "Varese"],
    "Veneto": ["Belluno", "Padova", "Rovigo", "Treviso", "Venezia", "Verona", "Vicenza"],
    "Friuli-Venezia Giulia": ["Gorizia", "Pordenone", "Trieste", "Udine"],
    "Liguria": ["Genova", "Imperia", "La Spezia", "Savona"],
    "Emilia-Romagna": ["Bologna", "Ferrara", "Forlì-Cesena", "Modena", "Parma", "Piacenza", "Ravenna", "Reggio Emilia", "Rimini"],
    "Toscana": ["Arezzo", "Firenze", "Grosseto", "Livorno", "Lucca", "Massa-Carrara", "Pisa", "Pistoia", "Prato", "Siena"],
    "Marche": ["Ancona", "Ascoli Piceno", "Fermo", "Macerata", "Pesaro e Urbino"],
    "Lazio": ["Frosinone", "Latina", "Rieti", "Roma", "Viterbo"],
    "Abruzzo": ["Chieti", "L'Aquila", "Pescara", "Teramo"],
    "Campania": ["Avellino", "Benevento", "Caserta", "Napoli", "Salerno"],
    "Puglia": ["Bari", "Barletta-Andria-Trani", "Brindisi", "Foggia", "Lecce", "Taranto"],
    "Calabria": ["Catanzaro", "Cosenza", "Crotone", "Reggio Calabria", "Vibo Valentia"],
    "Sardegna": ["Cagliari", "Gallura Nord-Est Sardegna", "Medio Campidano", "Nuoro", "Ogliastra", "Oristano", "Sassari", "Sulcis Iglesiente"],
    "Sicilia": ["Agrigento", "Caltanissetta", "Catania", "Enna", "Messina", "Palermo", "Ragusa", "Siracusa", "Trapani"]
}

const regioni = Object.keys(regioniProvince);

const elencoProvince = [
    "Agrigento", "Alessandria", "Ancona", "Aosta", "Arezzo", "Ascoli Piceno",
    "Asti", "Avellino", "Bari", "Barletta-Andria-Trani", "Belluno", "Benevento",
    "Bergamo", "Biella", "Bologna", "Bolzano", "Brescia", "Brindisi",
    "Cagliari", "Caltanissetta", "Campobasso", "Carbonia-Iglesias", "Caserta",
    "Catania", "Catanzaro", "Chieti", "Como", "Cosenza", "Cremona", "Crotone",
    "Cuneo", "Enna", "Fermo", "Ferrara", "Firenze", "Foggia", "Forlì-Cesena",
    "Frosinone", "Genova", "Gorizia", "Grosseto", "Imperia", "Isernia",
    "L'Aquila", "La Spezia", "Latina", "Lecce", "Lecco", "Livorno", "Lodi",
    "Lucca", "Macerata", "Mantova", "Massa-Carrara", "Matera", "Medio Campidano",
    "Messina", "Milano", "Modena", "Monza e Brianza", "Napoli", "Novara",
    "Nuoro", "Ogliastra", "Olbia-Tempio", "Oristano", "Padova", "Palermo",
    "Parma", "Pavia", "Perugia", "Pesaro e Urbino", "Pescara", "Piacenza",
    "Pisa", "Pistoia", "Pordenone", "Potenza", "Prato", "Ragusa", "Ravenna",
    "Reggio Calabria", "Reggio Emilia", "Rieti", "Rimini", "Roma", "Rovigo",
    "Salerno", "Sassari", "Savona", "Siena", "Siracusa", "Sondrio", "Taranto",
    "Teramo", "Terni", "Torino", "Trapani", "Trento", "Treviso", "Trieste",
    "Udine", "Varese", "Venezia", "Verbano-Cusio-Ossola", "Vercelli", "Verona",
    "Vibo Valentia", "Vicenza", "Viterbo"
];

document.getElementById("startbutton").addEventListener("click", () => {

    // sull'input è prestabilito che i numeri siano interi (step=1 di default), tuttavia si possono inserire anche numeri non interi,
    // quindi utilizziamo Math.floor per sistemare:
    numeroDomande = Math.floor(Number(numeroQuiz.value));

    // nonostante ci sia un min e un max prestabilito sull'input, si può mettere qualsiasi valore,
    // quindi nella seguente condizione questo caso viene sistemato:
    if (numeroDomande < 1) { numeroDomande = 1 }
    if (numeroDomande > 15) { numeroDomande = 15 }

    domandaCorrente = 0;
    risposteCorrette = 0;
    startQuiz();
});

function random(num) {
    return Math.floor(Math.random() * num) + 1
}

function randomRemove(list) {
    return list.splice(random(list.length) - 1, 1)[0];
}

function generaRisposte(provinceCorrenti) {
    let copiaProvinceCorrenti = [...provinceCorrenti];
    let copiaElencoProvince = [...elencoProvince]
    let opzioni = [];
    let indexProvinciaErrata = random(4) - 1;
    for (let i = 0; i < 4; i++) {
        if (i == indexProvinciaErrata) {
            let intruso = randomRemove(copiaElencoProvince);
            while (copiaProvinceCorrenti.includes(intruso)) {
                intruso = randomRemove(copiaElencoProvince);
            }
            opzioni.push(intruso);
        }
        else {
            let opzione = randomRemove(copiaProvinceCorrenti);
            opzioni.push(opzione);
        }
    }
    let risposte = "";
    for (let i = 0; i < opzioni.length; i++) {
        let opzione = `<li class="opzione" onclick="verificaRisposta(${indexProvinciaErrata}, ${i})">${i + 1} - ${opzioni[i]}</li>`
        risposte += opzione
    }
    return risposte
}

function verificaRisposta(indexProvinciaErrata, indexOpzione) {
    let risposte = document.querySelectorAll("#game li");

    risposte.forEach((risposta, i) => {
        if (i == indexProvinciaErrata) {
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
    if (indexOpzione == indexProvinciaErrata) {
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
    let regioneCorrente = randomRemove(regioniDisponibili);
    let provinceCorrenti = regioniProvince[regioneCorrente];
    let question = "";
    question += `<p class="conteggiodomande">Domanda ${domandaCorrente}/${numeroDomande} - Risposte corrette ${risposteCorrette}/${domandaCorrente - 1}</p>`
    question += `<h2 class="domanda">Regione ${regioneCorrente}: qual è l'intruso?</h2>`;
    question += `<ul>${generaRisposte(provinceCorrenti)}</ul>`;
    game.innerHTML = question;
}

function startQuiz() {
    start.innerHTML = "";
    regioniDisponibili = [...regioni]
    quiz();
}