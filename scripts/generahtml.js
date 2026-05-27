// Questo file serve a creare tutti e 20 i file html delle regioni

const fs = require('fs');

const regioni = [
    { file: "abruzzo", nome: "Abruzzo" },
    { file: "basilicata", nome: "Basilicata" },
    { file: "calabria", nome: "Calabria" },
    { file: "campania", nome: "Campania" },
    { file: "emilia-romagna", nome: "Emilia-Romagna" },
    { file: "friuli-venezia-giulia", nome: "Friuli-Venezia Giulia" },
    { file: "lazio", nome: "Lazio" },
    { file: "liguria", nome: "Liguria" },
    { file: "lombardia", nome: "Lombardia" },
    { file: "marche", nome: "Marche" },
    { file: "molise", nome: "Molise" },
    { file: "piemonte", nome: "Piemonte" },
    { file: "puglia", nome: "Puglia" },
    { file: "sardegna", nome: "Sardegna" },
    { file: "sicilia", nome: "Sicilia" },
    { file: "toscana", nome: "Toscana" },
    { file: "trentino-alto-adige", nome: "Trentino-Alto Adige" },
    { file: "umbria", nome: "Umbria" },
    { file: "valle-d-aosta", nome: "Valle d'Aosta" },
    { file: "veneto", nome: "Veneto" }
];

// Legge il template dalla stessa cartella (scripts)
const template = fs.readFileSync('template.html', 'utf8');

// Crea la cartella 'regioni' un livello sopra (nella root)
const dirPath = '../regioni';
if (!fs.existsSync(dirPath)){
    fs.mkdirSync(dirPath);
}

regioni.forEach(r => {
    let output = template
        .replace(/NOME_REGIONE/g, r.nome)
        .replace(/FILENAME/g, r.file);

    // Scrive il file un livello sopra
    fs.writeFileSync(`${dirPath}/${r.file}.html`, output);
    console.log(`Generato: ${dirPath}/${r.file}.html`);
});