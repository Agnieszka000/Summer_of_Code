#Ask the user to write lenghths of a triangle's sides:
print('\nPodaj wymiary boku a, b oraz c, a ja sprawdze, czy da sie z nich utworzyc trojkat.\n')
a = int(input('Podaj dlugosc boku a:')) 
b = int(input('Podaj dlugosc boku b:')) 
c = int(input('Podaj dlugosc boku c:')) 

#Check if with it is possible to make a triangle with the given lengths (the longests side should be shorter than the sum of the other two):
if (a>b and a>c and a<b+c) or (b>a and b>c and b<a+c) or (c>a and c>b and c<a+b):
   print('\nSuper! Z tych wymiarow mozna stworzyc trojkat.')
elif a == b == c:
    print('\nSuper! Z tych wymiarow mozna stworzyc trojkat rownoboczny.')
else:
    print('\nNiestety z tych wymiarow nie powstanie trojkat.')
    quit()

#Check if is the pythagorean triangle:
if a**2+b**2==c**2:
    print('To jest trojkat pitagorejski.')
    #Check if the pythagorean triangle is an egyptian triangle:
    if (a/3 == b/4 == c/5):
        print('To jest trojkat egipski.')
else:
    print('To NIE jest trojkat pitagorejski.')