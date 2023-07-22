# - napisz program secret3.py, które odkoduje twoją wiadomość

print ('Podaj zakodowane haslo:')
message = input ()

if message == 'RZUIPO-KFTU-TWRFS':
    print ('Haslo poprawne.')
    print('Dekoduje.')
else:
    print('Haslo nieporawne')
    quit()

def decoded_message():
    message_decoded  = message.replace('-',' ')
    message_decoded = message_decoded.replace('RZUIPO','PYTHON').replace('KFTU','JEST').replace('TWRFS','SUPER')
    print ('Message decoded: ' + message_decoded)

decoded_message()