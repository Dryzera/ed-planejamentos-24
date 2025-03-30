(function() {
    const larguraTela = window.innerWidth;
    if (larguraTela <= 500) {
        const elementDisplay = document.querySelector('.alert-mobile').style.display = 'block'
    }

    const span = document.querySelector('.cumprimento')

    const atualDate = new Date().getHours()
    if (atualDate >= 6 && atualDate < 12) span.innerHTML = 'Bom dia'
    else if (atualDate >= 12 && atualDate < 18) span.innerHTML = 'Boa tarde'
    else if (atualDate >= 18 && atualDate < 24 || atualDate < 6) span.innerHTML = 'Boa noite'
    else span.innerHTML = 'Olá'
})()
