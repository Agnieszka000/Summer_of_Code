# Zadanie: Napisz skrypt "Szczęśliwy numerek"
# Skrypt losuje nr od 1 do 30. Następnie wyświetli napis "Szczęśliwy numer to {numer}. Dzisiaj nauczyciel nie może Cię odpytać na lekcji! Super!" 

import random
number = str(random.randrange(1, 31))

print ('Szczęśliwy numer to ' + number + '. Dzisiaj nauczyciel nie może Cię odpytać na lekcji! Super!')