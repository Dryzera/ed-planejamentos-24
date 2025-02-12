(() => {
    const fields = document.querySelectorAll('.form-area')
    let maxCaracteres = 700;
    
    fields.forEach((value) => {
        const counter = value.querySelector('.count-caracteres')
        const input = value.querySelector('.textarea-create-planning')

        input.addEventListener('input', () => {
            let caracteresInputed = input.value.length
            
            if (caracteresInputed >= maxCaracteres) counter.style.color = 'red'
            else counter.style.color = 'black'

            counter.innerText = `${caracteresInputed}/700 caracteres`
        })
    })

})()