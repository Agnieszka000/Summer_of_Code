# - wymyśl własny algorytm kodujący (możesz skorzystać z istniejących np. klasyczne/harcerskie) jako secret2.py
# RZUIPO-KFTU-TWRFS -> PYTHON JEST SUPER

message = 'RZUIPO-KFTU-TWRFS'

def decode_message():
    message_decoded  = message.replace('-',' ')
    message_decoded = message_decoded.replace('RZUIPO','PYTHON').replace('KFTU','JEST').replace('TWRFS','SUPER')
    print ('Message decoded: ' + message_decoded)

decode_message()