#Zadanie 5
#Spróbuj wyświetlić choinkę z trójkątów w taki sposób, aby każdy poziom choinki był o 1 wiersz dłuższy.
#1.poziom -> 2 linijki; lacznie maja byc 3 poziomy

#NIE DZIALA DLA WIEKSZYCH LICZB!!!

for i in range(1,4):
    if i == 1:
        x = '@'
        y = '@@'
        print(x)
        print(y)
    elif i == 2:
        print(x)
        print(y)
        print(x+y)
    else:        
        print(x)
        print(y)
        print(x+y)
        print(x * (i + 1))