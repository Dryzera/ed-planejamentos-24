function fieldsValidate(field) {
    if (!field) return false
    if (field.value.length < 3) {
        if(field.name === 'last_name') return true
        return 'Todos os campos devem ter no mínimo 3 caracteres.'
    }
    if (field.name === 'email') {
        const tempMailRegex = /@(gmail\.com|outlook\.com|yahoo\.com|hotmail\.com|aol\.com|icloud\.com|protonmail\.com|zoho\.com|mail\.com|edu\.com|escola\.pr\.gov\.br|inbox\.com|fastmail\.com|oul\.com\.br)$/i;
        if (!tempMailRegex.test(field.value)) return 'Este domínio de e-mail não é aceito. Tente outro.'
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
            checkExistsErrors = checkExistsErrors.reduce((acc, next) => {
                if (!acc.includes(next)) acc.push(next)
                    return acc
            }, [])
            checkExistsErrors.forEach(err => message(err, 'error'))
            return
        }

        form.submit()
    });

}

registerValidation()