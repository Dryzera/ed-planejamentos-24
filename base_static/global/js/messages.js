(() => {
    function closeMessage() {
        const closeMessageBtn = document.querySelector('.closeMessage')
        const message = document.querySelector('.message')
        
        closeMessageBtn.addEventListener('click', () => {
            message.style.filter = 'blur(1rem)'

            setTimeout(() => message.style.display = 'none', 120)
        })
    }
closeMessage()
})()