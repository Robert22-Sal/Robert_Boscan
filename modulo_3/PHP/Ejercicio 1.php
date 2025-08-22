<?php 

//Ejercicio 1 Contador de Pares e Impares
// 🔢 Escribe un script que cuente y muestre la cantidad de números pares e impares que hay en el rango del 1 al 50.


for ($i = 0; $i <=50; $i++){
    if ($i %2 == 0) {
        echo "" .$i. " es par\n";
    }
    else {
        echo "" .$i. "es impar\n";
    }
}

//Ejercicio 2 Crea un script que genere y muestre en la terminal la tabla de multiplicar completa del número 8, desde el 8×1 hasta el 8×10.

for ($n = 1; $n<=10; $n++){
    echo "8 x ". $n . " = " . (8 * $n) . "\n";   
}

//Ejercicio 3  Desarrolla un programa que simule un juego de "adivina el número". Define una variable con un número secreto y utiliza un bucle while para intentar adivinarlo, incrementando un contador hasta encontrarlo. Muestra cada intento.

$num = readline("Escribe un numero entre el 10 y el 15: ");
$intentos = 5;
$ad = 12;

 while ($num != $ad) {
    $intentos --;
    if ($num != $ad) {
        echo "Fallaste!! Te quedan " .$intentos. " intentos.\n";
        $num = readline("Escribe un numero entre el 10 y el 15: ");
    }
    if ($intentos == 0) {
        echo "Fallaste!! Te quedan " .$intentos. " intentos.\n";
        echo "Lo siento, ya perdiste todos los intentos :( \n";
        break;
    }
    else {
        echo "Acertaste!! el número es " .$ad. "\n";
    }
}
// ejercicio 4 Escribe un script que calcule la suma de todos los números impares desde el 1 hasta el 100.

echo "numeros impares del 1 al 100 \n";
for ($i = 1; $i<=100; $i++){
    if ($i % 2 != 0){
        echo "" .$i. "\n";
    }
}


//ejercicio 5 Crea un programa que verifique si una persona puede obtener una licencia de conducir. La condición es que debe tener al menos 18 años y no más de 65 años. Define una variable para la edad y muestra si cumple los requisitos o no.

$edad = readline("Introduce tu edad: ");

if ($edad >= 18 && $edad <=65){
    echo "puedes aprender a conducir\n";
}
else{
    echo "no puedes aprender a conducir \n";
}


//Ejercicio 6 Utilizando bucles anidados, crea un script que dibuje un cuadrado de 5×5 en la terminal utilizando el carácter #.

for ($i = "#"; $i<=5; $i++){
    echo "" .$i. "";
}

//ejercicio 7 Desarrolla un script que determine si un número almacenado en una variable es positivo, negativo o cero, y muestre el resultado correspondiente.
$numero = 12;

if ($numero < 0){
    echo "el numero es negativo";
}
elseif($numero > 0){
    echo "el numero es positivo";
}
else{
    echo "el numero es nulo";
}

//ejercicio 8 Escribe un programa que imprima los números del 1 al 30. Para los múltiplos de 3, debe imprimir "Mar"; para los múltiplos de 5, "Tierra"; y para los múltiplos de ambos, "MarTierra".

for($i=1; $i<=30; $i++){
    if($i % 3 == 0 && $i % 5 == 0){
        echo "" .$i. " = Mar/Tierra \n";
    }
    
    elseif($i % 3 == 0){
        echo "" .$i. " = Mar \n" ;
    }
    
    elseif($i % 5 == 0){
        echo "" .$i. " = Tierra\n";
    }
}

//ejercicio 9 Crea un script que, dada una variable numérica que representa la temperatura en grados Celsius, muestre un mensaje diferente según el valor:
   //❄️ "Fría" si es menor de 10°C  
   //🌤️ "Templada" si está entre 10°C y 25°C  
   //" si es mayor de 25°C
$temperatura = 12
if ($temperatura < 10){
    echo "❄️ Fría";
}
if ($temperatura >=10 && <= 25){
    echo "🌤️ Templada";
}
else{
    echo "🔥 Calurosa";
}

// Ejercicio 10 Escribe un programa que realice una cuenta regresiva desde el 10 hasta el 1. Al finalizar, debe mostrar el mensaje: "¡Feliz Año Nuevo! 🎉"

for($i = 10; $i <= 0; $i-=1) {
    echo "" .$i. "\n";
    if ($i == 0){
        echo "¡Feliz Año Nuevo! 🎉";
    }
}

?>