const btnGerar = document.getElementById('btnGerar')
const wait = document.getElementById('wait')
const p = document.querySelector('.animation-p')

btnGerar.addEventListener('click', function() {
    wait.style.display = 'block'
    i = 0
    const originalText = p.innerText
    setInterval(function() {
        if (i === 3) {
            i = 0
            p.innerText = originalText
        }
        p.innerHTML += '.'
        i++
    }, 800)
})