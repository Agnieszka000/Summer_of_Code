import requests
from requests.exceptions import RequestException # I import the exception module to handle possible errors.

try:
    r_get = requests.get('https://jsonplaceholder.typicode.com/posts/1') # I make a GET request.
except RequestException as err:
    print(f'Error occurred: {err}')
else:
    print(r_get)
    print('\nGET request status code: ' + str(r_get.status_code)) # I print the status code.
    print('\nGET request headers: \n\n' + str(r_get.headers)) # I print the headers.
    print('\nGET json content: \n\n' + str(r_get.json())) # I print the json content.

try:
    r_post = requests.post('https://jsonplaceholder.typicode.com/posts', data={'userId':'11'}) # I make a POST request.
except RequestException as err:
    print(f'Error occurred: {err}')
else:  
    print('\n POST request status code: ' + str(r_post.status_code)) # I check the status code to see if the data has been created.