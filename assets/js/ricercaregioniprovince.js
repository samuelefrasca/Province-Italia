// Barra di ricerca comuni
const barraRicerca = document.getElementById('barra-ricerca');

barraRicerca.addEventListener('input', function () {
    const filtro = barraRicerca.value.trim().toLowerCase();
    if (filtro === '') {
        // Nessun filtro: mostra tutti i comuni
        scritturaComuni(provinciaCorrente, comuniProvincia, nomeRegione);
    } else {
        // Filtra i comuni il cui nome contiene il testo cercato
        const comuniFiltrati = comuniProvincia.filter(comune =>
            comune.comune.toLowerCase().includes(filtro)
        );
        scritturaComuni(provinciaCorrente, comuniFiltrati, nomeRegione);
    }
});