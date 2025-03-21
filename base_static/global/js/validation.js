function fieldsValidate(field) {
    if (!field) return false
    if (field.value.length < 3) {
        if(field.name === 'last_name') return true
        return 'Todos os campos devem ter no mínimo 2 caracteres.'
    }
    if (field.name === 'email') {
        const tempMailRegex = /@(tempmail\.email|10minutemail\.com|guerrillamail\.com|yopmail\.com|mailinator\.com|mohmal\.com|throwawaymail\.com|uorak\.com)$/i;
        if (tempMailRegex.test(field.value)) return 'Este domínio de e-mail não é aceito. Tente outro.'
    }
    return true
}

function registerValidation() {
    form = document.querySelector('.register-form')
    
    form.addEventListener('submit', e => {
        e.preventDefault()
        const errorsOnValidation = []
        
        inputs = form.querySelectorAll('.input-validate')
        inputs.forEach(element => {
            const validationResponses = fieldsValidate(element)
            errorsOnValidation.push(validationResponses)
        });

        let checkExistsErrors = errorsOnValidation.filter(result => result !== true)
        if(checkExistsErrors.length !== 0) {
            let errorMessage = ''
            checkExistsErrors.forEach(err => errorMessage += err + '\n')
            alert(errorMessage)
            return
        }
        form.submit()
    });

}

registerValidation()