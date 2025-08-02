// ejercicio 1

let edad = Number(prompt("ingresa tu edad"));

if (edad >= 18) {
    console.log ("es mayor de edad");
}else {
    console.log ("es menor de edad");
}

// ejercicio 2

let numero1 = Number(prompt("dime un numero"));
let numero2 = Number(prompt("dime otro numero"));

if (numero1 == numero2) {
    console.log (`el ${numero1} es igual que ${numero2}`);
} else if (numero1 > numero2) {
    console.log (`el ${numero1} es mayor que ${numero2}`);
}

else {
    console.log (`el ${numero1} es menor que ${numero2}`);
}

// ejercicio 3

let color = prompt("que color es?")

if (color == "verde") {
    console.log("puedes cruzar");
}else if (color == "rojo") {
    console.log ("no cruce");
} else if (color == "amarillo") {
    console.log ("precaucion");
} else {
    console.log ("ese color no es valido")
}

// ejercicio 4

let edadusuario = Number(prompt("ingresa tu edad"));
let ticket = true;

if (edadusuario >=18 && ticket == true) {
    console.log ("acceso concedido")
}
else {
    console.log ("acceso denegado")
}

// ejercicio 5

let montoCompra = Number(prompt("ingresa el monto"));

if (montoCompra > 100) {
    montototal = montoCompra *0.80;
    console.log(`${montototal}`);
}
else if (montoCompra >= 50) {
    montototal = montoCompra *0.90;
    console.log(`${montototal}`);
}
else {
    console.log("sin descuento");
}

