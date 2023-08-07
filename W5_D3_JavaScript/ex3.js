/*Napisz skrypt, który wylosuje dowolną liczbę całkowitą od zera do 10 a następnie prosi użytkownika o jej zgadniecie, ale maksymalnie 5 razy

Gdy program działa, rozszerz go np. o podawanie informacji za którym razem udało się zgadnąć lub o wskazówki typu 
”Podana przez ciebie liczba jest większa/mniejsza od wylosowanej”*/

let number = parseInt(Math.round(Math.random() * 10)); //Math.round zaokragla float do najblizszej pelnej liczby.
let userNumber = parseInt(prompt("Wylosowalam liczbe. Zgadnij ja. Podaj od 0 do 10:"));

function inf() {
    if (userNumber < number) {
        alert('Podana liczna jest za mala');
    } else {
        alert('Podana liczba jest za duza.');
    }
}

function repeatNumber() {
  let n = parseInt(4);
  while (n > 0) {
  userNumber = parseInt(prompt('Niestety nie zgadlas. Sprobuj jeszcze raz:'));
    if (userNumber === number) {
      alert('Brawo. Zgadlas!');
      console.log('Brawo!');
      break;
      } else {
      inf();
      n = (n - 1);
      if (n === 0) {
        alert('Niestety to koniec gry.')
        console.log('GAME OVER')
      }
    }
  }
}


function guessNumber() {
  if (userNumber !== number) {
    inf();
    repeatNumber();
    } else {
    alert('Brawo. Zgadlas!');
    console.log('Brawo. Zgadlas!');
  }
}

guessNumber();