const form = document.querySelector('.register-form')

sendCode()
async function sendCode() {
    const email = document.getElementById("email").value;
    document.querySelector(".modal-page").style.display = "flex";
    const resendButton = document.querySelector('#resendCode')

    try {
        const response = await fetch("/send-mail/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(), 
            },
            body: JSON.stringify({ email: email })
        });

        if (!response.ok) {
            message('Erro ao enviar o código', 'error')
            throw new Error("Erro ao enviar código")
        };

        message(`Código enviado com sucesso para: ${email}`, 'success')
        
        let allowed = false

        setTimeout(() => {
            allowed = true
        }, 60000)

        resendButton.addEventListener('click', () => {
          if(allowed) {
            sendCode()
          } else {
            message('Aguarde alguns instantes para enviar o código novamente.', 'error')
          }
        })

    } catch (error) {
        console.error("Erro:", error);
        message('Erro ao processar o pedido', 'error')
    }

    document.querySelector("#verifyCode").addEventListener("click", async function() {
        const email = document.getElementById("email").value;
        const code = document.querySelector(".code").value;
        if(code.length < 6) return message('O código deve ter 6 caracteres', 'error')

        try {
            const response = await fetch("/check-code/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: JSON.stringify({ email: email, code: code })
            });
    
            const data = await response.json();
            
            if (data.valid) {
                document.querySelector(".modal-page").style.display = "none";

                form.submit()
            } else {
                message('Código inválido. Tente Novamente.', 'error')
            }
    
        } catch (error) {
            console.error("Erro:", error);
        }
    });
}


function getCSRFToken() {
    const cookie = document.cookie.split("; ").find(row => row.startsWith("csrftoken="));
    return cookie ? cookie.split("=")[1] : "";
}