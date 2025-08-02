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

let opcioMenu = prompt("elije una opcion del menu: ").tolowerCase();

const menu1 = "iniciar";
const menu2 = "guardar";
const menu3 = "salir";

switch (opcionMenu) {

    case "iniciar":
        console.log ("iniciando...");
        break;
    case "guardar":
        console.log ("guardando...");
}



