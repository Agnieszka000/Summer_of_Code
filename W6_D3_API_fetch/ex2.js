/* 2. Wykorzystaj endpoint https://reqres.in/api/users do wysłania zapytania POST i dodania nowego użytkownika.*/

fetch('https://reqres.in/api/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify ({
        first_name: 'Geenie'
    }),
}).then(res => {
    return res.json()
})
.then(data => console.log(data))
.catch(error => console.log('ERROR'))