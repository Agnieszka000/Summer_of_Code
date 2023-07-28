# Stworzenie prostego programu do wyodrębniania danych ze strony internetowej.

from bs4 import BeautifulSoup # I import BeautifulSoup.
import requests # I import "requests" BS library.

with open('index.html') as html_file: # I read file and write it to a variable. 
    soup = BeautifulSoup(html_file, 'lxml') # I send the file to BeautifulSoup zmiennej "soup". I use "lxml" as a parser.

tag1 = soup.find('ul') # I find a tag (<ul>)
y = tag1.text # I extract a text from the tag.
print(y)
