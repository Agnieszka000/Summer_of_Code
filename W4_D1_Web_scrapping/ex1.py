# Zadanie 1:
# W ramach rozgrzewki zastanów się jak wyciągniesz informacje z poniższej zmiennej
# html_input = "<ul><li>Jabłko</li><li>Gruszka</li><li>Pomarańcza</li></ul>"
# Twoim zadaniem jest użyć Pythona i odpowiednich metod typu string, aby wyodrębnić tylko tekst z wnętrza znaczników <li>, a następnie zapisać go jako listę:
# ['Jabłko', 'Gruszka', 'Pomarańcza']

#PROBLEM slowa tworza liste, alewszystkie sa jednym elementem. Trzeba je dodac do nowej listy jako pijedyncze slowa.


html_input = "<ul><li>Jabłko</li><li>Gruszka</li><li>Pomarańcza</li></ul>"
html_input = html_input.replace("<ul>" , "").replace("</ul>" , "").replace("</li>" , "").replace("<li>" , ", ") # Usuwam <ul>, </ul> oraz <li>
html_input = str(html_input) # Zamieniam zmienna na str.
html_input = html_input.split("</li>") # Dziele string na slowa. Slowa tworza liste.
html_input = str(html_input)
html_input = html_input.replace(", " , "" , 1)
print(html_input)