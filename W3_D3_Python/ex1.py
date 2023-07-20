#Zadanie 1
#Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
#Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

numbers = (1,2,3,4,5,6,7,8,9,10)

for number in numbers:
    if number <= 1:
        sum1 = number + (number-1)
        print(sum1)
    elif 10 >= number >= 2:
        sum2 = number + sum1  
        print(sum2)
        sum1 = sum2