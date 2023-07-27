# Wykorzystaj poniższy fragment kodu, aby wykonać zadanie
# import requests #skorzystaj z pakietu request

# req = requests.get("http://numbersapi.com/random/year") # odpytujemy API
# print(req.text)

# Sprawdź czy pobrany tekst ze strony zawiera liczbę "13"
# Zapytaj użytkownika o dowolny ciąg znaków.
# Sprawdź czy tekst ze strony zawiera też ciąg zadany przez użytkownika

import requests

req = requests.get("http://numbersapi.com/random/year") # odpytujemy API
print(req.text)
print()

if '13' in req:
    print ('Ten tekst zawiera liczbe 13.')
else:
    print ('Ten tekst nie zawiera liczby 13.')

text = req.text
user_input = input('\nWpisz zwrot. Program sprawdzi, czy znajduje sie on w tekscie:\n')

if user_input in text:
    print ('Ten zwrot znajduje sie w tekscie.')
else:
    print('Tego zwrotu nie ma w tekscie.')