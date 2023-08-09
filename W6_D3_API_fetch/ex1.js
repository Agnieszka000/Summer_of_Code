/* Wykorzystaj endpoint https://reqres.in/api/users?page=1 do pobrania listy użytkowników. */

fetch('https://reqres.in/api/users?page=1')
    .then(r => r.json())
    .then(data => console.log(data))