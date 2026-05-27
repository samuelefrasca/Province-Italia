// Script creato da Gemini per ordinare in ordine alfabetico gli oggetti dei json delle varie province
// Mettere il file nello stesso percorso dei json da riordinare

const fs = require('fs');
const path = require('path');

// Imposta la cartella corrente
const cartella = './';

// Trova tutti i file nella cartella e filtra solo i JSON
const filePresenti = fs.readdirSync(cartella);
const fileJson = filePresenti.filter(file => file.endsWith('.json'));

for (const file of fileJson) {
    const percorsoFile = path.join(cartella, file);

    // Legge il contenuto del file
    const rawData = fs.readFileSync(percorsoFile, 'utf8');
    let dati = JSON.parse(rawData);

    // Ordina i dati per la voce comune
    dati.sort((a, b) => a.comune.localeCompare(b.comune));

    // Sovrascrive il file originale con i dati ordinati
    fs.writeFileSync(percorsoFile, JSON.stringify(dati, null, 2));

    console.log(`Fatto: ${file}`);
}