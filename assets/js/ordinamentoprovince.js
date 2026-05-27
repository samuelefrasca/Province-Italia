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
    // parte dal presupposto che l'oggetto di riferimento sia già ordinato in ordine alfabetico
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