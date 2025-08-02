//ejercicio 1

const diasSemana = 7;

switch (diasSemana) {
    case 1:
        console.log ("Lunes");
        break;

    case 2:
        console.log ("martes");
        break;

    case 3:
        console.log ("miercoles");
        break;

    case 4:
        console.log ("jueves");
        break;

    case 5:
        console.log ("viernes");
        break;

    case 6:
        console.log ("sabado")
        break;

    case 7:
        console.log ("domingo");
        break;
    default:
        console.log ("ese numero no es valido");
        break;
}

// ejercicio 2

console.log ("iniciar");
console.log ("guardar");
console.log ("salir");

let opcionMenu = prompt("elije una opcion del menu: ").toLowerCase();
switch (opcionMenu) {

    case "iniciar":
        console.log ("iniciando...");
        break;
    case "guardar":
        console.log ("guardando...");
        break;
    case "salir":
        console.log ("saliendo...");
        break;
    default:
        console.log ("esa opcion no esta disponiblre");
        break;
}



