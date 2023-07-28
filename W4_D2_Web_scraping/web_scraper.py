from bs4 import BeautifulSoup # Importuje BeautifulSoup.
import requests # Importuje biblioteke "requests".

with open('simple.html') as html_file: # Odczytuje plik jdo zmiennej html_file.
    soup = BeautifulSoup(html_file, 'lxml') # Przesylam plik do BeautifulSoup zmiennej "soup". Uzywam "lxml" jako parsera.
# print(soup.prettify()) # Drukuje sformatowana wersje "soup".

for article in soup.find_all('div', class_='article'):

    print() #Pritns blank line between articles

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)