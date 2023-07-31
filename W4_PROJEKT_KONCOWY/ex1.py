# Celem tego projektu jest stworzenie web scrapera, który będzie wyciągał informacje o nadchodzących wydarzeniach IT z meetup.com w Twoim mieście (lub jeśli w Twoim mieście nic się nie dzieje to np. Warszawie).
#Jeśli strona meetup.com przerośnie Cię stopniem skomplikowania spróbuj z ciut prostrzą stroną jaką jest crossweb.pl

#Kroki do wykonania:
#   Zbadaj strukturę strony: Użyj narzędzi deweloperskich swojej przeglądarki, aby zbadać strukturę HTML strony Meetup.com. Zidentyfikuj tagi, które zawierają informacje o wydarzeniach IT.
#    Napisz scraper: Używając BeautifulSoup i Requests (lub korzystając z alternatywnych narzędzi jak Requests-HTML), napisz scraper, który będzie w stanie odwiedzić stronę, wyodrębnić potrzebne informacje i zapisać je w strukturze danych Pythona, takiej jak lista słowników. Informacje, które chcesz wyodrębnić, mogą obejmować nazwę wydarzenia, datę, czas, miejsce i opis.
#    (opcjonalnie - dla średniozaawansowanych) Dodaj obsługę błędów i debugowanie: Dodaj do swojego scrapera obsługę błędów, aby nie zawieszał się, gdy napotka nieoczekiwane dane.
#    Możesz to zrobić, używając instrukcji try/except w Pythonie. Dodaj również funkcje debugowania, które pomogą Ci zrozumieć, co się dzieje, gdy coś pójdzie nie tak.
#    Dodaj uprzejmy scraping: Dodaj do swojego scrapera opóźnienia między żądaniami, aby nie przeciążać serwera strony, którą odwiedzasz. Możesz to zrobić, używając funkcji time.sleep() w Pythonie. Zachowaj conajmniej 5 sekundowe odstępy między żądaniami.
#    Zapisz dane: Na koniec, zapisz wyodrębnione dane do pliku CSV lub tekstowego, aby można było je łatwo analizować lub przetwarzać w przyszłości.

from bs4 import BeautifulSoup
import requests
import time # Importuje modul 'time', zeby moc wykorzystac time.sleep().

source = requests.get('https://crossweb.pl/wydarzenia/trojmiasto/').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

# UWAGA! Wazne, zeby w tym miejscu podawac 'soup', a nie 'source'.
#events = soup.find('div', id='container').text # W soup.find nie trzeba wpisywac calej sciezki tagow, wystarczy tag, ktory nas interesuje. Ren wyswietli oczyszcony teks z div container.
#print(events)

events = soup.find('div', id='container') # Bez .text poniewaz potrzebuje cala zawartosc HTML, a nue sam tekst.

event_name = events.find_all('div', class_='tab-row fw-regular fs-standard fc-black-light') # Znajduje cala zawartosc dic=v class wraz z tagami.

#event_name1 = events.find_all('div', class_='tab-row fw-regular fs-standard fc-black-light')[0].get_text() # Znajduje i drukuje tekst tylko 1 elementu (o indeksie 0).
#print(event_name1)

event_number = 0
for event in event_name:
    event = events.find_all('div', class_='tab-row fw-regular fs-standard fc-black-light')[event_number].get_text()
    event = event.replace(' ' , '')
    with open('list.txt', 'a') as f: # Uzywam append mode (a), zeby program dodawal do pliku kazda info a nie zastepowal je jak w write mode (w).
      f.write(event)
    event_number += 1
    time.sleep(5)

# TERAZ TRZEBA OCZYSCIC TEKST Z BLANK LINES ORAZ WYRZUCIC NIEPOTRZEBNE TAGI.
