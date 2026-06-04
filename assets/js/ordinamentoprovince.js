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

function ordinaPerRegioneCrescente(provinceCorrenti) {
    let copiaProvince = [...provinceCorrenti];
    copiaProvince.sort((a, b) => {
        return a.regione.localeCompare(b.regione);
    })
    scritturaProvince(regioneCorrente, copiaProvince);
}

function ordinaPerRegioneDecrescente(provinceCorrenti) {
    let copiaProvince = [...provinceCorrenti];
    copiaProvince.sort((a, b) => {
        return b.regione.localeCompare(a.regione);
    })
    scritturaProvince(regioneCorrente, copiaProvince);
}

// Funzioni applicate ai button

function ordinaPerRegione(flag) {
    if (flag) {
        ordinaPerRegioneDecrescente(provinceCorrenti);
        flagAbitanti = false;
        flagAlfabetico = false;
        flagRegione = false;
    }
    if (!flag) {
        ordinaPerRegioneCrescente(provinceCorrenti);
        flagAbitanti = false;
        flagAlfabetico = false;
        flagRegione = true;
    }
}

function ordinaPerAbitanti(flag) {
    if (flag) {
        ordinaPerAbitantiDecrescente(provinceCorrenti);
        flagAbitanti = false;
        flagAlfabetico = false;
        flagRegione = false;
    }
    if (!flag) {
        ordinaPerAbitantiCrescente(provinceCorrenti);
        flagAbitanti = true;
        flagAlfabetico = false;
        flagRegione = false;
    }
}

function ordinaPerNome(flag) {
    // parte dal presupposto che l'oggetto di riferimento sia già ordinato in ordine alfabetico
    if (flag) {
        scritturaProvince(regioneCorrente, provinceCorrenti.toReversed());
        flagAlfabetico = false;
        flagAbitanti = false;
        flagRegione = false;
    }
    if (!flag) {
        scritturaProvince(regioneCorrente, provinceCorrenti);
        flagAlfabetico = true;
        flagAbitanti = false;
        flagRegione = false;
    }
}