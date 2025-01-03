// add loader 
const btnGerar = document.getElementById('btnGerar')
const wait = document.getElementById('wait')

btnGerar.addEventListener('click', function() {
    wait.innerText = 'Isso pode demorar, redirecionaremos você assim que concluido.'
})
