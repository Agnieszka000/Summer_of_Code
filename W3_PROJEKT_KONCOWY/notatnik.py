print('\nNOTATNIK ZADAN\n\nWybierz opcje:\n')

notes = {0 : 'Przykladowe zadanie.',}
notes_done = {0 : 'Przykladowe zadanie.',}

def task_done():
    print('\nWybierz numer zakonczonego zadania: ')
    task_done_key = input() # Input (= task_done_key) to jednoczesnie key ze slownika notes.
    task_done_new_key = len(notes_done) # Dla slownika notes_done musze zmienic key na dodawanie kluczy w formie roznacych liczb ze wzgledu na ryzyko nadpisania key:value w wypadku powtorzenia sie tej samej liczby dla kolejnego key ze slownika notes.
    task_done_value = notes[int(task_done_key)] # Przypisuje value klucza ze slownika notes do value dla slownika notes_done.
    notes_done[task_done_new_key] = task_done_value # Dopisuje nowy key i "stare" value do slownika notes_done.
    del notes[int(task_done_key)] # Kasuje zadanie o wybranym przez uzytkownika key ze slownika notes.

def tasks_list():
    print(notes)
    print ('\nJesli chcesz oznaczyc ktores z zadan jako wykonane, nacisnij "t":')
    option_yes = input()
    if option_yes == 't':
        task_done()
    else:
        start()   

def new_task():
    all_keys_list = [notes.keys()] # Wyciagam ze slownika "notes" wszystkie keys i tworze z nich liste "all_keys_list".
    all_keys_list = str(all_keys_list) # Program traktuje wszystkie keys jako jeden element, wiec musze zamienic to na str i pozbyc sie niepotrzebnych elementow.
    all_keys_list = all_keys_list.replace('[', '').replace(']', '').replace('dict_keys', '').replace('(', '').replace(')', '') # Pozbywam sie zbednych elementow, aby uzyskac liste numerow.
    all_keys_list.split(', ') # Rozdzielam str na pojedyncze numery
    new_task_key = int(all_keys_list[-1]) + 1 # Nadaje numer (nastepny z kolei key) nowemu zadaniu na liscie.
    new_task_value = input('\nWpisz zadanie do wykonania: ')
    notes[new_task_key] = new_task_value # Przypisuje value do key.
    print('\nZADANIE DODANE!')

    return notes

def start():
    intro = input ('\n1: dodaj nowe zadanie \n2: wyswietl liste zadan do zrobienia \n3: wyswietl liste ukonczonych zadan \n4: zamknij notatnik\n\n')
    if intro == '1':
        new_task()
        start()
    elif intro == '2':
        tasks_list()
        start()
    elif intro == '3':
        print(notes_done)
        start()
    else:
        quit()

start()