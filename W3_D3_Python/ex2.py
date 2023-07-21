#Zadanie 3
#Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.

#Tutaj dodajesz 1 tylko element wszystkie imiona na raz. raczej możesz pobrać wszystkie imiona np rozdzielone przecinkiem i wykorzystać metodę split()
#Zyskasz wtedy listę imion

names = (input('Podaj imiona: '))
names = names.split(' ' or ', ')

for name in names:
    print ('Czesc, ' + name + '!')