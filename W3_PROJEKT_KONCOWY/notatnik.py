print('\nNOTATNIK ZADAN\n\nWybierz opcje:\n')

def new_task():
    task = input('Dodaj zadanie: ')
    add_new_task = {id:task}
    notes.update(add_new_task)
    print ('Zadanie dodane.')
    print(notes)
    
def start():
    start = input ('1: dodaj nowe zadanie \n2: wyswietl liste zadan do zrobienia \n3: wyswietl liste ukonczonych zadan \n4: zamknij notatnik\n\n')
    if start == '1':
        id = int(id) + 1
        new_task()
        start()
    else:
        quit()

notes = {}
id = int(0)  
start()
