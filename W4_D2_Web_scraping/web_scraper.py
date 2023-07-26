from bs4 import BeautifulSoup # Importuje BeautifulSoup.
import requests # Importuje biblioteke "requests".

with open('/home/kali/Desktop/summer_of_code/W4_D2_Web_scraping/simple.html') as html_file: # Odczytuje plik jdo zmiennej html_file.
    soup = BeautifulSoup(html_file, 'lxml') # Przesylam plik do BeautifulSoup zmiennej "soup". Uzywam "lxml" jako parsera.
# print(soup.prettify()) # Drukuje sformatowana wersje "soup".

match = soup.title.text # Znajduje PIERWSZY tag <title> wraz z zawartoscia, oczyszczam go z samych tagow (.text) i zapisuje tekst do zmiennej "match".
print(match)

match2 = soup.find('div', class_= 'footer' ) # Zeby znalezc wszystkie dane tagi, wykorzystuje .find, a w nawiasie podaje atrybut szukanego taga.
print(match2.text) # Drukuje info bez tagow.

czas: 14:14