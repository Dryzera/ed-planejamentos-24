function loadingOnPlanning() {
    return new Promise(resolve => {
        const btnGerar = document.getElementById('btnGerar')
        const wait = document.getElementById('wait')
        const p = document.querySelector('.animation-p')
        const modalContent = document.querySelector('.modal-content')

        btnGerar.addEventListener('click', function() {
            wait.style.display = 'block'
            modalContent.style.display = 'block'
            i = 0
            const originalText = p.innerHTML
            setInterval(function() {
                if (i === 3) {
                    i = 0
                    p.innerHTML = originalText
                }
                p.innerHTML += '.'
                i++
            }, 800);
        });
        resolve();
    })
}

function caracteresCount() {
    return new Promise(resolve => {
        const widthCols = window.innerWidth * 0.04;
        const fields = document.querySelectorAll('.form-area')
        let maxCaracteres = 700;

        const aditionalContent = document.getElementById('aditional_content');
        aditionalContent.setAttribute('cols', String(widthCols));
        
        fields.forEach((value) => {
            const counter = value.querySelector('.count-caracteres');
            const input = value.querySelector('.textarea-create-planning');
            
            input.setAttribute('cols', String(widthCols));

            input.addEventListener('input', () => {
                let caracteresInputed = input.value.length;
                
                if (caracteresInputed >= maxCaracteres) counter.style.color = 'red';
                else counter.style.color = 'black';

                counter.innerText = `${caracteresInputed}/700 caracteres`;
            });
        });
        resolve();
    });
};

async function executor() {
    await Promise.all([caracteresCount(), loadingOnPlanning()]);
}

executor()