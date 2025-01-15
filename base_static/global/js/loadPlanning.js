const btnGerar = document.getElementById('btnGerar')
const wait = document.getElementById('wait')
const p = document.querySelector('.animation-p')

btnGerar.addEventListener('click', function() {
    wait.style.display = 'block'
    setInterval(function() {
        p.innerHTML += '.'
    }, 1800)
})