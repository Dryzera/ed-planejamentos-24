(() => {
    const clearBtn = document.querySelector('#clear')
    const input = document.querySelector('.input-terms-activities')

    clearBtn.addEventListener('click', () => {
        if (input.value) {
            window.location.replace('/professores/atividades/')
        } else return

    }) 
})()