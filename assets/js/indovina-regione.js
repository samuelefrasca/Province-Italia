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
    if (numeroDomande > 109) { numeroDomande = 109 }

    domandaCorrente = 0;
    risposteCorrette = 0;
    startQuiz();
});

const provinceRegioni = {
    "Alessandria": "Piemonte",
    "Asti": "Piemonte",
    "Biella": "Piemonte",
    "Cuneo": "Piemonte",
    "Novara": "Piemonte",
    "Torino": "Piemonte",
    "Verbano-Cusio-Ossola": "Piemonte",
    "Vercelli": "Piemonte",
    "Bergamo": "Lombardia",
    "Brescia": "Lombardia",
    "Como": "Lombardia",
    "Cremona": "Lombardia",
    "Lecco": "Lombardia",
    "Lodi": "Lombardia",
    "Mantova": "Lombardia",
    "Milano": "Lombardia",
    "Monza e Brianza": "Lombardia",
    "Pavia": "Lombardia",
    "Sondrio": "Lombardia",
    "Varese": "Lombardia",
    "Bolzano": "Trentino-Alto Adige",
    "Trento": "Trentino-Alto Adige",
    "Belluno": "Veneto",
    "Padova": "Veneto",
    "Rovigo": "Veneto",
    "Treviso": "Veneto",
    "Venezia": "Veneto",
    "Verona": "Veneto",
    "Vicenza": "Veneto",
    "Gorizia": "Friuli-Venezia Giulia",
    "Pordenone": "Friuli-Venezia Giulia",
    "Trieste": "Friuli-Venezia Giulia",
    "Udine": "Friuli-Venezia Giulia",
    "Genova": "Liguria",
    "Imperia": "Liguria",
    "La Spezia": "Liguria",
    "Savona": "Liguria",
    "Bologna": "Emilia-Romagna",
    "Ferrara": "Emilia-Romagna",
    "Forlì-Cesena": "Emilia-Romagna",
    "Modena": "Emilia-Romagna",
    "Parma": "Emilia-Romagna",
    "Piacenza": "Emilia-Romagna",
    "Ravenna": "Emilia-Romagna",
    "Reggio Emilia": "Emilia-Romagna",
    "Rimini": "Emilia-Romagna",
    "Arezzo": "Toscana",
    "Firenze": "Toscana",
    "Grosseto": "Toscana",
    "Livorno": "Toscana",
    "Lucca": "Toscana",
    "Massa-Carrara": "Toscana",
    "Pisa": "Toscana",
    "Pistoia": "Toscana",
    "Prato": "Toscana",
    "Siena": "Toscana",
    "Perugia": "Umbria",
    "Terni": "Umbria",
    "Ancona": "Marche",
    "Ascoli Piceno": "Marche",
    "Fermo": "Marche",
    "Macerata": "Marche",
    "Pesaro e Urbino": "Marche",
    "Frosinone": "Lazio",
    "Latina": "Lazio",
    "Rieti": "Lazio",
    "Roma": "Lazio",
    "Viterbo": "Lazio",
    "Chieti": "Abruzzo",
    "L'Aquila": "Abruzzo",
    "Pescara": "Abruzzo",
    "Teramo": "Abruzzo",
    "Campobasso": "Molise",
    "Isernia": "Molise",
    "Avellino": "Campania",
    "Benevento": "Campania",
    "Caserta": "Campania",
    "Napoli": "Campania",
    "Salerno": "Campania",
    "Matera": "Basilicata",
    "Potenza": "Basilicata",
    "Bari": "Puglia",
    "Barletta-Andria-Trani": "Puglia",
    "Brindisi": "Puglia",
    "Foggia": "Puglia",
    "Lecce": "Puglia",
    "Taranto": "Puglia",
    "Catanzaro": "Calabria",
    "Cosenza": "Calabria",
    "Crotone": "Calabria",
    "Reggio Calabria": "Calabria",
    "Vibo Valentia": "Calabria",
    "Cagliari": "Sardegna",
    "Gallura Nord-Est Sardegna": "Sardegna",
    "Medio Campidano": "Sardegna",
    "Nuoro": "Sardegna",
    "Ogliastra": "Sardegna",
    "Oristano": "Sardegna",
    "Sassari": "Sardegna",
    "Sulcis Iglesiente": "Sardegna",
    "Agrigento": "Sicilia",
    "Caltanissetta": "Sicilia",
    "Catania": "Sicilia",
    "Enna": "Sicilia",
    "Messina": "Sicilia",
    "Palermo": "Sicilia",
    "Ragusa": "Sicilia",
    "Siracusa": "Sicilia",
    "Trapani": "Sicilia"
}

const provinceKeys = Object.keys(provinceRegioni)

const regioni = [
    "Piemonte",
    "Lombardia",
    "Trentino-Alto Adige",
    "Veneto",
    "Friuli-Venezia Giulia",
    "Liguria",
    "Emilia-Romagna",
    "Toscana",
    "Umbria",
    "Marche",
    "Lazio",
    "Abruzzo",
    "Molise",
    "Campania",
    "Basilicata",
    "Puglia",
    "Calabria",
    "Sardegna",
    "Sicilia"
]

function random(num) {
    return Math.floor(Math.random() * num) + 1
}

function randomRemove(list) {
    return list.splice(random(list.length) - 1, 1)[0];
}

function generaRisposte(regioneCorrente) {
    let copiaRegioni = [...regioni];
    copiaRegioni.splice(copiaRegioni.indexOf(regioneCorrente), 1);
    let opzioni = [];
    let indexRegioneCorrente = random(4) - 1;
    for (let i = 0; i < 4; i++) {
        if (indexRegioneCorrente == i) {
            opzioni.push(regioneCorrente);
        }
        else {
            let regioneRandom = randomRemove(copiaRegioni);
            while (regioneRandom == regioneCorrente) {
                regioneRandom = randomRemove(copiaRegioni);
            }
            opzioni.push(regioneRandom)
        }
    }
    let risposte = "";
    for (let i = 0; i < opzioni.length; i++) {
        let opzione = `<li class="opzione" onclick="verificaRisposta(${indexRegioneCorrente}, ${i})">${i + 1} - ${opzioni[i]}</li>`
        risposte += opzione
    }
    return risposte
}

function verificaRisposta(indexRegioneCorrente, indexOpzione) {
    let risposte = document.querySelectorAll("#game li");

    risposte.forEach((risposta, i) => {
        if (i == indexRegioneCorrente) {
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
    if (indexOpzione == indexRegioneCorrente) {
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
    let regioneCorrente = provinceRegioni[provinciaCorrente];
    let question = "";
    question += `<p class="conteggiodomande">Domanda ${domandaCorrente}/${numeroDomande} - Risposte corrette ${risposteCorrette}/${domandaCorrente - 1}</p>`
    question += `<h2 class="domanda">In che regione si trova la provincia ${provinciaCorrente}?</h2>`;
    question += `<ul>${generaRisposte(regioneCorrente)}</ul>`;
    game.innerHTML = question;
}

function startQuiz() {
    start.innerHTML = "";
    provinceDisponibili = [...provinceKeys];
    quiz();
}