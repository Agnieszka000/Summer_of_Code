/* Spróbuj napisać kod, który w konsoli wyświetli liczby od 1 do 20, ale za każdym razem, gdy liczba jest podzielna przez 5 wyświetli dodatkowo napis "Hurra!" */

for (let number = 1; number <= 20; number++) {
    if (number%5 == 0) {
        console.log(number + ' Hurra!');
    } else {
        console.log(number);
    }
}