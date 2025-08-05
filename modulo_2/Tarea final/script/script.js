const pantallita = document.querySelector(".pantallita");
const botones = document.querySelectorAll(".boton");


botones.forEach(button => {
    button.addEventListener("click", () => {
        const botonp = button.textContent;

        //multiplicacion////
        if (button.id === "multiplicacion") {
            pantallita.textContent += "*";
            return;
        }

        //division////
        if (button.id === "division") {
            pantallita.textContent += "/"
            return;
        }

        //potencia/////
        if (button.id === "potencia") {
            
            pantallita.textContent += "**";
            return;
        }

        //coseno
        if (button.id === "cos") {
            pantallita.textContent = "cos("+Math.cos(eval(pantallita.textContent));
            return;
        }

        //tangente
        if (button.id === "tan") {
            pantallita.textContent = "tan("+Math.tan(eval(pantallita.textContent));
            return;
        }

        //raiz
        if (button.id === "raiz") {
            if (pantallita.textContent < 0) {
                pantallita.textContent = "Error";
               return;
            }
                pantallita.textContent = Math.sqrt(pantallita.textContent);
                return;
        }
        
        //borrrar
        if (button.id === "borrar") {
            pantallita.textContent = pantallita.textContent.slice(0, -1);
           if (pantallita.textContent.length === 0 || pantallita.textContent === "Error") {
               pantallita.textContent = "0";
            }
            return;
        }

        //Igualdad
        if (button.id === "igual") {
            
            try {
                pantallita.textContent = eval(pantallita.textContent);
            } catch {
                pantallita.textContent = "Error";
            }
            return;
            }

        //pantashita
        if (pantallita.textContent === "0" || pantallita.textContent === "Error") {
            pantallita.textContent = botonp;
        } else {
            pantallita.textContent += botonp;
        }

        //AC
        if (button.id === "ac") {
            pantallita.textContent = "0";
        }

    })
});



