function transcriptIaReponses(text) {
    const texto = text
    .replace(/^### (.*)$/gm, "<h5>$1</h5>") 
    .replace(/^## (.*)$/gm, "<h4>$1</h4>")  
    .replace(/^# (.*)$/gm, "<h3>$1</h3>")   
    // Aplica formatação de texto dentro das tags
    .replace(/\*\*(.*?)\*\*/g, "<b>$1</b>")  
    .replace(/\*(.*?)\*/g, "<i>$1</i>")      
    .replace(/~~(.*?)~~/g, "<s>$1</s>")      
    .replace(/__(.*?)__/g, "<u>$1</u>")      
    .replace(/`(.*?)`/g, "<code>$1</code>")  
    // Substitui listas corretamente (sem `<br>`)
    .replace(/^\* (.*)$/gm, "• $1")    
    // Envolve as listas em `<ul>`
    .replace(/(<li>.*<\/li>)/gs, "<ul>$1</ul>")
    // Substitui quebras de linha apenas quando necessário
    .replace(/(?<!<\/(ul|li|p)>)\n/g, "<br>");

    return `<p>${texto}</p>`
}

const form = document.querySelector('.form-ia')
function checkFields() {
    const loader = document.querySelector('.generateAnwser')

    return new Promise(resolve => {
        form.addEventListener('submit', e => {
            e.preventDefault()
            const prompt = document.querySelector('#input-prompt')

            let errors = []

            if(prompt.value.length <= 1) errors.push('Você precisa inserir mais alguns caracteres')

            if(errors.length !== 0) return
            loader.style.display = 'flex'
            form.submit();
            resolve()
        });
    })
};

function styleIaResponse() {
    const message = document.querySelector('.message')
    if(message) return
    
    const iaResponses = document.querySelectorAll('.ia-response')

    iaResponses.forEach(el => {
        const responseTranscripted = transcriptIaReponses(el.innerText)
        el.innerHTML = responseTranscripted
    })
}

function scrollBottom() {
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
}

function domLoaded() {
    return new Promise(resolve => {
        document.addEventListener('DOMContentLoaded', () => {
            styleIaResponse();
            scrollBottom();
        });
        resolve();
    });
};

async function runFunctions() {
    await Promise.all([domLoaded(), checkFields()]);
}

runFunctions()