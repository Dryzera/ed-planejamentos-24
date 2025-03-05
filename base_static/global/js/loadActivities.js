const modal = document.getElementById('modal');
const overlay = document.getElementById('overlay');
const modalContent = document.getElementById('modalContent');
const openModal = document.querySelector('.openModal');
const closeModal = document.getElementById('closeModal');


function captureClick() {
    btnUse = document.querySelectorAll('.useActivityButton')
    inputActivity = document.querySelector('.activityInput')
    
    btnUse.forEach(element => {
        element.addEventListener('click', e => {
            let atribute = element.getAttribute('data-id')
            console.log(atribute)
            inputActivity.setAttribute('value', atribute)
        })
    });
}

openModal.addEventListener('click', async () => {
    modal.style.display = 'block';
    overlay.style.display = 'block';

    try {
        const response = await fetch('/load_activities/');
        const html = await response.text();
        modalContent.innerHTML = html;
        captureClick()
    } catch (error) {
        modalContent.innerHTML = "Erro ao carregar atividades.";
    }
});

closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
    overlay.style.display = 'none';
});

overlay.addEventListener('click', () => {
    modal.style.display = 'none';
    overlay.style.display = 'none';
});