from bs4 import BeautifulSoup 
import requests

source = requests.get('https://flynerd.pl').text
soup = BeautifulSoup(source, 'lxml')

articles = soup.find_all('div', class_='article-container')
#print(articles)
print()

for article in articles:
    article_snippet = article.text
    print(article_snippet)
