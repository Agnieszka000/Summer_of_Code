# Zadanie 3
# Rozszerz grę z punktu powyżej. Gracz powinen otrzymać informację czy jego liczba jest za duża czy za mała.

import random 
my_number = random.randrange(1, 31)

print ('Guess the number between 1 and 30! ')
user_number = int(input()) 

while my_number != user_number:
    # Here goes the added part of code:
    if user_number > my_number:
        print('Wrong guess! The number is too big. Try again: ')
    else:
        print('Wrong guess! The number is too small. Try again: ')
    # The end of the added part.
    user_number = int(input())
    
print ('You nailed it! The correct number is: ' + str(my_number))