# Zapoznaj się z modułem random.
# >>> import random

# Stwórz prostą grę zgadywankę. Komputer losuje wartość z przedziału od 1-30. Poproś użytkownika o zgadnięcie liczby. Program pyta użytkownika o podanie liczby tak długo, 
# dopóki gracz nie zgadnie.

import random # I import the "random" module
my_number = random.randrange(1, 31) # I generate a random integer from the scope 1-30

print ('Guess the number between 1 and 30! ')
user_number = int(input()) # The user makes their guess. IMPORTANT! The input is string by default, so I have to turn it into an integer. Otherwise the programme will not be able to compare the input and the generated number correctly.

while my_number != user_number:
    print ('Wrong guess. Try again: ') 
    user_number = int(input()) # If the user's guess is incorrect, the programme asks them to guess the number again and repeats the loop.

print ('You nailed it! The correct number is: ' + str(my_number))