const form = document.querySelector('.register-form')
sendCode()
async function sendCode() {
    const email = document.getElementById("email").value;
    document.querySelector(".modal-page").style.display = "flex";

    try {
        const response = await fetch("/send-mail/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(), 
            },
            body: JSON.stringify({ email: email })
        });

        if (!response.ok) throw new Error("Erro ao enviar código");


    } catch (error) {
        console.error("Erro:", error);
        alert("Erro ao processar pedido");
    }

    document.querySelector(".verifyCode").addEventListener("click", async function() {
        const email = document.getElementById("email").value;
        const code = document.querySelector(".code").value;
    
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
                alert("Código inválido! Tente novamente.");
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