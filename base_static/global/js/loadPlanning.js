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
    }, 800)
});