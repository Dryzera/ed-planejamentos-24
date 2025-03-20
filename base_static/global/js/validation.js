function fieldsValidate(field) {
    if (!field) return false
    if (field.value.length < 3) {
        if(field.name === 'last_name') return
        return 'Todos os campos devem ser preenchidos.'
    }
    if (field.name === 'email') {
        const tempMailRegex = /@(tempmail\.email|10minutemail\.com|guerrillamail\.com|yopmail\.com|mailinator\.com|mohmal\.com|throwawaymail\.com|uorak\.com)$/i;
        if (tempMailRegex.test(field.value)) return 'Este domínio de e-mail não é aceito.'
    }
    return true
}

function registerValidation() {
    const errorsOnValidation = []
    form = document.querySelector('.register-form')

    form.addEventListener('submit', e => {
        e.preventDefault()
        
        inputs = form.querySelectorAll('.input-validate')
        inputs.forEach(element => {
            const validationResponses = fieldsValidate(element)
            errorsOnValidation.push(validationResponses)
        });
        form.submit()
    });

}

registerValidation()