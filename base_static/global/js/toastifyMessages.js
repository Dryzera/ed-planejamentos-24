import Toastify from 'toastify-js'
import "toastify-js/src/toastify.css"

function message(message, type='info', time=4000) {
    const backgroundColors = {
        success: 'linear-gradient(to right, #4caf50,rgb(106, 164, 109))',
        error: 'linear-gradient(to right,rgb(255, 43, 43),rgb(255, 65, 65))',
        info: 'linear-gradient(to right, #2196f3, #64b5f6)',
        warning: 'linear-gradient(to right,rgb(239, 193, 87),rgb(228, 173, 9))',
    }
    
    Toastify({
        text: message,
        duration: time,
        gravity: 'top',
        position: 'left',
        stopOnFocus: true,
        stopOnFocus: true,
        style: {
            background: backgroundColors[type]
        }
    }).showToast();
}

window.message = message;
export default message;