(() => {
    const download = document.querySelector('.ver-docx')
    const pdf = document.querySelector('.ver-pdf')
    const divPdf = document.querySelector('.info-finish-planning-pdf')
    const divDownload = document.querySelector('.info-finish-planning')

    download.addEventListener('click', () => {
        divPdf.style.display = 'none'
        divDownload.style.display = 'block'
    })
    
    pdf.addEventListener('click', () => {
        divDownload.style.display = 'none'
        divPdf.style.display = 'block'
    })
})();