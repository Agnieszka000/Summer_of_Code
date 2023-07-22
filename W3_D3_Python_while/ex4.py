# Zadanie 4
# Napisz skrypt obliczający wartość silnii. Rozwiąż zadanie za pomocą pętli for oraz pętli while.
# Wejście: „Podaj dowolną liczbę całkowitą do 15:” 4
# Wyjście: 4! = 24

import math # I import the "math" module to count factorials.

print ('Write a number up to 15 and I\'ll count its factorial: ')
number = int(input())

while number <= 15:
    print('The factorial is: ' +str(math.factorial(number))) # The programme counts the factorial and prints the outcome.
    quit() # The programme exits the loop.